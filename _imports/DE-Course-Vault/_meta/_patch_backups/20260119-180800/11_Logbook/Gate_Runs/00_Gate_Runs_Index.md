---
type: index
created: 2026-01-18
tags: [course/gates, course/logbook]
---

# Gate Runs

Create a new note from `09_Templates/Gate_Run_Template.md` each time you attempt a gate.

## Dataview (optional)
```dataview
TABLE gate_id, result, created, timebox_minutes
FROM "10_Logbook/Gate_Runs"
WHERE type = "gate-run"
SORT created DESC
```
