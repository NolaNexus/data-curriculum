---
type: index
created: 2026-01-18
tags: [course/capstone, topic/datasets]
---

# Capstone datasets (cards)

Create dataset cards from `09_Templates/Dataset_Card_Template.md`.

## Dataview (optional)
```dataview
TABLE source, status, file.link
FROM "08_Capstone/01_Spec/Datasets"
WHERE type = "dataset-card"
SORT file.name ASC
```
