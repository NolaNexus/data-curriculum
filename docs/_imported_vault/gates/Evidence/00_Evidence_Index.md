---
type: index
created: 2026-01-18T00:00:00.000Z
tags:
  - course/gates
id: doc_gate_evidence
title: Gate evidence
---

# Gate evidence

Store evidence notes here (command output, screenshots, links, commit hashes).

## Dataview (optional)
```dataview
TABLE gate_id, status, created, file.link
FROM "14_Gates/Evidence"
WHERE type = "gate-evidence"
SORT created DESC
```
