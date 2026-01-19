---
type: index
created: 2026-01-18T00:00:00.000Z
tags:
  - course/capstone
  - topic/metrics
id: doc_capstone_metrics_definitions
title: Capstone metrics (definitions)
---

# Capstone metrics (definitions)

Create metric notes from `09_Templates/Metric_Definition_Template.md`.

## Dataview (optional)
```dataview
TABLE grain, window, filters, owner, status
FROM "08_Capstone/01_Spec/Metrics"
WHERE type = "metric-definition"
SORT file.name ASC
```
