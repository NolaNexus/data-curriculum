---
type: lesson
created: 2026-01-18T00:00:00.000Z
timebox_minutes: 180
tags:
  - course/cloud
  - course/lab
kind: lab
estimated_time_minutes: 180
id: les_lab_b_serverless_scheduled_run_container_job
title: Lab B — Serverless scheduled run (container job)
---

# Lab B — Serverless scheduled run (container job)

## Outcome
Run the pipeline headlessly as a container on a schedule.

## Recommended
- Cloud Run (services or jobs); documented free-tier compute seconds. citeturn0search6turn0search14

## Steps (generic)
1. Build your container image
2. Push image to a registry
3. Deploy job/service with env vars
4. Schedule daily execution
5. Persist logs and include `run_id`

## Pass criteria
- [ ] One run succeeds
- [ ] Logs include run_id for every step
- [ ] A failed run is visible and debuggable

## Maps to gates
- G4, G7


# Success criteria
- [ ] (define a testable outcome)
- [ ] (define a reproducible run command)


# Evidence
```text
(paste command output, screenshots filenames, links, or notes)
```


# Reflection
- What was the sharp edge?
- What would you do differently next time?
