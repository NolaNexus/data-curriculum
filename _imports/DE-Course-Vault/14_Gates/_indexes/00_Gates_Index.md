---
type: moc
created: 2026-01-18
tags: [course/gates]
---

# Gates (v1 completeness)

**Rule:** You don’t “finish a phase” by reading about it. You finish it by **passing the gate**.

## Gates
- [[14_Gates/Gates/G0_Repo_Bootstrap]]
- [[14_Gates/Gates/G1_Raw_Immutability_Plus_Provenance]]
- [[14_Gates/Gates/G2_Idempotent_Reruns]]
- [[14_Gates/Gates/G3_dbt_Models_Plus_Tests_Plus_Docs]]
- [[14_Gates/Gates/G4_Scheduled_Run_Plus_Logs_Plus_run_id]]
- [[14_Gates/Gates/G5_Publish_Plus_Metrics_Plus_Dashboard]]
- [[14_Gates/Gates/G6_Backfill_Plus_Recovery_Drill]]
- [[14_Gates/Gates/G7_Fresh_Machine_Bootstrap]]
- [[14_Gates/Gates/G8_Capstone_Demo]]

## Where to store evidence
- Evidence notes: `14_Gates/Evidence/`
- Gate run logs: `11_Logbook/Gate_Runs/`

## Dataview (optional)
```dataview
TABLE status, last_run, evidence_links
FROM "14_Gates/Gates"
SORT file.name ASC
```
