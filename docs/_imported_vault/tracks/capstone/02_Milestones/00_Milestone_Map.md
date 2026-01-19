---
type: plan
updated: 2026-01-18T00:00:00.000Z
tags:
  - course/capstone
  - course/plan
id: doc_capstone_milestone_map_maps_directly_to_gates
title: Capstone milestone map (maps directly to gates)
---

# Capstone milestone map (maps directly to gates)

This is the “what ship looks like” path. Each milestone should produce evidence you can attach to a gate.

## M0 — Repo boots (G0)
**Outcome:** repo scaffold + tooling works on a fresh machine.
- Deliverables: `pyproject.toml`, `src/`, `tests/`, `make/just`, README bootstrap
- Evidence: passing `ruff` + `pytest`

## M1 — Raw ingestion + metadata (G1)
**Outcome:** one real source ingested, raw stored immutably, provenance recorded.
- Deliverables: raw storage convention + metadata table/file
- Evidence: raw object key + metadata row

## M2 — Idempotency + reruns (G2)
**Outcome:** rerun produces same result; duplicates are prevented.
- Deliverables: rerun strategy documented; duplicate detection test
- Evidence: before/after row counts or checksums

## M3 — Models + tests + docs (G3)
**Outcome:** dbt build passes; docs are generated.
- Deliverables: staging + mart; tests on keys; docs generated
- Evidence: `dbt build` output + docs screenshot/link

## M4 — Publish + metric truth (G5)
**Outcome:** one dashboard/report output + metrics are defined outside the dashboard.
- Deliverables: at least 1 metric definition note; 1 tile/chart linked to it
- Evidence: screenshot/URL + metric note link

## M5 — Schedule + observability (G4)
**Outcome:** daily run is scheduled; logs persist; failures are visible.
- Deliverables: cron/systemd/Prefect/Dagster schedule; run_id in logs
- Evidence: schedule config + log snippet

## M6 — Backfill + recovery drill (G6)
**Outcome:** replay a date range safely and recover from an intentional break.
- Deliverables: backfill mode; runbook procedure; “what changed” note
- Evidence: backfill output + runbook steps + recovery evidence

## M7 — Fresh machine + demo (G7, G8)
**Outcome:** a stranger can run it quickly; you can demo it coherently.
- Deliverables: 15-minute bootstrap; 5–10 minute demo script
- Evidence: bootstrap proof + demo checklist completion
