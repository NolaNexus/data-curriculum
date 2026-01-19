#!/usr/bin/env node
/* Curriculum index generator for Docusaurus (front matter -> docs/indexes/_generated). */


import fs from "node:fs";
import path from "node:path";
import process from "node:process";

import fg from "fast-glob";
import matter from "gray-matter";
import YAML from "yaml";

const REPO_ROOT = process.cwd();
const DOCS_DIR = path.join(REPO_ROOT, "docs");
const OUT_DIR = path.join(DOCS_DIR, "indexes", "_generated");
const PROGRESS_PATH = path.join(REPO_ROOT, "data", "progress.yaml");

function ensureDir(p) {
  fs.mkdirSync(p, { recursive: true });
}

function readYamlIfExists(p, fallbackObj) {
  if (!fs.existsSync(p)) return fallbackObj;
  const raw = fs.readFileSync(p, "utf8");
  try {
    return YAML.parse(raw) ?? fallbackObj;
  } catch (e) {
    console.error(`Failed to parse YAML: ${p}`);
    throw e;
  }
}

function writeDoc(outPath, { id, title, body }) {
  const front = `---\nid: ${id}\ntitle: ${title}\n---\n\n`;
  fs.writeFileSync(outPath, front + body.trimStart(), "utf8");
}

function normSlashes(p) {
  return p.split(path.sep).join("/");
}

function relLink(fromDir, toFile) {
  // Docusaurus Markdown links work great with relative paths.
  // fromDir and toFile are absolute paths.
  const rel = path.relative(fromDir, toFile);
  return normSlashes(rel);
}

function safeArray(x) {
  return Array.isArray(x) ? x : [];
}

function summarizeMissing(prereqLessons, prereqGates, completedLessons, passedGates) {
  const missingLessons = prereqLessons.filter((id) => !completedLessons.has(id));
  const missingGates = prereqGates.filter((id) => !passedGates.has(id));
  return { missingLessons, missingGates };
}

