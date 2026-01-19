---
type: index
updated: 2026-01-18T00:00:00.000Z
tags:
  - course/module
  - module/de-core
id: doc_data_engineering_core_index
title: Data Engineering Core — Index
---

# Data Engineering Core — Index

## Outcome
Ingest data safely, model it with dbt, enforce quality, and run on a schedule with logs.


## Next up (do this next)
- [ ] Read the next lesson in **Ordered path**
- [ ] Do the first relevant **Lab** and capture evidence
- [ ] Write a quick log entry in Logbook (what worked, what broke, what you learned)
- **Gate:** G1_Raw_Immutability_Plus_Provenance

### Definition of done
You are done with this module when you can **run the system**, show **evidence**, and pass its gate(s).


## Ordered path
1. 01_Raw_Silver_Gold
2. 02_Immutable_Raw_and_Metadata
3. 03_Idempotency_and_Backfills
4. 04_dbt_Staging_and_Marts
5. 05_Data_Quality_Gates
6. 06_Scheduling_and_Observability
7. 07_Schema_Contracts_and_Evolution
8. 08_Performance_Fundamentals_Parquet_Indexes_Explain

## Labs
- 01_Lab_Raw_Ingestion_With_Metadata
- 02_Lab_dbt_Project_Setup
- 03_Lab_Quality_Tests
- 04_Lab_Scheduled_Run_With_Logs
- 05_Lab_Golden_Files_and_Schema_Drift
- 06_Lab_Query_Plans_and_Partitioning




## Resources (auto)
```dataview
TABLE format, source, phase, status, topics, file.link AS "Resource"
FROM "08_Resources_Library"
WHERE type = "resource" AND contains(modules, "03_Data_Engineering_Core")
SORT status ASC, file.name ASC
```
## Gate alignment
- G1_Raw_Immutability_Plus_Provenance
- G2_Idempotent_Reruns
- G3_dbt_Models_Plus_Tests_Plus_Docs
- G4_Scheduled_Run_Plus_Logs_Plus_run_id

## Auto-list (Dataview, optional)
```dataview
TABLE module, type, status, timebox_minutes
FROM "03_Data_Engineering_Core"
WHERE type AND type != "index"
SORT file.path ASC
```
