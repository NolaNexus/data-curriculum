---
type: lesson
module: Foundations
timebox_minutes: 90
status: active
prereqs: []
tags: [course/lesson, topic/linux]
updated: 2026-01-18
---

# Linux + shell for data pipelines (the “operator” skill)

This is the skill that turns “I built it once” into “I can keep it running.”

## Minimum commands to be dangerous (in a good way)
- Navigation: `pwd`, `ls`, `cd`, `find`
- Text: `cat`, `less`, `head`, `tail -f`, `grep`
- Pipes: `|`, redirect `>`, `2>&1`
- Processes: `ps`, `top`, `kill`
- Services/logs: `systemctl`, `journalctl`
- Archives: `tar`, `gzip`, `zip`
- Networking sanity: `curl`, `nc` (optional)

## What you must be able to do
- Follow logs for a failing run
- Prove what changed between runs
- Find where a file came from and who wrote it
- Identify the process that’s eating CPU/RAM

## Practice focus
Do the lab: [[02_Foundations/Labs/02_Lab_Shell_And_Logs_Drill]]
