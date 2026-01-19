---
type: dashboard
tags:
  - course/dashboard
id: doc_progress_board
title: Progress board
---

# Progress board

## Current focus
- Module:
- This week’s deliverable:
- Next session starts with:

## Phase gates (definition of done)
### Phase 0 — Ergonomics
- [ ] Repo boots on a fresh machine
- [ ] `make test` runs (or `just test`)
- [ ] ruff/format + pytest run in CI (or local hooks)

### Phase 1 — DE core spine
- [ ] Raw is immutable (+ provenance metadata)
- [ ] Silver + Gold models exist with tests
- [ ] Scheduled run + logs + failure visibility
- [ ] Idempotent reruns + backfills exist

### Phase 2 — Analytics
- [ ] Metrics have written definitions (grain, filters, window)
- [ ] Dashboard/report is repeatable

### Phase 4 — Shipping
- [ ] One-command bootstrap
- [ ] One-command run
