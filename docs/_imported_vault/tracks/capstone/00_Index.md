---
type: index
updated: 2026-01-18T00:00:00.000Z
tags:
  - course/capstone
id: doc_capstone_index
title: Capstone — Index
---

# Capstone — Index

## Next up (do this next)
- [ ] Read the next lesson in **Ordered path**
- [ ] Do the first relevant **Lab** and capture evidence
- [ ] Write a quick log entry in Logbook (what worked, what broke, what you learned)
- **Gate:** G8_Capstone_Demo

### Definition of done
You are done with this module when you can **run the system**, show **evidence**, and pass its gate(s).

## The point
The capstone is where the course stops being “a curriculum” and becomes **a shipped data product**.

## Start here
- 00_Capstone_Spec
- 00_Milestone_Map

## Operate + demo
- 00_Runbook
- 00_Demo_Checklist

## Spec subfolders
- 00_Datasets_Index
- 00_Metrics_Index
- 00_Decisions_Index




## Resources (auto)
```dataview
TABLE format, source, phase, status, topics, file.link AS "Resource"
FROM "08_Resources_Library"
WHERE type = "resource" AND contains(modules, "07_Capstone")
SORT status ASC, file.name ASC
```
## Gate alignment
- Passing the gates **is** completing the capstone:
  - 00_Gates_Dashboard
