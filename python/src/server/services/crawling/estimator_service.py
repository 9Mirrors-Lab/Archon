"""
Pre-crawl Estimator Service

Provides a lightweight estimation of crawl scope (pages) and runtime (ETA)
without launching a full crawl. It prefers sitemap-based counting and falls
back to a shallow link scan. Network work is intentionally minimal and
guarded by timeouts.
"""

from __future__ import annotations

import asyncio
import re
import time
from dataclasses import dataclass
from typing import Any, Dict, List, Set, Tuple
from urllib.parse import urljoin, urlparse

import httpx

from ...config.logfire_config import get_logger
from ..credential_service import credential_service
from .helpers.url_handler import URLHandler


logger = get_logger(__name__)


LINK_HREF_RE = re.compile(r'href=["\']([^"\']+)["\']', re.IGNORECASE)


@dataclass
class EstimateResult:
    method_used: str
    estimated_pages: int
    sample_avg_ms: float
    concurrency: int
    eta_minutes: float
    notes: List[str]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "method_used": self.method_used,
            "estimated_pages": self.estimated_pages,
            "sample_avg_ms": round(self.sample_avg_ms, 2),
            "concurrency": self.concurrency,
            "eta_minutes": round(self.eta_minutes, 2),
            "notes": self.notes,
        }


async def _get_crawl_settings() -> Tuple[int, float]:
    """Return (concurrency, delay_seconds). Delay is optional and used for ETA safety."""
    try:
        settings = await credential_service.get_credentials_by_category("rag_strategy")
        concurrency = int(settings.get("CRAWL_MAX_CONCURRENT", "10"))
        delay = float(settings.get("CRAWL_DELAY_BEFORE_HTML", "1.0"))
        return max(1, concurrency), max(0.0, delay)
    except Exception as e:
        logger.warning(f"Estimator: failed to load crawl settings, using defaults: {e}")
        return 10, 1.0


async def _fetch_text(client: httpx.AsyncClient, url: str, timeout: float = 10.0) -> str | None:
    try:
        resp = await client.get(url, timeout=timeout)
        if resp.status_code == 200 and resp.text:
            return resp.text
        return None
    except Exception as e:
        logger.debug(f"Estimator: fetch failed for {url}: {e}")
        return None


def _same_domain(base: str, candidate: str) -> bool:
    try:
        b = urlparse(base).netloc
        c = urlparse(candidate).netloc
        return bool(b) and (b == c)
    except Exception:
        return False


def _extract_links(html: str, base_url: str) -> Set[str]:
    links: Set[str] = set()
    if not html:
        return links
    for match in LINK_HREF_RE.finditer(html):
        href = match.group(1)
        if href.startswith("#"):
            continue
        absolute = urljoin(base_url, href)
        if _same_domain(base_url, absolute) and not URLHandler.is_binary_file(absolute):
            links.add(absolute)
    return links


async def _estimate_from_sitemap(client: httpx.AsyncClient, start_url: str) -> Tuple[int, List[str]]:
    notes: List[str] = []
    parsed = urlparse(start_url)
    base = f"{parsed.scheme}://{parsed.netloc}"
    candidates = [
        urljoin(base + "/", "sitemap.xml"),
        urljoin(base + "/", "sitemap_index.xml"),
    ]

    import xml.etree.ElementTree as ET

    total_urls: Set[str] = set()
    for sm_url in candidates:
        text = await _fetch_text(client, sm_url)
        if not text:
            continue
        try:
            root = ET.fromstring(text)
        except Exception:
            notes.append(f"Failed to parse {sm_url}")
            continue

        loc_tags = root.findall(".//{*}loc")
        if not loc_tags:
            continue

        for loc in loc_tags[:5000]:  # hard cap
            loc_url = (loc.text or "").strip()
            if not loc_url:
                continue
            if loc_url.endswith(".xml") and "sitemap" in loc_url:
                # nested sitemap: fetch a small subset to avoid heavy work
                nested_text = await _fetch_text(client, loc_url)
                if not nested_text:
                    continue
                try:
                    nroot = ET.fromstring(nested_text)
                    for nloc in nroot.findall(".//{*}loc")[:5000]:
                        u = (nloc.text or "").strip()
                        if u and _same_domain(start_url, u) and not URLHandler.is_binary_file(u):
                            total_urls.add(u)
                except Exception:
                    notes.append(f"Failed to parse nested sitemap {loc_url}")
            else:
                if _same_domain(start_url, loc_url) and not URLHandler.is_binary_file(loc_url):
                    total_urls.add(loc_url)

    if total_urls:
        notes.append("Used sitemap for estimation")
        return len(total_urls), notes
    return 0, notes


