#!/usr/bin/env node
/**
 * Import Obsidian-style vault markdown into Docusaurus docs, safely.
 *
 * - Reads *.md, *.mdx under --src
 * - Writes to --out (default: docs/_imported_vault)
 * - Converts Obsidian [[links|alias]] -> alias (or basename)
 * - Ensures front matter includes id + title
 * - Converts type: lab -> type: lesson + kind: lab (so your index generator can include them)
 *
 * Usage:
 *   node scripts/import-vault.mjs --src _imports/DE-Course-Vault --out docs/_imported_vault
 */

import fs from "node:fs";
import path from "node:path";
import process from "node:process";

import fg from "fast-glob";
import matter from "gray-matter";

function arg(name, fallback = null) {
  const i = process.argv.indexOf(name);
  if (i === -1) return fallback;
  return process.argv[i + 1] ?? fallback;
}

const SRC = path.resolve(arg("--src", "_imports/DE-Course-Vault"));
const OUT = path.resolve(arg("--out", "docs/_imported_vault"));

const IGNORE_DIRS = new Set([
  ".obsidian",
  "_meta",
  "_vault_audit",
]);

const TOPLEVEL_MAP = {
  "00_START_HERE": "handbook/start-here",
  "01_Syllabus": "handbook/syllabus",
  "02_Foundations": "lessons/foundations",
  "03_Data_Engineering_Core": "lessons/data-engineering",
  "04_Analytics_Core": "lessons/analytics",
  "05_Data_Science_Optional": "lessons/data-science",
  "06_Data_Product_Shipping": "lessons/shipping",
  "07_Cloud_Track": "tracks/cloud",
  "08_Capstone": "tracks/capstone",
  "09_Resources_Library": "resources",
  "10_Templates": "handbook/templates",
  "11_Logbook": "handbook/logbook",
  "12_Troubleshooting": "handbook/troubleshooting",
  "13_Assessments": "assessments",
  "14_Gates": "gates",
  "99_Glossary": "glossary",
};

function ensureDir(p) {
  fs.mkdirSync(p, { recursive: true });
}

function slugify(s) {
  return String(s)
    .trim()
    .toLowerCase()
    .replace(/['"]/g, "")
    .replace(/[^a-z0-9]+/g, "_")
    .replace(/^_+|_+$/g, "")
    .slice(0, 80);
}

function firstH1(md) {
  const m = md.match(/^\s*#\s+(.+)\s*$/m);
  return m ? m[1].trim() : null;
}

function stripObsidianLinks(md) {
  // [[path|alias]] -> alias
  // [[path]] -> basename(path)
  return md.replace(/\[\[([^\]|]+)(\|([^\]]+))?\]\]/g, (_full, target, _pipeAlias, alias) => {
    if (alias && alias.trim()) return alias.trim();
    const base = String(target).split("/").pop();
    return base.replace(/\.md$/i, "").trim();
  });
}

function guessType(fm) {
  const t = String(fm?.type || "").trim().toLowerCase();
  if (!t) return null;
  if (t === "lab") return "lesson"; // normalize labs into lessons
  return t; // lesson, resource, gate, index, guide, etc.
}

function ensureIdAndTitle({ fm, content, fileStem }) {
  const title = fm.title || firstH1(content) || fileStem;

  // Prefix IDs so they don’t collide across types
  const type = guessType(fm) || "doc";
  const prefix =
    type === "lesson" ? "les" :
    type === "resource" ? "res" :
    type === "gate" ? "gate" :
    "doc";

  const id = fm.id || `${prefix}_${slugify(title)}`;

  return { id, title };
}

function shouldIgnore(relPath) {
  const parts = relPath.split(path.sep).filter(Boolean);
  if (parts.length === 0) return true;
  if (IGNORE_DIRS.has(parts[0])) return true;
  // Drop patch backups specifically
  if (parts.includes("_patch_backups")) return true;
  return false;
}

function main() {
  if (!fs.existsSync(SRC)) {
    console.error(`Source not found: ${SRC}`);
    process.exit(1);
  }

  ensureDir(OUT);

  const files = fg.sync(["**/*.md", "**/*.mdx"], {
    cwd: SRC,
    dot: false,
    onlyFiles: true,
  });

  let imported = 0;

  for (const rel of files) {
    if (shouldIgnore(rel)) continue;

    const abs = path.join(SRC, rel);
    const raw = fs.readFileSync(abs, "utf8");
    const parsed = matter(raw);

    const fm = parsed.data || {};
    let content = parsed.content || "";

    // Convert Obsidian links to non-link text to avoid broken-link build failures
    content = stripObsidianLinks(content);

    // Normalize lab -> lesson
    const originalType = String(fm.type || "").toLowerCase();
    if (originalType === "lab") {
      fm.type = "lesson";
      fm.kind = fm.kind || "lab";
    }

    // Resource normalization (optional but helpful)
    if (String(fm.type || "").toLowerCase() === "resource") {
      if (fm.format && !fm.kind) fm.kind = fm.format; // format -> kind
      if (fm.estimated_minutes && !fm.time_minutes) fm.time_minutes = fm.estimated_minutes;
    }

    // Lesson normalization
    if (String(fm.type || "").toLowerCase() === "lesson") {
      if (fm.timebox_minutes && !fm.estimated_time_minutes) {
        fm.estimated_time_minutes = fm.timebox_minutes;
      }
    }

    const fileStem = path.basename(rel).replace(/\.(md|mdx)$/i, "");
    const { id, title } = ensureIdAndTitle({ fm, content, fileStem });
    fm.id = id;
    fm.title = title;

    // Decide destination path based on top-level folder
    const top = rel.split(path.sep)[0];
    const mapped = TOPLEVEL_MAP[top] || `misc/${top}`;
    const subRel = rel.split(path.sep).slice(1).join(path.sep);

    const outDir = path.join(OUT, mapped, path.dirname(subRel));
    ensureDir(outDir);

    const outPath = path.join(outDir, path.basename(rel));

    // Recompose
    const out = matter.stringify(content, fm);
    fs.writeFileSync(outPath, out, "utf8");
    imported += 1;
  }

  console.log(`Imported ${imported} files into: ${OUT}`);
  console.log(`Next: add docs/_imported_vault to your sidebar (autogenerated will pick it up automatically).`);
}

main();
