---
type: reference
updated: 2026-01-18
tags: [course/analytics, topic/metrics]
---

# Metric catalog (single source of truth)

**Rule:** dashboards do not define metrics — metric notes do. Dashboards *link back* to these definitions.

## Capstone metrics
- [[08_Capstone/01_Spec/Metrics/00_Metrics_Index]]

## Template
- [[09_Templates/Metric_Definition_Template]]

## Dataview (optional)
```dataview
TABLE grain, window, filters, status, file.link
FROM "08_Capstone/01_Spec/Metrics"
WHERE type = "metric-definition"
SORT file.name ASC
```
