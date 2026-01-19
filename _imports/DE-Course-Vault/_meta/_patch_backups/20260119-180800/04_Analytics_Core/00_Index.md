---
type: index
tags: [course/module, module/analytics]
---

# Analytics Core — Index

## Outcome
Define metrics and publish a dashboard/report that supports decisions.

## Lessons
- [[04_Analytics_Core/Lessons/01_Metrics_That_Dont_Lie]]
- [[04_Analytics_Core/Lessons/02_Cohorts_and_Funnels]]
- [[04_Analytics_Core/Lessons/03_Dashboard_Design]]
- [[04_Analytics_Core/Lessons/04_Static_Report_Build]]

## Labs
- [[04_Analytics_Core/Labs/01_Lab_Metric_Catalog]]
- [[04_Analytics_Core/Labs/02_Lab_Dashboard_v1]]

## Auto-list (Dataview, optional)
```dataview
TABLE type, status, timebox_minutes
FROM "04_Analytics_Core"
WHERE type AND type != "index"
SORT file.path ASC
```



## Resources (auto)
```dataview
TABLE format, source, phase, status, topics, file.link AS "Resource"
FROM "08_Resources_Library"
WHERE type = "resource" AND contains(modules, "04_Analytics_Core")
SORT status ASC, file.name ASC
```
