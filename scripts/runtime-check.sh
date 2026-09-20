#!/usr/bin/env bash
set -euo pipefail
UNIVERSITY_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ROOT="$(cd "$UNIVERSITY_ROOT/.." && pwd)"
cd "$ROOT"
roles=(rector dean lecturer teacher laboratory-specialist learning-analyst examiner)

require_file() {
  if [[ ! -f "$1" ]]; then
    echo "Missing runtime file: $1" >&2
    exit 1
  fi
}

for role in "${roles[@]}"; do
  require_file ".claude/agents/university-$role.md"
  require_file ".codex/agents/university-$role.toml"
  require_file ".cursor/agents/university-$role.md"
done
for worker in petro bob luke; do
  require_file "$UNIVERSITY_ROOT/university/workers/$worker/WORKER.md"
done

for f in .codex/agents/university-*.toml; do python3 - "$f" <<'PY'
import re
import sys

path = sys.argv[1]
text = open(path, encoding="utf-8").read()

# Keep this check compatible with Python 3.10. The runtime check only needs to
# validate the adapter metadata and should not require tomllib/tomli to be
# installed just to inspect generated files.
fields = {
    "name": r'^\s*name\s*=\s*["\'][^"\'\n]+["\']\s*(?:#.*)?$',
    "description": r'^\s*description\s*=\s*["\'][^"\'\n]+["\']\s*(?:#.*)?$',
    "developer_instructions": r'(?s)^\s*developer_instructions\s*=\s*""".+?"""\s*(?:#.*)?$',
}

for field, pattern in fields.items():
    if not re.search(pattern, text, re.MULTILINE):
        print(f"{path}: missing or empty TOML field '{field}'", file=sys.stderr)
        raise SystemExit(1)
PY
done
# No worker-specific runtime agents.
for worker in petro bob luke; do
  ! find .claude/agents .codex/agents .cursor/agents -maxdepth 1 -iname "*${worker}*" | grep -q .
done
# No broken symlinks under runtime dirs.
if find .agents .claude .codex .cursor -xtype l -print | grep -q .; then
  echo "Broken runtime symlink(s) found" >&2
  find .agents .claude .codex .cursor -xtype l -print >&2
  exit 1
fi
echo "Agent runtime triad OK"
