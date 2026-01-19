---
type: index
created: 2026-01-18
tags: [course/resources, course/videos]
---

# Videos

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
FROM "08_Resources_Library/Videos"
WHERE type = "resource"
SORT source ASC
```
