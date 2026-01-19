---
type: index
updated: 2026-01-18
tags: [course/module, module/shipping]
---

# Data Product Shipping — Index

## Outcome
Your pipeline runs like a product: CLI, configs, Docker stack, docs, versioning, CI, and sane security defaults.

## Lessons
1. [[06_Data_Product_Shipping/Lessons/01_CLI_Command_Design]]
2. [[06_Data_Product_Shipping/Lessons/02_Config_and_Contracts]]
3. [[06_Data_Product_Shipping/Lessons/03_Docker_Compose_as_Product]]
4. [[06_Data_Product_Shipping/Lessons/04_Release_Process]]
5. [[06_Data_Product_Shipping/Lessons/05_CI_Precommit_and_Release_Hygiene]]
6. [[06_Data_Product_Shipping/Lessons/06_Security_Privacy_for_Personal_Data_Projects]]

## Labs
- [[06_Data_Product_Shipping/Labs/01_Lab_CLI_Wiring]]
- [[06_Data_Product_Shipping/Labs/02_Lab_One_Command_Bootstrap]]
- [[06_Data_Product_Shipping/Labs/03_Lab_Add_Precommit_and_CI]]




## Resources (auto)
```dataview
TABLE format, source, phase, status, topics, file.link AS "Resource"
FROM "08_Resources_Library"
WHERE type = "resource" AND contains(modules, "06_Data_Product_Shipping")
SORT status ASC, file.name ASC
```
## Gate alignment
- Supports: G4, G7, G8 (shipping quality makes the gates passable under pressure)

## Auto-list (Dataview, optional)
```dataview
TABLE module, type, status, timebox_minutes
FROM "06_Data_Product_Shipping"
WHERE type AND type != "index"
SORT file.path ASC
```
