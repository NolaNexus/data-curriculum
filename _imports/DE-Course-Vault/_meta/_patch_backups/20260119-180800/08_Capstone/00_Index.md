---
type: index
updated: 2026-01-18
tags: [course/capstone]
---

# Capstone — Index

## The point
The capstone is where the course stops being “a curriculum” and becomes **a shipped data product**.

## Start here
- [[07_Capstone/01_Spec/00_Capstone_Spec]]
- [[07_Capstone/02_Milestones/00_Milestone_Map]]

## Operate + demo
- [[07_Capstone/03_Runbook/00_Runbook]]
- [[07_Capstone/04_Demo/00_Demo_Checklist]]

## Spec subfolders
- [[07_Capstone/01_Spec/Datasets/00_Datasets_Index]]
- [[07_Capstone/01_Spec/Metrics/00_Metrics_Index]]
- [[07_Capstone/01_Spec/Decisions/00_Decisions_Index]]




## Resources (auto)
```dataview
TABLE format, source, phase, status, topics, file.link AS "Resource"
FROM "08_Resources_Library"
WHERE type = "resource" AND contains(modules, "07_Capstone")
SORT status ASC, file.name ASC
```
## Gate alignment
- Passing the gates **is** completing the capstone:
  - [[14_Gates/Dashboards/00_Gates_Dashboard]]
