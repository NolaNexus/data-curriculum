---
type: index
created: 2026-01-18T00:00:00.000Z
tags:
  - course/cloud
id: doc_provider_notes
title: Provider notes
---

# Provider notes

Create one provider note per provider/project using:
`09_Templates/Cloud_Provider_Note_Template.md`

## Dataview (optional)
```dataview
TABLE provider, budget_cap_monthly, created, file.link
FROM "07_Cloud_Track/Provider_Notes"
WHERE type = "cloud-provider-note"
SORT created DESC
```
