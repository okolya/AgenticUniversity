#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
UNIVERSITY_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
WORKSPACE_ROOT="$(cd "$UNIVERSITY_ROOT/.." && pwd)"
SOURCE_FILE="$UNIVERSITY_ROOT/agent-runtime/adapters/codex/config.toml"
CODEX_CONFIG_ROOT="${CODEX_HOME:-${HOME}/.codex}"
TARGET_FILE="$CODEX_CONFIG_ROOT/config.toml"
BEGIN_MARKER="# BEGIN Agentic University project overlay: $UNIVERSITY_ROOT"
END_MARKER="# END Agentic University project overlay: $UNIVERSITY_ROOT"

[ -f "$SOURCE_FILE" ] || { echo "✗ missing source file: $SOURCE_FILE" >&2; exit 1; }
mkdir -p "$CODEX_CONFIG_ROOT"
if [ -L "$TARGET_FILE" ]; then
  echo "✗ refusing to update symlinked Codex config: $TARGET_FILE" >&2
  exit 1
fi
if [ -e "$TARGET_FILE" ] && [ ! -f "$TARGET_FILE" ]; then
  echo "✗ refusing to update non-regular Codex config: $TARGET_FILE" >&2
  exit 1
fi
touch "$TARGET_FILE"

python3 - "$TARGET_FILE" "$SOURCE_FILE" "$WORKSPACE_ROOT" "$UNIVERSITY_ROOT" "$BEGIN_MARKER" "$END_MARKER" <<'PY'
import sys
from pathlib import Path

target_path, source_path, workspace_root, university_root = map(Path, sys.argv[1:5])
begin_marker, end_marker = sys.argv[5:7]

def substitute(text: str) -> str:
    return (text.replace("{{WORKSPACE_ROOT}}", str(workspace_root))
                .replace("{{UNIVERSITY_ROOT}}", str(university_root)))

def strip_overlay(lines: list[str]) -> list[str]:
    result = []
    inside = False
    for line in lines:
        if line == begin_marker:
            inside = True
            continue
        if line == end_marker:
            inside = False
            continue
        if not inside:
            result.append(line)
    return result

existing = strip_overlay(target_path.read_text(encoding="utf-8").splitlines())
source = substitute(source_path.read_text(encoding="utf-8")).splitlines()
existing_tables = {
    line.strip()
    for line in existing
    if line.strip().startswith("[") and line.strip().endswith("]")
}
filtered_source = []
skip_table = False
for line in source:
    stripped = line.strip()
    if stripped.startswith("[") and stripped.endswith("]"):
        skip_table = stripped in existing_tables
    if skip_table:
        if not stripped:
            skip_table = False
        continue
    filtered_source.append(line)

merged = existing[:]
if merged and merged[-1].strip():
    merged.append("")
merged.append(begin_marker)
merged.extend(filtered_source)
merged.append(end_marker)
target_path.write_text("\n".join(merged).rstrip("\n") + "\n", encoding="utf-8")
PY

printf '✓ Agentic University Codex overlay installed in %s\n' "$TARGET_FILE"
