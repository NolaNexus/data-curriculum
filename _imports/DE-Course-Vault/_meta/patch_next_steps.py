#!/usr/bin/env python3
"""Patch the vault to reduce overwhelm and fix link rot.

What it does (idempotent-ish):
- Fixes old internal links (13_Gates -> 14_Gates, 10_Logbook -> 11_Logbook)
- Adds/updates 'Next up' sections in module indexes
- Creates missing root 00_Index.md files for Cloud Track and Gates
- Ensures Labs contain Success criteria + Evidence headings (adds if missing)
- Adds lightweight READMEs clarifying Assessments vs Gates

Run from anywhere:
  python3 _meta/patch_next_steps.py /path/to/DE-Course-Vault_REBUILD

Safe defaults:
- Makes a timestamped backup of any file it changes under _meta/_patch_backups/
"""

from __future__ import annotations

import re
import shutil
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


@dataclass
class Change:
    path: Path
    before: str
    after: str


def backup_file(src: Path, backup_root: Path) -> None:
    backup_root.mkdir(parents=True, exist_ok=True)
    dst = backup_root / src.relative_to(vault_root)
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def write_if_changed(path: Path, new_text: str, changes: list[Change]) -> None:
    old_text = path.read_text(encoding="utf-8")
    if old_text == new_text:
        return
    changes.append(Change(path=path, before=old_text, after=new_text))


def apply_replacements(text: str) -> str:
    # Internal link path fixes
    text = text.replace("[[13_Gates/", "[[14_Gates/")
    text = text.replace("FROM \"13_Gates", "FROM \"14_Gates")

    text = text.replace("13_Gates/", "14_Gates/")

    text = text.replace("[[10_Logbook", "[[11_Logbook")
    text = text.replace("FROM \"10_Logbook", "FROM \"11_Logbook")
    text = text.replace("10_Logbook/", "11_Logbook/")
    # Capstone folder renumbering
    text = text.replace("[[07_Capstone", "[[08_Capstone")
    text = text.replace("FROM \"07_Capstone", "FROM \"08_Capstone")
    text = text.replace("07_Capstone/", "08_Capstone/")

    # Troubleshooting folder renumbering
    text = text.replace("[[11_Troubleshooting", "[[12_Troubleshooting")
    text = text.replace("FROM \"11_Troubleshooting", "FROM \"12_Troubleshooting")
    text = text.replace("11_Troubleshooting/", "12_Troubleshooting/")


    # Some files used 13_Gates without wiki brackets in bullet paths
    return text


def ensure_next_up(index_path: Path, module_slug: str, module_title: str, primary_gate: str | None) -> None:
    """Insert/replace a standardized Next up block right after the Outcome section."""
    txt = index_path.read_text(encoding="utf-8")

    # Build the block
    gate_line = f"- **Gate:** {primary_gate}\n" if primary_gate else ""
    next_block = (
        "## Next up (do this next)\n"
        "- [ ] Read the next lesson in **Ordered path**\n"
        "- [ ] Do the first relevant **Lab** and capture evidence\n"
        "- [ ] Write a quick log entry in [[11_Logbook/README|Logbook]] (what worked, what broke, what you learned)\n"
        f"{gate_line}"
        "\n"
        "### Definition of done\n"
        "You are done with this module when you can **run the system**, show **evidence**, and pass its gate(s).\n"
    )

    # Where to place: after the first "## Outcome" block (keep existing outcome text)
    # If Next up already exists, replace that section.
    if "## Next up (do this next)" in txt:
        # Replace existing Next up section up to the next H2
        pattern = re.compile(r"## Next up \(do this next\)[\s\S]*?(?=\n## |\Z)")
        txt2 = pattern.sub(next_block.rstrip() + "\n\n", txt)
    else:
        # Insert after Outcome section (Outcome header + its paragraph(s))
        # Find first occurrence of "## Outcome" and insert after its content until next H2.
        m = re.search(r"## Outcome\n([\s\S]*?)(?=\n## |\Z)", txt)
        if not m:
            # No outcome; insert after title
            m2 = re.search(r"^# .+\n\n", txt, flags=re.M)
            if m2:
                insert_at = m2.end()
                txt2 = txt[:insert_at] + next_block + "\n" + txt[insert_at:]
            else:
                txt2 = next_block + "\n" + txt
        else:
            insert_at = m.end()
            txt2 = txt[:insert_at] + "\n\n" + next_block + "\n" + txt[insert_at:]

    index_path.write_text(txt2, encoding="utf-8")


def ensure_root_index(dir_path: Path, title: str, links: list[str]) -> None:
    idx = dir_path / "00_Index.md"
    if idx.exists():
        return
    frontmatter = "---\ntype: index\ncreated: 2026-01-19\ntags: [course/index]\n---\n\n"
    body = [f"# {title}", "", "## Start here", *[f"- {l}" for l in links], ""]
    idx.write_text(frontmatter + "\n".join(body) + "\n", encoding="utf-8")


