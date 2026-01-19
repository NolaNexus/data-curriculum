---
type: reference
updated: 2026-01-18T00:00:00.000Z
tags:
  - course/analytics
  - topic/metrics
id: doc_metric_catalog_single_source_of_truth
title: Metric catalog (single source of truth)
---

# Metric catalog (single source of truth)

**Rule:** dashboards do not define metrics — metric notes do. Dashboards *link back* to these definitions.

## Capstone metrics
- 00_Metrics_Index

## Template
- Metric_Definition_Template

## Dataview (optional)
```dataview
TABLE grain, window, filters, status, file.link
FROM "08_Capstone/01_Spec/Metrics"
WHERE type = "metric-definition"
SORT file.name ASC
```
