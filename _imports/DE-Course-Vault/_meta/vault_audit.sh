#!/usr/bin/env bash
set -euo pipefail

OUT_DIR="_vault_audit"
mkdir -p "$OUT_DIR"

REPORT_MD="$OUT_DIR/report.md"
REPORT_CSV="$OUT_DIR/folder_counts.csv"

echo "# Vault Audit Report" > "$REPORT_MD"
echo "" >> "$REPORT_MD"
echo "Generated: $(date -Is)" >> "$REPORT_MD"
echo "" >> "$REPORT_MD"

echo "## File counts by top-level folder" >> "$REPORT_MD"
echo "" >> "$REPORT_MD"

# CSV header
echo "folder,file_count" > "$REPORT_CSV"

for d in */ ; do
  # skip audit folder itself
  [[ "$d" == "${OUT_DIR}/" ]] && continue
  count=$(find "$d" -type f 2>/dev/null | wc -l | tr -d ' ')
  printf "%s,%s\n" "${d%/}" "$count" >> "$REPORT_CSV"
done

# Pretty-print top folders into md
sort -t, -k2,2nr "$REPORT_CSV" | head -n 20 | awk -F, '
BEGIN { print "| Folder | Files |"; print "|---|---:|"; }
NR>1 { printf "| %s | %s |\n", $1, $2 }
' >> "$REPORT_MD"

echo "" >> "$REPORT_MD"
echo "## Largest files (top 25)" >> "$REPORT_MD"
echo "" >> "$REPORT_MD"
echo "| Size (KB) | File |" >> "$REPORT_MD"
echo "|---:|---|" >> "$REPORT_MD"
find . -type f -not -path "./.obsidian/*" -printf '%s\t%p\n' \
  | sort -nr \
  | head -n 25 \
  | awk -F'\t' '{ printf "| %.1f | %s |\n", $1/1024, $2 }' >> "$REPORT_MD"

echo "" >> "$REPORT_MD"
echo "## Index folders (_indexes) inventory" >> "$REPORT_MD"
echo "" >> "$REPORT_MD"
find . -type d -name "_indexes" -print \
  | sed 's/^/- /' >> "$REPORT_MD"

echo "" >> "$REPORT_MD"
echo "## Notes without frontmatter (top 50)" >> "$REPORT_MD"
echo "" >> "$REPORT_MD"
# Frontmatter heuristic: file starts with ---
grep -RIl --include="*.md" . -e "" \
  | while read -r f; do
      first_line="$(head -n 1 "$f" 2>/dev/null || true)"
      if [[ "$first_line" != "---" ]]; then
        echo "$f"
      fi
    done \
  | head -n 50 \
  | sed 's/^/- /' >> "$REPORT_MD"

echo "" >> "$REPORT_MD"
echo "Saved report: $REPORT_MD"
echo "Saved csv:    $REPORT_CSV"
