#!/usr/bin/env python3
"""
Create a curated resource library inside your DE-Course-Vault.

Where to run:
- Put this file in the ROOT of your vault, then:
  python3 create_resources_pack_v2.py
"""
from __future__ import annotations

import json
import datetime as dt
from pathlib import Path

ROOT = Path(".").resolve()
CURATED = ROOT / "08_Resources_Library" / "Curated"
CARDS = CURATED / "Resource_Cards"
INDEXES = CURATED / "_Indexes"

RESOURCES = [
    # Foundations
    {
        "slug": "sqlbolt",
        "title": "SQLBolt: Interactive SQL Lessons",
        "url": "https://sqlbolt.com/",
        "phase": "00_Foundations",
        "topics": ["SQL", "joins", "basics"],
        "format": "interactive",
        "est_time": "2–6h",
        "why": "Fast reps; low setup; great daily practice.",
    },
    {
        "slug": "mode_sql_tutorial",
        "title": "Mode: SQL Tutorial (Querying and analysis patterns)",
        "url": "https://mode.com/sql-tutorial/sql-in-mode/index.html",
        "phase": "00_Foundations",
        "topics": ["SQL", "analysis"],
        "format": "tutorial",
        "est_time": "4–8h",
        "why": "Analysis mindset + real patterns.",
    },
    {
        "slug": "mode_window_functions",
        "title": "Mode: Window Functions (concept + examples)",
        "url": "https://mode.com/blog/bridge-the-gap-window-functions/",
        "phase": "00_Foundations",
        "topics": ["SQL", "window functions"],
        "format": "article",
        "est_time": "30–60m",
        "why": "Window functions are a DE superpower.",
    },

    # DE Core
    {
        "slug": "prefect_quickstart",
        "title": "Prefect Docs: Quickstart",
        "url": "https://docs.prefect.io/v3/get-started/quickstart",
        "phase": "01_Data_Engineering_Core",
        "topics": ["orchestration", "prefect"],
        "format": "docs",
        "est_time": "30–90m",
        "why": "Turn Python into scheduled workflows quickly.",
    },
    {
        "slug": "dagster_quickstart",
        "title": "Dagster Docs: Quickstart",
        "url": "https://docs.dagster.io/getting-started/quickstart",
        "phase": "01_Data_Engineering_Core",
        "topics": ["orchestration", "dagster"],
        "format": "docs",
        "est_time": "45–120m",
        "why": "Modern orchestration + asset thinking.",
    },
    {
        "slug": "great_expectations_home",
        "title": "Great Expectations Docs: Home / Get started",
        "url": "https://docs.greatexpectations.io/docs/home/",
        "phase": "01_Data_Engineering_Core",
        "topics": ["data quality", "validation"],
        "format": "docs",
        "est_time": "45–120m",
        "why": "Powerful data contracts when dbt tests aren’t enough.",
    },
    {
        "slug": "scrapy_tutorial",
        "title": "Scrapy Docs: Tutorial",
        "url": "https://docs.scrapy.org/en/latest/intro/tutorial.html",
        "phase": "01_Data_Engineering_Core",
        "topics": ["scraping", "scrapy"],
        "format": "docs",
        "est_time": "1–3h",
        "why": "Industrial scraping patterns.",
    },
    {
        "slug": "nyc_open_data_howto",
        "title": "NYC Open Data: How to use Socrata APIs (SoQL)",
        "url": "https://opendata.cityofnewyork.us/how-to/",
        "phase": "01_Data_Engineering_Core",
        "topics": ["datasets", "api", "open data"],
        "format": "docs",
        "est_time": "20–60m",
        "why": "A realistic API for ingestion + modeling practice.",
    },

    # Analytics
    {
        "slug": "metabase_dashboards",
        "title": "Metabase Docs: Introduction to dashboards",
        "url": "https://www.metabase.com/docs/latest/dashboards/introduction",
        "phase": "02_Analytics_Core",
        "topics": ["BI", "dashboards", "metabase"],
        "format": "docs",
        "est_time": "30–60m",
        "why": "Fast path from tables to decisions.",
    },

    # DS
    {
        "slug": "sklearn_getting_started",
        "title": "scikit-learn: Getting Started",
        "url": "https://scikit-learn.org/stable/getting_started.html",
        "phase": "03_Data_Science_Core",
        "topics": ["ml", "baselines", "evaluation"],
        "format": "docs",
        "est_time": "1–3h",
        "why": "Practical ML basics with evaluation guidance.",
    },

    # Product
    {
        "slug": "fastapi_tutorial",
        "title": "FastAPI Tutorial",
        "url": "https://fastapi.tiangolo.com/tutorial/",
        "phase": "04_Data_Product_Layer",
        "topics": ["api", "fastapi"],
        "format": "docs",
        "est_time": "2–6h",
        "why": "Clean API serving if you need programmatic access.",
    },

    # Cloud
    {
        "slug": "google_cloud_well_architected",
        "title": "Google Cloud Well-Architected Framework",
        "url": "https://docs.cloud.google.com/architecture/framework",
        "phase": "07_Cloud_Track",
        "topics": ["cloud", "architecture", "cost"],
        "format": "docs",
        "est_time": "1–3h",
        "why": "Security/cost/reliability guardrails.",
    },
    {
        "slug": "opentofu_intro",
        "title": "OpenTofu Docs: Getting started",
        "url": "https://opentofu.org/docs/intro/",
        "phase": "07_Cloud_Track",
        "topics": ["iac", "opentofu"],
        "format": "docs",
        "est_time": "45–120m",
        "why": "Infrastructure as code for reproducible deploys.",
    },
]

