---
type: spec
updated: 2026-01-18
status: draft
tags: [course/capstone]
---

# Capstone spec

This spec makes the capstone concrete and prevents “infinite exploration syndrome.”

## Problem statement
- Decision supported:
- Who uses it:
- What changes because this exists:

## Domain (choose one)
- patch notes / change logs
- home network telemetry
- personal finance exports
- anything you collect daily

## Data sources
Create dataset cards here:
- [[08_Capstone/01_Spec/Datasets/00_Datasets_Index]]

Minimum v1 source set:
- [ ] 1 primary source (API/files/scrape/logs)
- [ ] 1 optional enrichment source (optional)

## Metrics (single source of truth)
Create metric definitions here:
- [[08_Capstone/01_Spec/Metrics/00_Metrics_Index]]

Minimum v1 metrics:
- [ ] 1 “core” metric that answers the problem statement
- [ ] 1 “quality/health” metric (freshness, volume, error rate)

## Architecture choices (v1)
- Workhorse DB: Postgres or DuckDB
- Analytics engine: DuckDB or dbt + Postgres
- Storage for raw: filesystem or object storage
- Orchestration: cron/systemd first; upgrade later

## Acceptance criteria (maps to gates)
- [ ] G1: raw immutable + provenance
- [ ] G2: idempotent rerun
- [ ] G3: dbt models/tests/docs
- [ ] G4: scheduled run + logs + run_id
- [ ] G5: published output + metric definitions
- [ ] G6: backfill + recovery drill
- [ ] G7: fresh machine bootstrap
- [ ] G8: demo script + checklist complete

## Decision log
Keep major choices documented here:
- [[08_Capstone/01_Spec/Decisions/00_Decisions_Index]]
