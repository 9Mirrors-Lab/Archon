name: "Task/Bug Fix PRP Template"
description: |
  Focused PRP for a single task or bug fix with clear problem definition,
  expected behavior, implementation steps, and validation criteria.

---

## Metadata

- **Document Type**: prp
- **Title**: Task or Bug Fix
- **Version**: 1.0
- **Author**: [Your Name]
- **Date**: YYYY-MM-DD
- **Status**: draft | review | approved | deprecated

## Goal

**Task Goal**: [Describe the single outcome to achieve]

## Why

- [Impact on users or system if not fixed]
- [How this fits into larger project goals]
- [Priority level and urgency]

## What

### Description

[Specific problem to solve and expected outcome]

### Current Behavior

[What happens now (the problem)]

### Expected Behavior

[What should happen instead]

### Acceptance Criteria

- [ ] Specific testable condition 1
- [ ] Specific testable condition 2
- [ ] No regressions in existing functionality

## Context

### Affected Files

```yaml
- path: src/component.tsx
  reason: Contains the bug or needs the change
- path: src/service.ts
  reason: Related logic that may need updates
```

### Root Cause

[Analysis of why this issue exists]

### Related Issues

- [Link to GitHub issue or ticket]
- [Related bugs or enhancement requests]

### Dependencies

- [Other tasks that must be completed first]
- [External services or APIs involved]

## Implementation Steps

1. Reproduce the issue
   - Create a test case that demonstrates the problem
2. Identify root cause
   - Debug and trace the issue to its source
3. Implement fix
   - Apply the minimal change that resolves the issue
4. Test solution
   - Verify the fix works and doesn’t break other functionality
5. Update documentation
   - Update any relevant docs or comments

## Validation

### Reproduction Test

- Steps to reproduce the original issue
- Verify the issue no longer occurs

### Regression Tests

- Run existing test suite to ensure no regressions
- Test related functionality manually

### Edge Cases

- Test boundary conditions
- Test error scenarios

---

## Final Checklist

- [ ] All acceptance criteria met
- [ ] Unit/integration tests updated and passing
- [ ] No regressions in impacted areas
- [ ] Documentation updated (if applicable)
