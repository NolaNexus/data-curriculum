---
type: lab
module: DE Core
timebox_minutes: 120
status: planned
created: 2026-01-19
tags: [course/lab, topic/orchestration]
---

# Lab objective
Schedule the pipeline and make logs easy to find.

# Steps
1. Choose scheduling: cron/systemd or Prefect/Dagster.
2. Ensure each run has a run_id.
3. Persist logs to a known path.
4. Simulate a failure and confirm it’s visible.

# Success criteria
- [ ] You can answer: “did last night’s run succeed?”
- [ ] You can locate logs for a specific run_id
