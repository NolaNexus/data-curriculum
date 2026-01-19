---
type: gate
gate_id: G2
status: not_started
last_run: null
evidence_links: []
tags:
  - course/gates
id: gate_g2_idempotent_reruns
title: G2 — Idempotent Reruns
---

# G2 — Idempotent Reruns

## Why this gate exists
Proves re-running doesn’t duplicate or corrupt results.

## Pass criteria (must all be true)
- [ ] Ingestion rerun with same inputs produces identical outputs
- [ ] Transform rerun produces same modeled tables
- [ ] You can explain your idempotency strategy (upsert, partition overwrite, checksum skip, etc.)

## Evidence required
- [ ] Checksums/row counts before & after rerun
- [ ] Short note describing strategy
- [ ] Commit hash

## Common failure modes
- Duplicate rows on rerun
- Non-deterministic transforms
- Missing primary keys / natural keys

## Next step (smallest move)
- Add a rerun test and fail the pipeline if duplicates appear.