async def _sample_latency(client: httpx.AsyncClient, urls: List[str], max_samples: int = 5) -> float:
    samples = urls[:max_samples]
    if not samples:
        return 1500.0  # fallback 1.5s

    durations: List[float] = []
    for u in samples:
        start = time.perf_counter()
        _ = await _fetch_text(client, u)
        durations.append((time.perf_counter() - start) * 1000.0)
    return sum(durations) / max(1, len(durations))


async def estimate_crawl(url: str, max_depth: int = 2) -> Dict[str, Any]:
    """Estimate pages and ETA for a crawl.

    Strategy: try sitemap first; if not available, shallow scan start page and a
    subset of depth-2 pages. Compute average latency and estimate ETA using
    configured concurrency.
    """
    url = url.strip()
    if not url.startswith(("http://", "https://")):
        raise ValueError("URL must start with http:// or https://")

    concurrency, delay = await _get_crawl_settings()
    notes: List[str] = []

    async with httpx.AsyncClient(follow_redirects=True) as client:
        # 1) Try sitemap
        sm_count, sm_notes = await _estimate_from_sitemap(client, url)
        notes.extend(sm_notes)
        if sm_count > 0:
            avg_ms = await _sample_latency(client, [url])
            eta_minutes = ((sm_count / max(1, concurrency)) * ((avg_ms / 1000.0) + delay)) / 60.0
            return EstimateResult(
                method_used="sitemap",
                estimated_pages=sm_count,
                sample_avg_ms=avg_ms,
                concurrency=concurrency,
                eta_minutes=eta_minutes,
                notes=notes,
            ).to_dict()

        # 2) Fallback: breadth-first shallow scan honoring max_depth (sampled)
        max_depth = max(1, min(int(max_depth), 5))
        sample_per_depth = 10  # cap network work

        visited: Set[str] = set([url])
        frontier: Set[str] = set([url])
        all_discovered: Set[str] = set([url])
        depth = 0
        while depth < max_depth and frontier:
            depth += 1
            next_frontier: Set[str] = set()
            # sample a subset of current frontier for expansion
            seeds = list(frontier)[: min(sample_per_depth, len(frontier))]
            new_count = 0
            for seed in seeds:
                if seed in visited:
                    continue
                visited.add(seed)
                h = await _fetch_text(client, seed)
                links = _extract_links(h or "", seed)
                links = {u for u in links if _same_domain(url, u)}
                new_links = links - all_discovered
                new_count += len(new_links)
                next_frontier |= new_links
                all_discovered |= new_links
            notes.append(f"Depth{depth} sampled: {len(seeds)} pages → {new_count} new links")
            frontier = next_frontier

        unique_urls = all_discovered
        est_pages = max(1, len(unique_urls))
        avg_ms = await _sample_latency(client, list(unique_urls))
        # Include processing overhead factor from settings if available
        try:
            settings = await credential_service.get_credentials_by_category("rag_strategy")
            overhead = float(settings.get("ESTIMATE_PROCESSING_OVERHEAD", "1.6"))
        except Exception:
            overhead = 1.6
        eta_minutes = ((est_pages / max(1, concurrency)) * ((avg_ms / 1000.0) + delay)) / 60.0
        eta_minutes *= overhead
        return EstimateResult(
            method_used="shallow_scan",
            estimated_pages=est_pages,
            sample_avg_ms=avg_ms,
            concurrency=concurrency,
            eta_minutes=eta_minutes,
            notes=notes,
        ).to_dict()


