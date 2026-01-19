---
type: index
tags: [course/resources]
---

# Resources Library

## Capture rules
- Always include **why** + **one action**
- Prefer primary docs (official) before opinion posts
- Link each resource from a module index where it applies

## Inbox
- [[Resource_Inbox]]


## Browse
- [[08_Resources_Library/Curated/_Indexes/00_Curated_Resources_Home|Curated (by module)]]
- [[08_Resources_Library/Videos/00_Index|Videos]]
- [[08_Resources_Library/Docs/00_Index|Docs]]
- [[08_Resources_Library/Courses/00_Index|Courses]]
- [[08_Resources_Library/Papers/00_Index|Papers]]
- [[08_Resources_Library/Repos/00_Index|Repos]]
- [[08_Resources_Library/Bookmarks/00_Index|Bookmarks]]

## All resources (auto)
```dataview
TABLE format, source, phase, status, topics, file.link AS "Resource"
FROM "08_Resources_Library"
WHERE type = "resource"
SORT status ASC, file.name ASC
```
