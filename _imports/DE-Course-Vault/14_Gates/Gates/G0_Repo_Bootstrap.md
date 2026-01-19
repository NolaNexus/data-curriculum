---
type: gate
gate_id: G0
status: not_started
last_run:
evidence_links: []
tags: [course/gates]
---

# G0 — Repo Bootstrap

## Why this gate exists
Proves you can reproduce the dev environment and basic repo ergonomics.

## Pass criteria (must all be true)
- [ ] Repo has `pyproject.toml`, `src/`, `tests/`
- [ ] `ruff` and `pytest` run locally
- [ ] `make` or `just` has at least `lint` and `test`
- [ ] README Getting Started works

## Evidence required
- [ ] `tree` output (top level)
- [ ] `pytest` output
- [ ] `ruff` output
- [ ] link to README section / commit hash

## Common failure modes
- Missing src layout
- Tests not runnable on fresh machine
- Tools installed globally instead of per-project

## Next step (smallest move)
- Create the repo scaffold lab and commit.
