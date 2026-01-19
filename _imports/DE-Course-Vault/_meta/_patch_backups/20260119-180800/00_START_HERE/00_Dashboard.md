---
type: dashboard
status: active
created: 2026-01-19
tags: [course/dashboard]
---

# Vault Dashboard

## Quick jumps
- [[01_Syllabus/00_Syllabus|Syllabus]]
- [[13_Gates/_indexes/00_Gates_Index|Gates Index]]
- [[13_Gates/Dashboards/00_Gates_Dashboard|Gates Dashboard]]
- [[07_Capstone|Capstone]]
- [[10_Logbook|Logbook]]
- [[11_Troubleshooting|Troubleshooting]]
- [[08_Resources_Library|Resources Library]]



## Resource inbox (latest)
```dataview
TABLE format, source, phase, topics, file.link AS "Resource"
FROM "08_Resources_Library"
WHERE type = "resource" AND (status = "inbox" OR status = "unread")
SORT added DESC, file.mtime DESC
LIMIT 12
```

---

## Now (last touched)
```dataview
TABLE file.mtime AS "Updated", file.folder AS "Folder"
FROM ""
SORT file.mtime DESC
LIMIT 12
```

## Open tasks anywhere
```dataview
TASK
FROM ""
WHERE !completed
SORT file.mtime DESC
```

---

## Tracks at a glance (auto-indexes)

### Foundations
```dataview
LIST
FROM "02_Foundations"
SORT file.name ASC
```

### Data Engineering Core
```dataview
LIST
FROM "03_Data_Engineering_Core"
SORT file.name ASC
```

### Analytics Core
```dataview
LIST
FROM "04_Analytics_Core"
SORT file.name ASC
```

### Data Science (optional)
```dataview
LIST
FROM "05_Data_Science_Optional"
SORT file.name ASC
```

### Data Product Shipping
```dataview
LIST
FROM "06_Data_Product_Shipping"
SORT file.name ASC
```

### Cloud Track
```dataview
LIST
FROM "07_Cloud_Track"
SORT file.name ASC
```

### Capstone
```dataview
LIST
FROM "07_Capstone"
SORT file.name ASC
```

---

## Gates (recent)
```dataview
TABLE file.mtime AS "Updated"
FROM "13_Gates"
SORT file.mtime DESC
LIMIT 15
```

## Logbook (latest entries)
```dataview
TABLE file.mtime AS "Updated"
FROM "10_Logbook"
SORT file.mtime DESC
LIMIT 10
```

---

## Inbox (choose ONE convention)

### Option A: tag stuff with #inbox
```dataview
LIST
FROM #inbox
SORT file.mtime DESC
```

### Option B: frontmatter `status: inbox`
```dataview
LIST
FROM ""
WHERE status = "inbox"
SORT file.mtime DESC
```
