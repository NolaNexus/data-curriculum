---
type: gate
gate_id: G1
status: not_started
last_run: null
evidence_links: []
tags:
  - course/gates
id: gate_g1_raw_immutability_provenance
title: G1 — Raw Immutability + Provenance
---

# G1 — Raw Immutability + Provenance

## Why this gate exists
Proves you can ingest data without destroying the original and you can explain where every record came from.

## Pass criteria (must all be true)
- [ ] Raw payload stored immutably (files or object storage)
- [ ] Metadata includes `run_id`, `fetched_at_utc`, `source`, checksum/hash
- [ ] Raw data is never overwritten

## Evidence required
- [ ] Example raw file/object key
- [ ] Example metadata record
- [ ] Commit hash

## Common failure modes
- Overwriting raw files
- No run_id; can’t trace outputs
- Timestamps in local time

## Next step (smallest move)
- Implement one ingest for one source + metadata row.