def ensure_lab_sections(lab_path: Path) -> None:
    txt = lab_path.read_text(encoding="utf-8")

    # Normalize headings (case-insensitive)
    def has_heading(name: str) -> bool:
        return re.search(rf"^#{{1,6}}\s+{re.escape(name)}\b", txt, flags=re.I | re.M) is not None

    # Ensure Success criteria section exists
    if not has_heading("Success criteria"):
        # Add near end, before Evidence if present else at end
        if re.search(r"^#{{1,6}}\s+Evidence\b", txt, flags=re.I | re.M):
            txt = re.sub(
                r"(^#{{1,6}}\s+Evidence\b)",
                "# Success criteria\n- [ ] (define a testable outcome)\n- [ ] (define a reproducible run command)\n\n\\1",
                txt,
                flags=re.I | re.M,
            )
        else:
            txt += "\n\n# Success criteria\n- [ ] (define a testable outcome)\n- [ ] (define a reproducible run command)\n"

    # Ensure Evidence section exists
    if not has_heading("Evidence"):
        txt += "\n\n# Evidence\n```text\n(paste command output, screenshots filenames, links, or notes)\n```\n"

    # Ensure Reflection section exists (tiny)
    if not has_heading("Reflection"):
        txt += "\n\n# Reflection\n- What was the sharp edge?\n- What would you do differently next time?\n"

    lab_path.write_text(txt.rstrip() + "\n", encoding="utf-8")


def ensure_assessments_readme(vault_root: Path) -> None:
    p = vault_root / "13_Assessments" / "README.md"
    if p.exists():
        return
    p.write_text(
        """---
created: 2026-01-19
type: guide
tags: [course/assessment]
---

# Assessments — how to use these

Assessments are **knowledge checks**. They answer: *Do you understand the ideas and vocabulary?*

- They are short.
- You can pass them with notes open.
- If you fail, you don’t ‘restart’ — you pick 1–2 weak spots and loop back.

## How this differs from Gates
Gates are **working-system proofs**. They answer: *Can you run the thing end-to-end and show evidence?*

Use Assessments to find what to study. Use Gates to prove you can build and operate it.
""",
        encoding="utf-8",
    )


def ensure_gates_readme(vault_root: Path) -> None:
    p = vault_root / "14_Gates" / "README.md"
    if p.exists():
        return
    p.write_text(
        """---
created: 2026-01-19
type: guide
tags: [course/gates]
---

# Gates — how to use these

A gate is a **boss fight** for a phase: you pass it by producing a working system and **evidence**.

## Rules
- Evidence lives in `14_Gates/Evidence/` and/or `11_Logbook/Gate_Runs/`.
- A gate is not ‘done’ until it’s reproducible on a fresh run.

## Recommended cadence
- Finish a module → attempt the aligned gate within 24–72 hours.
- If you fail: capture the failure, patch one thing, rerun.
""",
        encoding="utf-8",
    )


def main(vault_root_in: str) -> int:
    global vault_root
    vault_root = Path(vault_root_in).resolve()
    if not vault_root.exists():
        print(f"Vault root not found: {vault_root}")
        return 2

    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_root = vault_root / "_meta" / "_patch_backups" / ts

    changes: list[Change] = []

    # 1) Link replacements across all markdown files (except backups)
    md_files = [p for p in vault_root.rglob("*.md") if "_patch_backups" not in str(p)]
    for p in md_files:
        old = p.read_text(encoding="utf-8")
        new = apply_replacements(old)
        if new != old:
            backup_file(p, backup_root)
            p.write_text(new, encoding="utf-8")

    # 2) Ensure module "Next up" blocks
    module_indexes = [
        (vault_root / "02_Foundations" / "00_Index.md", "Foundations", "[[14_Gates/Gates/G0_Repo_Bootstrap]]"),
        (vault_root / "03_Data_Engineering_Core" / "00_Index.md", "Data Engineering Core", "[[14_Gates/Gates/G1_Raw_Immutability_Plus_Provenance]]"),
        (vault_root / "04_Analytics_Core" / "00_Index.md", "Analytics Core", "[[14_Gates/Gates/G5_Publish_Plus_Metrics_Plus_Dashboard]]"),
        (vault_root / "05_Data_Science_Optional" / "00_Index.md", "Data Science (Optional)", None),
        (vault_root / "06_Data_Product_Shipping" / "00_Index.md", "Data Product Shipping", "[[14_Gates/Gates/G5_Publish_Plus_Metrics_Plus_Dashboard]]"),
        (vault_root / "07_Cloud_Track" / "_indexes" / "00_Cloud_Track_Index.md", "Cloud Track", None),
        (vault_root / "08_Capstone" / "00_Index.md", "Capstone", "[[14_Gates/Gates/G8_Capstone_Demo]]"),
    ]
    for idx, title, gate in module_indexes:
        if idx.exists():
            backup_file(idx, backup_root)
            ensure_next_up(idx, title, title, gate)

    # 3) Create missing root indexes
    ensure_root_index(vault_root / "07_Cloud_Track", "Cloud Track", ["[[07_Cloud_Track/_indexes/00_Cloud_Track_Index|Cloud Track Index]]"])
    ensure_root_index(vault_root / "14_Gates", "Gates", ["[[14_Gates/_indexes/00_Gates_Index|Gates Index]]", "[[14_Gates/Dashboards/00_Gates_Dashboard|Gates Dashboard]]", "[[14_Gates/Evidence/00_Evidence_Index|Evidence Index]]"])

    # 4) Labs template enforcement
    for lab in (vault_root.rglob("Labs/*.md")):
        backup_file(lab, backup_root)
        ensure_lab_sections(lab)

    # 5) Clarifying READMEs
    ensure_assessments_readme(vault_root)
    ensure_gates_readme(vault_root)

    print(f"Patch applied. Backups saved to: {backup_root}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 _meta/patch_next_steps.py /path/to/vault")
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1]))
