---
type: moc
created: 2026-01-18T00:00:00.000Z
tags:
  - course/gates
id: doc_gates_v1_completeness
title: Gates (v1 completeness)
---

# Gates (v1 completeness)

**Rule:** You don’t “finish a phase” by reading about it. You finish it by **passing the gate**.

## Gates
- G0_Repo_Bootstrap
- G1_Raw_Immutability_Plus_Provenance
- G2_Idempotent_Reruns
- G3_dbt_Models_Plus_Tests_Plus_Docs
- G4_Scheduled_Run_Plus_Logs_Plus_run_id
- G5_Publish_Plus_Metrics_Plus_Dashboard
- G6_Backfill_Plus_Recovery_Drill
- G7_Fresh_Machine_Bootstrap
- G8_Capstone_Demo

## Where to store evidence
- Evidence notes: `14_Gates/Evidence/`
- Gate run logs: `11_Logbook/Gate_Runs/`

## Dataview (optional)
```dataview
TABLE status, last_run, evidence_links
FROM "14_Gates/Gates"
SORT file.name ASC
```
