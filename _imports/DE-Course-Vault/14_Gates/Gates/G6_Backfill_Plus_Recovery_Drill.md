---
type: gate
gate_id: G6
status: not_started
last_run:
evidence_links: []
tags: [course/gates]
---

# G6 — Backfill + Recovery Drill

## Why this gate exists
Proves you can safely replay history and recover from failure.

## Pass criteria (must all be true)
- [ ] You can run a date-range backfill safely
- [ ] You can intentionally break the pipeline and recover using the runbook
- [ ] You can explain what data got reprocessed

## Evidence required
- [ ] Backfill command + output
- [ ] Runbook steps you followed
- [ ] Evidence of recovery

## Common failure modes
- Backfill duplicates data
- Partial failures leave inconsistent state
- No runbook; you guess

## Next step (smallest move)
- Add a `--start/--end` backfill mode and document it.
