name: "Architecture/Planning PRP Template"
description: |
  Strategic PRP for system architecture and planning with current-state analysis,
  proposed architecture, implementation phases, metrics, and risks.

---

## Metadata

- **Document Type**: prp
- **Title**: System Architecture and Planning
- **Version**: 1.0
- **Author**: [Your Name]
- **Date**: YYYY-MM-DD
- **Status**: draft | review | approved | deprecated

## Goal

Design and plan system architecture for [specific system/feature]

## Why

- Strategic business objective driving this architecture
- Technical debt or scalability issues to address
- Future growth and maintainability requirements

## What

### Scope

System boundaries, affected components, and integration points

### Deliverables

- Comprehensive architecture documentation
- Component specifications and interfaces
- Implementation roadmap and timeline
- Migration/deployment strategy

### Constraints

- Budget and timeline limitations
- Technical constraints and dependencies
- Regulatory or compliance requirements

## Current State Analysis

### Strengths

- What works well in the current system
- Stable components that should be preserved
- Existing patterns worth maintaining

### Weaknesses

- Performance bottlenecks and limitations
- Maintenance and scaling challenges
- Security or reliability concerns

### Opportunities

- Modern technologies to leverage
- Process improvements to implement
- Business capabilities to enable

### Threats

- Risks during transition period
- Dependencies on legacy systems
- Resource and timeline constraints

## Proposed Architecture

### Overview

High-level description of the new architecture

### Components

```yaml
frontend:
  technology: React 18 with TypeScript
  patterns: Component composition with ShadCN UI
  state_management: React hooks with context for global state
backend:
  technology: FastAPI with async Python
  patterns: Service layer with repository pattern
  database: Supabase PostgreSQL with proper indexing
realtime:
  technology: Socket.IO for live updates
  patterns: Event-driven communication with proper error handling
infrastructure:
  deployment: Docker containers with orchestration
  monitoring: Comprehensive logging and metrics
  security: OAuth2 with proper encryption
```

### Data Flow

- User interaction → Frontend validation → API call
- Backend processing → Database operations → Response
- Real-time events → Socket.IO → UI updates

### Integration Points

- External APIs and their usage patterns
- Third-party services and data sources
- Legacy system interfaces

## Implementation Phases

### Phase 1: Foundation

- Duration: 2–3 weeks
- Objective: Core infrastructure and basic functionality
- Deliverables:
  - Database schema and basic API endpoints
  - Authentication and authorization system
  - Core UI components and routing
- Success Criteria:
  - Basic user flows working end-to-end
  - Core API responses under 200ms
  - Authentication working with test users

### Phase 2: Features

- Duration: 3–4 weeks
- Objective: Primary feature implementation
- Deliverables:
  - Complete feature set with UI
  - Real-time updates and notifications
  - Data validation and error handling
- Success Criteria:
  - All major user stories implemented
  - Real-time features working reliably
  - Comprehensive error handling

### Phase 3: Optimization

- Duration: 1–2 weeks
- Objective: Testing, optimization, and deployment
- Deliverables:
  - Comprehensive test suite
  - Performance optimization
  - Production deployment
- Success Criteria:
  - Test coverage >80%
  - Performance targets met
  - Successful production deployment

## Success Metrics

### Performance

- API response time <200ms for 95% of requests
- UI load time <2 seconds
- Support 1000+ concurrent users

### Quality

- Test coverage >80%
- Zero critical security vulnerabilities
- Mean time to recovery <15 minutes

### Business

- User task completion rate >90%
- Feature adoption >60% within first month
- User satisfaction score >4.5/5

## Risks and Mitigation

### Technical Risks

```yaml
- risk: Integration complexity with legacy systems
  mitigation: Phased approach with fallback options
- risk: Performance issues at scale
  mitigation: Load testing and optimization in early phases
```

### Business Risks

```yaml
- risk: Timeline delays due to scope creep
  mitigation: Clear requirements and change control process
```

---

## Final Checklist

- [ ] Architecture doc reviewed and approved
- [ ] Phase plan agreed with timelines
- [ ] Risks acknowledged with mitigations
- [ ] Success metrics defined and measurable
