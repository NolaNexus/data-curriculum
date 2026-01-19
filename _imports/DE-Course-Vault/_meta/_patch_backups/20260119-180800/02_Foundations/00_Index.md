---
type: index
updated: 2026-01-18
tags: [course/module, module/foundations]
---

# Foundations — Index

## Outcome
Build a small Python project, query data with SQL, use Git safely, and operate basic logs.

## Ordered path
1. [[02_Foundations/Lessons/01_Python_Project_Shape]]
2. [[02_Foundations/Lessons/02_SQL_Joins_and_Keys]]
3. [[02_Foundations/Lessons/03_SQL_Window_Functions]]
4. [[02_Foundations/Lessons/04_Git_Solo_PR_Workflow]]
5. [[02_Foundations/Lessons/05_Linux_Shell_For_Data_Pipelines]]

## Labs
- [[02_Foundations/Labs/00_Lab_Repo_Scaffold]]
- [[02_Foundations/Labs/01_Lab_SQL_Practice_Set]]
- [[02_Foundations/Labs/02_Lab_Shell_And_Logs_Drill]]




## Resources (auto)
```dataview
TABLE format, source, phase, status, topics, file.link AS "Resource"
FROM "08_Resources_Library"
WHERE type = "resource" AND contains(modules, "02_Foundations")
SORT status ASC, file.name ASC
```
## Gate alignment
- Primary: [[14_Gates/Gates/G0_Repo_Bootstrap]]

## Auto-list (Dataview, optional)
```dataview
TABLE module, type, status, timebox_minutes
FROM "02_Foundations"
WHERE type AND type != "index"
SORT file.name ASC
```
