#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
# These directories are generated integration state in this standalone repository.
# Refuse to remove them if they contain non-symlink foreign files outside the University namespace.
for dir in .agents .claude .codex .cursor; do
  path="$ROOT/$dir"
  [ -e "$path" ] || continue
  foreign="$(find "$path" -type f ! -path '*/university/*' ! -name 'university-*' 2>/dev/null | head -1 || true)"
  if [ -n "$foreign" ]; then
    echo "✗ refusing to remove $dir; foreign file found: $foreign" >&2
    exit 1
  fi
done
rm -rf "$ROOT/.agents" "$ROOT/.claude" "$ROOT/.codex" "$ROOT/.cursor"
echo "✅ Generated University runtime state removed"
