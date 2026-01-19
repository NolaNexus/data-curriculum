---
type: index
updated: 2026-01-18T00:00:00.000Z
tags:
  - course/module
  - module/shipping
id: doc_data_product_shipping_index
title: Data Product Shipping — Index
---

# Data Product Shipping — Index

## Outcome
Your pipeline runs like a product: CLI, configs, Docker stack, docs, versioning, CI, and sane security defaults.


## Next up (do this next)
- [ ] Read the next lesson in **Ordered path**
- [ ] Do the first relevant **Lab** and capture evidence
- [ ] Write a quick log entry in Logbook (what worked, what broke, what you learned)
- **Gate:** G5_Publish_Plus_Metrics_Plus_Dashboard

### Definition of done
You are done with this module when you can **run the system**, show **evidence**, and pass its gate(s).


## Lessons
1. 01_CLI_Command_Design
2. 02_Config_and_Contracts
3. 03_Docker_Compose_as_Product
4. 04_Release_Process
5. 05_CI_Precommit_and_Release_Hygiene
6. 06_Security_Privacy_for_Personal_Data_Projects

## Labs
- 01_Lab_CLI_Wiring
- 02_Lab_One_Command_Bootstrap
- 03_Lab_Add_Precommit_and_CI




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
