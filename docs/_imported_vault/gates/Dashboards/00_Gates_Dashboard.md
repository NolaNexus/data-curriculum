---
type: dashboard
created: 2026-01-18T00:00:00.000Z
tags:
  - course/gates
  - course/dashboard
id: doc_gates_dashboard_control_panel
title: Gates Dashboard (control panel)
---

# Gates Dashboard (control panel)

If Dataview is enabled, this page stays fresh automatically.

## Next gate to push
```dataview
TABLE gate_id, status, last_run, file.link AS gate
FROM "14_Gates/Gates"
WHERE status != "passed"
SORT gate_id ASC
LIMIT 3
```

## Missing evidence (quick shame, productive shame)
```dataview
TABLE gate_id, status, evidence_links, file.link AS gate
FROM "14_Gates/Gates"
WHERE status = "passed" AND (length(evidence_links) = 0 OR !evidence_links)
SORT gate_id ASC
```

## Recent gate runs
```dataview
TABLE gate_id, result, created, file.link AS run
FROM "11_Logbook/Gate_Runs"
WHERE type = "gate-run"
SORT created DESC
LIMIT 10
```

## Tip
Every week, aim to move **one gate** forward with real evidence.
