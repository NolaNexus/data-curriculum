---
type: moc
updated: 2026-01-18T00:00:00.000Z
tags:
  - course/cloud
id: doc_cloud_track_personal_projects
title: Cloud Track (personal projects)
---

# Cloud Track (personal projects)

## Next up (do this next)
- [ ] Read the next lesson in **Ordered path**
- [ ] Do the first relevant **Lab** and capture evidence
- [ ] Write a quick log entry in Logbook (what worked, what broke, what you learned)

### Definition of done
You are done with this module when you can **run the system**, show **evidence**, and pass its gate(s).

Goal: cloud deployments **without** surprise bills and without breaking your local-first workflow.

## Recommended path (low-cost, high-learning)
1. Cloud mirror (object storage for raw + artifacts)
2. Serverless scheduled run (container job)
3. Managed Postgres (optional)
4. Static report publishing
5. IaC lite (reproducibility + destroy path)

## Cost guardrails (do this first)
- 00_Cost_Guardrails_Checklist
- 01_Lifecycle_Retention_Rules
- 02_Cloud_Cleanup_Runbook
- 00_Cloud_Cost_Checks_Index
- 00_Provider_Notes_Index

## Lessons
- 01_Cloud_Basics_for_DE
- 02_Cost_Guardrails
- 03_Object_Storage_and_Artifacts
- 04_Serverless_Jobs_and_Scheduling
- 05_Managed_Postgres_Options
- 06_IaC_Lite_OpenTofu_Terraform_Mindset

## Labs
- Lab_A_Cloud_Mirror_Object_Storage
- Lab_B_Serverless_Scheduled_Run
- Lab_C_Managed_Postgres_Migration
- Lab_D_Static_Report_Publish
- Lab_E_IaC_Lite_Minimal_Stack




## Resources (auto)
```dataview
TABLE format, source, phase, status, topics, file.link AS "Resource"
FROM "08_Resources_Library"
WHERE type = "resource" AND contains(modules, "07_Cloud_Track")
SORT status ASC, file.name ASC
```
## Gate integration
- G1/G2: mirror raw + metadata to object storage
- G4: schedule cloud job or local timer
- G5: publish static report/dashboard via cloud
- G7: IaC makes “fresh machine bootstrap” repeatable
