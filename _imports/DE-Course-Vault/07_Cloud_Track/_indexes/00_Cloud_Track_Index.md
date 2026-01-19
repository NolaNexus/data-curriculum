---
type: moc
updated: 2026-01-18
tags: [course/cloud]
---

# Cloud Track (personal projects)

## Next up (do this next)
- [ ] Read the next lesson in **Ordered path**
- [ ] Do the first relevant **Lab** and capture evidence
- [ ] Write a quick log entry in [[11_Logbook/README|Logbook]] (what worked, what broke, what you learned)

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
- [[07_Cloud_Track/Cost_Guardrails/00_Cost_Guardrails_Checklist]]
- [[07_Cloud_Track/Cost_Guardrails/01_Lifecycle_Retention_Rules]]
- [[07_Cloud_Track/Cost_Guardrails/02_Cloud_Cleanup_Runbook]]
- [[11_Logbook/Cloud_Cost_Checks/00_Cloud_Cost_Checks_Index]]
- [[07_Cloud_Track/Provider_Notes/00_Provider_Notes_Index]]

## Lessons
- [[07_Cloud_Track/Lessons/01_Cloud_Basics_for_DE]]
- [[07_Cloud_Track/Lessons/02_Cost_Guardrails]]
- [[07_Cloud_Track/Lessons/03_Object_Storage_and_Artifacts]]
- [[07_Cloud_Track/Lessons/04_Serverless_Jobs_and_Scheduling]]
- [[07_Cloud_Track/Lessons/05_Managed_Postgres_Options]]
- [[07_Cloud_Track/Lessons/06_IaC_Lite_OpenTofu_Terraform_Mindset]]

## Labs
- [[07_Cloud_Track/Labs/Lab_A_Cloud_Mirror_Object_Storage]]
- [[07_Cloud_Track/Labs/Lab_B_Serverless_Scheduled_Run]]
- [[07_Cloud_Track/Labs/Lab_C_Managed_Postgres_Migration]]
- [[07_Cloud_Track/Labs/Lab_D_Static_Report_Publish]]
- [[07_Cloud_Track/Labs/Lab_E_IaC_Lite_Minimal_Stack]]




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
