---
type: snippets
created: 2026-01-18
tags: [course/snippets, course/gates, course/cloud]
---

# Dashboard snippets (copy/paste)

These are small blocks you can paste into your existing notes without restructuring the vault.

## 1) Progress dashboard: “Gates panel”
Paste this near the top of your progress dashboard note:

```dataview
TABLE gate_id, status, last_run, file.link AS gate
FROM "13_Gates/Gates"
SORT gate_id ASC
```

## 2) Module indexes: “Today’s gate focus”
Paste into each module index (Foundations, DE Core, Analytics, Shipping):

```dataview
LIST FROM "13_Gates/Gates"
WHERE status != "passed"
SORT gate_id ASC
```

## 3) Cloud tracker: “Cost guardrails panel”
Paste into your Cloud Track index:

```dataview
LIST FROM "07_Cloud_Track/Cost_Guardrails"
SORT file.name ASC
```

## 4) Daily plans: “Gate moved today?”
Add this checkbox to the bottom of daily plan notes:

- [ ] Gate moved today: [[13_Gates/Gates/G0_Repo_Bootstrap]] (update link)

## 5) Evidence capture shortcut
When you pass a gate, create a note from:
`09_Templates/Cloud_Cost_Check_Template.md` (cost)
`09_Templates/Gate_Evidence_Template.md` (gate)
