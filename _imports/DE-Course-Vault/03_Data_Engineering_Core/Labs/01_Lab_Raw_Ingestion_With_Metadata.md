---
type: lab
module: DE Core
timebox_minutes: 120
status: planned
created: 2026-01-19
tags: [course/lab, topic/ingestion]
---

# Lab objective
Ingest one source into immutable raw storage + metadata.

# Steps
1. Pick a source (file/API/HTML scrape/logs).
2. Save raw payload to `data/raw/<source>/<yyyy-mm-dd>/...`
3. Write metadata: checksum + fetched_at + run_id.
4. Prove rerunning does not overwrite prior raw.

# Success criteria
- [ ] Raw files are immutable
- [ ] Metadata answers “what/when/where”


# Evidence
```text
(paste command output, screenshots filenames, links, or notes)
```


# Reflection
- What was the sharp edge?
- What would you do differently next time?
