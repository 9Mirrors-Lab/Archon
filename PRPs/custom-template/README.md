# Custom Feature PRP Template Kit

This folder contains a portable Feature PRP template you can copy outside this repo and use with Archon MCP.

## Files
- `feature-prp.template.json`: Structured PRP JSON compatible with `manage_document` (PRPViewer-ready).

## How to use
2) Open the JSON template and customize defaults (title, goals, phases, tasks).
3) Upload via MCP using `manage_document` with `document_type="prp"` and the JSON as `content`.

### Example (MCP payload)
```json
{
  "tool": "manage_document",
  "args": {
    "action": "add",
    "project_id": "<PROJECT_ID>",
    "document_type": "prp",
    "title": "New Feature Implementation",
    "content": { /* contents of feature-prp.template.json */ },
    "metadata": { "author": "User", "tags": ["feature", "prp"] }
  }
}
```

### Notes
- PRP content must include: `goal`, `why`, `what`, `context`, `implementation_blueprint`, `validation`.
- `document_type` should be set to `"prp"` inside `content` (already included).
- Dates can be set to today’s ISO `YYYY-MM-DD`.

### Optional
If you prefer markdown-only, store as `document_type="markdown"` and paste your content in `content.markdown`, but PRPViewer features (phases, validation gates) require the structured JSON format above.
