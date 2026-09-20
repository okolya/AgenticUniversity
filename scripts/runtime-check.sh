#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
roles=(rector dean lecturer teacher laboratory-specialist learning-analyst examiner)
for role in "${roles[@]}"; do
  test -e ".claude/agents/university-$role.md"
  test -e ".codex/agents/university-$role.toml"
  test -e ".cursor/agents/university-$role.md"
done
for worker in petro bob luke; do test -f "university/workers/$worker/WORKER.md"; done
for f in .codex/agents/university-*.toml; do python3 - "$f" <<'PY'
import sys, tomllib
with open(sys.argv[1], 'rb') as h:
    d=tomllib.load(h)
for k in ('name','description','developer_instructions'):
    assert d.get(k), (sys.argv[1], k)
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