def ensure_dirs() -> None:
    CARDS.mkdir(parents=True, exist_ok=True)
    INDEXES.mkdir(parents=True, exist_ok=True)

def write_card(r: dict) -> None:
    today = dt.date.today().isoformat()
    front = {
        "type": "resource",
        "status": "unread",
        "phase": r["phase"],
        "topics": r["topics"],
        "format": r["format"],
        "est_time": r["est_time"],
        "added": today,
        "url": r["url"],
    }
    fm = "---\n" + "\n".join(
        f"{k}: {json.dumps(v) if isinstance(v, (list, dict)) else v}"
        for k, v in front.items()
    ) + "\n---\n"

    body = f"""# {r['title']}

- **URL:** {r['url']}
- **Phase:** `{r['phase']}`
- **Topics:** {", ".join(f"`{t}`" for t in r["topics"])}
- **Format:** `{r['format']}` | **Estimated time:** {r['est_time']}

## Why this matters
{r['why']}

## What to do with it (suggested)
- Skim → do a tiny output → write a short reflection.
- Link evidence: commit, notebook, dbt run, dashboard screenshot, etc.
"""
    (CARDS / f"{r['slug']}.md").write_text(fm + body, encoding="utf-8")

def write_index(title: str, phase: str, filename: str) -> None:
    items = [r for r in RESOURCES if r["phase"] == phase]
    lines = [f"# {title}\n", "## Resources\n"]
    for r in items:
        lines.append(f"- [[../Resource_Cards/{r['slug']}|{r['title']}]] — *{r['format']}* ({r['est_time']})")
    (INDEXES / filename).write_text("\n".join(lines) + "\n", encoding="utf-8")

def main() -> None:
    ensure_dirs()
    for r in RESOURCES:
        write_card(r)

    # Home + phase indexes
    home = """# Curated Resources

Start with the index for your current phase.

## Phase indexes
- [[00_Foundations_Index]]
- [[01_Data_Engineering_Core_Index]]
- [[02_Analytics_Core_Index]]
- [[03_Data_Science_Core_Index]]
- [[04_Data_Product_Layer_Index]]
- [[07_Cloud_Track_Index]]
"""
    (INDEXES / "00_Curated_Resources_Home.md").write_text(home + "\n", encoding="utf-8")

    write_index("Foundations", "00_Foundations", "00_Foundations_Index.md")
    write_index("Data Engineering Core", "01_Data_Engineering_Core", "01_Data_Engineering_Core_Index.md")
    write_index("Analytics Core", "02_Analytics_Core", "02_Analytics_Core_Index.md")
    write_index("Data Science Core", "03_Data_Science_Core", "03_Data_Science_Core_Index.md")
    write_index("Data Product Layer", "04_Data_Product_Layer", "04_Data_Product_Layer_Index.md")
    write_index("Cloud Track", "07_Cloud_Track", "07_Cloud_Track_Index.md")

    print(f"Done. Created: {CURATED}")

if __name__ == "__main__":
    main()
