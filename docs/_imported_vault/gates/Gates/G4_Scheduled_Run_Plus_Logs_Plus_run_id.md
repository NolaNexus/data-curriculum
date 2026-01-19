---
type: gate
gate_id: G4
status: not_started
last_run: null
evidence_links: []
tags:
  - course/gates
id: gate_g4_scheduled_run_logs_run_id
title: G4 — Scheduled Run + Logs + run_id
---

# G4 — Scheduled Run + Logs + run_id

## Why this gate exists
Proves the system runs unattended and you can debug it.

## Pass criteria (must all be true)
- [ ] A scheduler runs daily (cron/systemd/Prefect/Dagster)
- [ ] Logs are persisted (file or log system)
- [ ] Each step logs a shared `run_id`
- [ ] Failure is visible (non-zero exit, alert or obvious log)

## Evidence required
- [ ] Scheduler config snippet
- [ ] Example log lines with run_id
- [ ] Screenshot of last run success/failure

## Common failure modes
- Silent failures
- Logs overwritten
- No run identifiers; can’t correlate steps

## Next step (smallest move)
- Add run_id wiring + daily timer.
