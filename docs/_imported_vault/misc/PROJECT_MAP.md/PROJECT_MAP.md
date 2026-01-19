---
type: map
status: active
created: 2026-01-19T00:00:00.000Z
tags:
  - course/map
id: doc_project_map
title: Project map
---

# Project map

The vault is organized like a **game campaign**: fundamentals → pipeline core → analytics → shipping → (optional) cloud/ML → capstone.

## Top-level structure

- `00_START_HERE/` → operating manual: how to study, set up, track progress
- `01_Syllabus/` → pacing, outcomes, rubrics, weekly plan template
- `02_Foundations/` → Python + SQL + Git + shell (the “tools of thought”)
- `03_Data_Engineering_Core/` → raw→silver→gold, dbt, orchestration, quality, performance
- `04_Analytics_Core/` → metrics, cohorts, dashboards, reporting
- `05_Data_Science_Optional/` → only after gold tables are reliable
- `06_Data_Product_Shipping/` → CLI, config, Docker, CI, releases, privacy basics
- `07_Cloud_Track/` → optional cloud habits + cost guardrails
- `08_Capstone/` → spec → milestones → runbook → demo checklist
- `09_Resources_Library/` → resource inbox + curated resource cards
- `10_Templates/` → templates for lessons/labs/reviews/debug logs
- `11_Logbook/` → weekly notes + gate runs
- `12_Troubleshooting/` → checklists + known failure patterns
- `13_Assessments/` → self-checks per module
- `14_Gates/` → “evidence checkpoints” (mini certification exams)
- `99_Glossary/` → terms with examples
- `_meta/` → scripts and patch notes (non-learning, maintenance only)

## The minimal path (anti-overwhelm route)

**Goal:** ship a tiny real pipeline you can run in one command.

1) `02_Foundations` (enough Python/SQL/Git/shell to function)
2) `03_Data_Engineering_Core` lessons 01–06 + labs 01–04
3) `14_Gates` through **G4** (scheduled run + logs)
4) `04_Analytics_Core` lesson 01 + lab 02 (a first dashboard/report)
5) `06_Data_Product_Shipping` lab 02 (one-command bootstrap)
6) `08_Capstone` spec + milestone 1

Everything else is *upgrade content*.

## “What counts as done?” (learning foundations)

A unit is “done” when you have:
- **Evidence** (a link, screenshot, command output, or a committed repo artifact)
- A short **reflection** (3–6 bullets: what worked, what broke, what you’d do next)
- A **next action** (the smallest possible next move)

Use:
- `10_Templates/Gate_Evidence_Template.md`
- `11_Logbook/` weekly notes

