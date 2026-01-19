---
type: index
created: 2026-01-18
tags: [course/gates]
---

# Gate evidence

Store evidence notes here (command output, screenshots, links, commit hashes).

## Dataview (optional)
```dataview
TABLE gate_id, status, created, file.link
FROM "13_Gates/Evidence"
WHERE type = "gate-evidence"
SORT created DESC
```