function main() {
  // Guardrails
  if (!fs.existsSync(DOCS_DIR)) {
    console.error("No docs/ directory found. Run from repo root.");
    process.exit(1);
  }

  ensureDir(OUT_DIR);

  const progress = readYamlIfExists(PROGRESS_PATH, {
    passed_gates: [],
    completed_lessons: [],
  });

  const passedGates = new Set(safeArray(progress.passed_gates));
  const completedLessons = new Set(safeArray(progress.completed_lessons));

  // Scan docs (ignore generated output + node_modules)
  const patterns = [
    "docs/**/*.{md,mdx}",
    "!docs/indexes/_generated/**",
    "!**/node_modules/**",
  ];

  const files = fg.sync(patterns, { dot: false });

  /** @type {Array<{file:string, fm:any, content:string}>} */
  const parsed = [];

  for (const file of files) {
    const abs = path.join(REPO_ROOT, file);
    const raw = fs.readFileSync(abs, "utf8");
    const m = matter(raw);
    const fm = m.data || {};

    // Skip empty/non-typed docs (lets you keep regular pages)
    if (!fm.type) continue;

    // Track
    parsed.push({ file: abs, fm, content: m.content || "" });
  }

  const resources = [];
  const lessons = [];
  const gates = [];

  for (const p of parsed) {
    if (p.fm.type === "resource") resources.push(p);
    else if (p.fm.type === "lesson") lessons.push(p);
    else if (p.fm.type === "gate") gates.push(p);
  }

  // Build lookup maps by id (fallback to file-based id if missing)
  const byId = new Map();
  for (const item of [...resources, ...lessons, ...gates]) {
    const id = item.fm.id || normSlashes(path.relative(DOCS_DIR, item.file)).replace(/\.(md|mdx)$/i, "");
    byId.set(id, { ...item, derivedId: id });
  }

  // -----------------------------
  // Index 1: Gates not yet passed
  // -----------------------------
  {
    const rows = gates
      .map((g) => {
        const id = g.fm.id || g.derivedId;
        return {
          id,
          title: g.fm.title || id,
          file: g.file,
          passed: passedGates.has(id),
        };
      })
      .filter((g) => !g.passed)
      .sort((a, b) => a.title.localeCompare(b.title));

    const outPath = path.join(OUT_DIR, "gates-not-passed.md");

    const body =
      rows.length === 0
        ? `All gates are marked as passed (or you haven’t created any gates yet).\n`
        : [
            `These are gates you haven’t marked as passed in \`data/progress.yaml\`.`,
            ``,
            `| Gate | ID |`,
            `|---|---|`,
            ...rows.map((r) => {
              const link = relLink(path.dirname(outPath), r.file);
              return `| [${r.title}](${link}) | \`${r.id}\` |`;
            }),
            ``,
          ].join("\n");

    writeDoc(outPath, {
      id: "idx_gates_not_passed",
      title: "Gates not passed",
      body,
    });
  }

  // --------------------------------
  // Index 2: Resources by topic/tag
  // --------------------------------
  {
    // Group by "topic" if present, else fall back to tags (each tag acts like a topic bucket)
    /** @type {Map<string, Array<{id:string,title:string,file:string,topic?:string,tags:string[]}>>} */
    const buckets = new Map();

    for (const r of resources) {
      const id = r.fm.id || r.derivedId;
      const title = r.fm.title || id;
      const topic = (r.fm.topic || "").toString().trim().toLowerCase();
      const tags = safeArray(r.fm.tags).map((t) => String(t).toLowerCase());

      const entry = { id, title, file: r.file, topic, tags };

      if (topic) {
        if (!buckets.has(topic)) buckets.set(topic, []);
        buckets.get(topic).push(entry);
      } else if (tags.length) {
        for (const t of tags) {
          if (!buckets.has(t)) buckets.set(t, []);
          buckets.get(t).push(entry);
        }
      } else {
        if (!buckets.has("uncategorized")) buckets.set("uncategorized", []);
        buckets.get("uncategorized").push(entry);
      }
    }

    // Always make a SQL page if anything matches topic/tags "sql"
    const topics = [...buckets.keys()].sort((a, b) => a.localeCompare(b));

    // Master overview page
    const overviewPath = path.join(OUT_DIR, "resources-by-topic.md");
    const overviewLines = [];

    overviewLines.push(`This is generated from \`type: resource\` front matter.\n`);
    if (topics.length === 0) {
      overviewLines.push(`No resources found yet. Add some \`type: resource\` docs.\n`);
    } else {
      overviewLines.push(`## Topics\n`);
      for (const t of topics) {
        const pageName = `resources-${t.replace(/[^a-z0-9]+/g, "-")}.md`;
        overviewLines.push(`- [${t}](./${pageName}) (${buckets.get(t).length})`);
      }
      overviewLines.push("");
    }

    writeDoc(overviewPath, {
      id: "idx_resources_by_topic",
      title: "Resources by topic",
      body: overviewLines.join("\n"),
    });

    // Per-topic pages (including sql if present)
    for (const t of topics) {
      const entries = buckets
        .get(t)
        .slice()
        .sort((a, b) => a.title.localeCompare(b.title));

      const pageName = `resources-${t.replace(/[^a-z0-9]+/g, "-")}.md`;
      const outPath = path.join(OUT_DIR, pageName);

      const body = [
        `Generated from \`type: resource\` docs where \`topic: ${t}\` (or tag fallback).`,
        ``,
        `| Resource | ID |`,
        `|---|---|`,
        ...entries.map((e) => {
          const link = relLink(path.dirname(outPath), e.file);
          return `| [${e.title}](${link}) | \`${e.id}\` |`;
        }),
        ``,
      ].join("\n");

      writeDoc(outPath, {
        id: `idx_resources_${t.replace(/[^a-z0-9]+/g, "_")}`,
        title: `Resources: ${t}`,
        body,
      });
    }
  }

  // --------------------------------------
  // Index 3: Unlocked "next lessons" list
  // --------------------------------------
  {
    const outPath = path.join(OUT_DIR, "unlocked-next-lessons.md");

    // Consider a lesson unlocked if prereq lessons + gates are satisfied.
    const lessonRows = lessons.map((l) => {
      const id = l.fm.id || l.derivedId;
      const title = l.fm.title || id;

      const prereqLessons = safeArray(l.fm?.prerequisites?.lessons);
      const prereqGates = safeArray(l.fm?.prerequisites?.gates);

      const { missingLessons, missingGates } = summarizeMissing(
        prereqLessons,
        prereqGates,
        completedLessons,
        passedGates
      );

      const completed = completedLessons.has(id);
      const unlocked = !completed && missingLessons.length === 0 && missingGates.length === 0;

      return {
        id,
        title,
        file: l.file,
        level: (l.fm.level || "").toString(),
        time: Number(l.fm.estimated_time_minutes || 0),
        unlocked,
        completed,
        missingLessons,
        missingGates,
      };
    });

    const unlocked = lessonRows
      .filter((r) => r.unlocked)
      .sort((a, b) => (a.level || "").localeCompare(b.level || "") || a.title.localeCompare(b.title));

    const locked = lessonRows
      .filter((r) => !r.unlocked && !r.completed)
      .sort((a, b) => (a.missingGates.length + a.missingLessons.length) - (b.missingGates.length + b.missingLessons.length));

    const bodyLines = [];
    bodyLines.push(`This is generated from \`type: lesson\` docs + your \`data/progress.yaml\`.\n`);

    bodyLines.push(`## Unlocked next lessons\n`);
    if (unlocked.length === 0) {
      bodyLines.push(`No unlocked lessons yet. Either:\n`);
      bodyLines.push(`- you haven’t added lessons, or`);
      bodyLines.push(`- your lessons require gates/lessons not marked completed/passed.\n`);
    } else {
      bodyLines.push(`| Lesson | Level | Est. min | ID |`);
      bodyLines.push(`|---|---:|---:|---|`);
      for (const r of unlocked) {
        const link = relLink(path.dirname(outPath), r.file);
        bodyLines.push(`| [${r.title}](${link}) | ${r.level || ""} | ${r.time || ""} | \`${r.id}\` |`);
      }
      bodyLines.push("");
    }

    // Helpful: show the “closest locked” items with missing prereqs
    bodyLines.push(`## Closest locked lessons (what’s blocking them)\n`);
    if (locked.length === 0) {
      bodyLines.push(`Nothing is locked (or everything is completed).\n`);
    } else {
      const top = locked.slice(0, 15);
      bodyLines.push(`| Lesson | Missing gates | Missing lessons |`);
      bodyLines.push(`|---|---|---|`);
      for (const r of top) {
        const link = relLink(path.dirname(outPath), r.file);
        const mg = r.missingGates.map((x) => `\`${x}\``).join(", ");
        const ml = r.missingLessons.map((x) => `\`${x}\``).join(", ");
        bodyLines.push(`| [${r.title}](${link}) | ${mg || "—"} | ${ml || "—"} |`);
      }
      bodyLines.push("");
    }

    writeDoc(outPath, {
      id: "idx_unlocked_next_lessons",
      title: "Unlocked next lessons",
      body: bodyLines.join("\n"),
    });
  }

  console.log(`Generated indexes into: ${path.relative(REPO_ROOT, OUT_DIR)}`);
  console.log(`- docs/indexes/_generated/gates-not-passed.md`);
  console.log(`- docs/indexes/_generated/resources-by-topic.md (+ per-topic pages)`);
  console.log(`- docs/indexes/_generated/unlocked-next-lessons.md`);
}

main();
