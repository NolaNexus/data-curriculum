---
type: index
created: 2026-01-18T00:00:00.000Z
tags:
  - course/cloud
  - topic/cost
  - course/logbook
id: doc_cloud_cost_checks
title: Cloud cost checks
---

# Cloud cost checks

Create a note from `09_Templates/Cloud_Cost_Check_Template.md` 2–3 times per week.

## Dataview (optional)
```dataview
TABLE provider, estimate, status, created, file.link
FROM "11_Logbook/Cloud_Cost_Checks"
WHERE type = "cloud-cost-check"
SORT created DESC
LIMIT 20
```
