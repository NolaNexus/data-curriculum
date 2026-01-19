---
type: gate
gate_id: G3
status: not_started
last_run: null
evidence_links: []
tags:
  - course/gates
id: gate_g3_dbt_models_tests_docs
title: G3 — dbt Models + Tests + Docs
---

# G3 — dbt Models + Tests + Docs

## Why this gate exists
Proves you can model data and enforce quality gates.

## Pass criteria (must all be true)
- [ ] dbt project runs: `dbt build`
- [ ] At least staging + mart models exist
- [ ] Tests: unique + not_null + freshness (where meaningful)
- [ ] dbt docs build succeeds

## Evidence required
- [ ] `dbt build` output
- [ ] `dbt docs generate` output
- [ ] Screenshot/link for docs site (even local)

## Common failure modes
- Grain not stated → wrong joins
- Missing tests on keys
- Docs not maintained

## Next step (smallest move)
- Add one staging model, one mart model, and three tests.
