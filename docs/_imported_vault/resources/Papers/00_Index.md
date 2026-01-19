---
type: index
created: 2026-01-18T00:00:00.000Z
tags:
  - course/resources
  - course/papers
id: doc_papers
title: Papers
---

# Papers

## How to use
- Add resources as individual notes in this folder (one note per resource).
- Include minimal frontmatter so the index stays sortable:
  - `type: resource`
  - `source:` (e.g., freeCodeCamp, docs, paper)
  - `topics:` (list)
  - `phase:` (optional)
  - `status:` (queued | in_progress | done)

## Dataview (optional)
```dataview
TABLE source, phase, topics, status
FROM "08_Resources_Library/Papers"
WHERE type = "resource"
SORT source ASC
```
