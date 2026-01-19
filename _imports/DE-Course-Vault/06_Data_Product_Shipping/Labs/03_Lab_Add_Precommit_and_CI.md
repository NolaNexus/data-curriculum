---
type: lab
module: Shipping
timebox_minutes: 120
status: planned
tags: [course/lab, topic/ci]
created: 2026-01-18
---

# Lab — Add pre-commit + CI

## Goal
Make “quality” automatic and boring.

## Steps (generic)
- [ ] Add a pre-commit config (ruff/format + pytest quick)
- [ ] Add CI workflow (GitHub Actions or equivalent):
  - install deps
  - run `ruff` and `pytest`
  - run `dbt build` or `dbt parse` if dbt exists
- [ ] Make CI badge visible in README (optional)

## Evidence
- Screenshot of passing CI run
- Commit hash


# Success criteria
- [ ] (define a testable outcome)
- [ ] (define a reproducible run command)


# Reflection
- What was the sharp edge?
- What would you do differently next time?
