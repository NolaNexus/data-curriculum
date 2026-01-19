---
type: index
tags:
  - course/resources
id: doc_resources_library
title: Resources Library
---

# Resources Library

## Capture rules
- Always include **why** + **one action**
- Prefer primary docs (official) before opinion posts
- Link each resource from a module index where it applies

## Inbox
- Resource_Inbox


## Browse
- Curated (by module)
- Videos
- Docs
- Courses
- Papers
- Repos
- Bookmarks

## All resources (auto)
```dataview
TABLE format, source, phase, status, topics, file.link AS "Resource"
FROM "08_Resources_Library"
WHERE type = "resource"
SORT status ASC, file.name ASC
```
