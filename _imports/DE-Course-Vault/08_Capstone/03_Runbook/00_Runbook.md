---
type: runbook
updated: 2026-01-18
tags: [course/capstone, course/runbook]
---

# Capstone runbook

This runbook exists so Future-You (or a stranger) can operate the project without guesswork.

## Quickstart (fresh machine)
1. Install prerequisites (Docker, Python, `uv`/Poetry)
2. Copy `.env.example` → `.env`
3. `docker compose up -d`
4. `make all` (or `just all`)

**Success criteria:** pipeline completes and a published output appears.

## Commands (single source of truth)
- `make ingest` — fetch/store raw immutably
- `make build` — transforms + dbt models/tests
- `make report` — publish dashboard/report artifacts
- `make backfill START=... END=...` — replay safely
- `make logs RUN_ID=...` — find correlated logs

## Environment variables
Document everything needed to run headless:
- DB connection
- object storage creds (if used)
- API keys (if used)
- scheduler settings (if used)

## Data policies
### Retention
- Raw: ____ days
- Artifacts (Parquet): ____ versions
- Logs: ____ days

### Privacy / secrets
- Never commit secrets to git
- Sanitize logs (no tokens / personal identifiers)

## Debug playbook
### If ingestion fails
- Check network/credentials
- Check rate limits
- Save the raw response for fixtures

### If dbt tests fail
- Identify failing test + model
- Check grain and key uniqueness
- Confirm freshness/window assumptions

### If scheduled run “succeeds” but data is stale
- Confirm the schedule actually triggered
- Confirm raw ingest wrote new objects
- Confirm freshness checks are enabled

## Recovery drill (G6)
Document a known “break” and the steps to recover:
- break:
- detection:
- fix:
- prevention:
