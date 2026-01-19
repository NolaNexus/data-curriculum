---
type: index
updated: 2026-01-18
tags: [course/module, module/de-core]
---

# Data Engineering Core — Index

## Outcome
Ingest data safely, model it with dbt, enforce quality, and run on a schedule with logs.


## Next up (do this next)
- [ ] Read the next lesson in **Ordered path**
- [ ] Do the first relevant **Lab** and capture evidence
- [ ] Write a quick log entry in [[11_Logbook/README|Logbook]] (what worked, what broke, what you learned)
- **Gate:** [[14_Gates/Gates/G1_Raw_Immutability_Plus_Provenance]]

### Definition of done
You are done with this module when you can **run the system**, show **evidence**, and pass its gate(s).


## Ordered path
1. [[03_Data_Engineering_Core/Lessons/01_Raw_Silver_Gold]]
2. [[03_Data_Engineering_Core/Lessons/02_Immutable_Raw_and_Metadata]]
3. [[03_Data_Engineering_Core/Lessons/03_Idempotency_and_Backfills]]
4. [[03_Data_Engineering_Core/Lessons/04_dbt_Staging_and_Marts]]
5. [[03_Data_Engineering_Core/Lessons/05_Data_Quality_Gates]]
6. [[03_Data_Engineering_Core/Lessons/06_Scheduling_and_Observability]]
7. [[03_Data_Engineering_Core/Lessons/07_Schema_Contracts_and_Evolution]]
8. [[03_Data_Engineering_Core/Lessons/08_Performance_Fundamentals_Parquet_Indexes_Explain]]

## Labs
- [[03_Data_Engineering_Core/Labs/01_Lab_Raw_Ingestion_With_Metadata]]
- [[03_Data_Engineering_Core/Labs/02_Lab_dbt_Project_Setup]]
- [[03_Data_Engineering_Core/Labs/03_Lab_Quality_Tests]]
- [[03_Data_Engineering_Core/Labs/04_Lab_Scheduled_Run_With_Logs]]
- [[03_Data_Engineering_Core/Labs/05_Lab_Golden_Files_and_Schema_Drift]]
- [[03_Data_Engineering_Core/Labs/06_Lab_Query_Plans_and_Partitioning]]




## Resources (auto)
```dataview
TABLE format, source, phase, status, topics, file.link AS "Resource"
FROM "08_Resources_Library"
WHERE type = "resource" AND contains(modules, "03_Data_Engineering_Core")
SORT status ASC, file.name ASC
```
## Gate alignment
- [[14_Gates/Gates/G1_Raw_Immutability_Plus_Provenance]]
- [[14_Gates/Gates/G2_Idempotent_Reruns]]
- [[14_Gates/Gates/G3_dbt_Models_Plus_Tests_Plus_Docs]]
- [[14_Gates/Gates/G4_Scheduled_Run_Plus_Logs_Plus_run_id]]

## Auto-list (Dataview, optional)
```dataview
TABLE module, type, status, timebox_minutes
FROM "03_Data_Engineering_Core"
WHERE type AND type != "index"
SORT file.path ASC
```
