---
type: system
updated: 2026-01-18
tags: [course/system, course/gates]
---

# Gates System (proof-based learning)

Gates turn “coverage” into **evidence**. If you pass the gates, you’re not missing anything important for v1.

## How to use gates
- Work normally (lessons/labs/videos), but every week you try to **move one gate forward**.
- A gate is “passed” only when you attach **evidence**:
  - command output
  - screenshots/URLs
  - commit hash
  - runbook excerpt
  - dbt docs link, etc.

## Gate progression (recommended)
1) G0 Repo Bootstrap
2) G1 Raw Immutability + Provenance
3) G2 Idempotent Reruns
4) G3 dbt Models + Tests + Docs
5) G4 Scheduled Run + Logs + run_id
6) G5 Publish (dashboard/report) + metric definitions
7) G6 Backfill + Recovery Drill
8) G7 Fresh Machine Bootstrap
9) G8 Capstone Demo (end-to-end)

## Integration into your daily practice
- **Build days:** pick one challenge that advances today’s gate.
- **Review days:** practice-test the gate from memory (“how does G4 work?”).
- **Integrate days:** run the pipeline end-to-end and capture evidence.

## Links
- [[13_Gates/_indexes/00_Gates_Index]]
- [[09_Templates/Gate_Evidence_Template]]
- [[09_Templates/Gate_Run_Template]]
