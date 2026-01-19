---
type: gate
gate_id: G7
status: not_started
last_run:
evidence_links: []
tags: [course/gates]
---

# G7 — Fresh Machine Bootstrap

## Why this gate exists
Proves a stranger can run it quickly.

## Pass criteria (must all be true)
- [ ] Fresh machine setup works in ≤ 15 min
- [ ] `docker compose up` brings up stack
- [ ] One command runs end-to-end

## Evidence required
- [ ] Bootstrap script output
- [ ] `docker compose ps` screenshot
- [ ] End-to-end command output

## Common failure modes
- Hidden dependencies
- Missing env vars
- Manual steps not documented

## Next step (smallest move)
- Write a bootstrap script and test it in a clean container/VM.
