#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/workspace-lib.sh"

echo "⬇️  git fetch origin (workspace repositories)"
echo ""
ok=0; failed=0; skipped=0
while IFS= read -r repo; do
  name="$(basename "$repo")"
  if ! git -C "$repo" remote get-url origin >/dev/null 2>&1; then
    echo "⚠️  $name has no origin; skipped"
    skipped=$((skipped + 1)); continue
  fi
  if git -C "$repo" fetch origin --prune --tags; then
    echo "✓ fetched $name"; ok=$((ok + 1))
  else
    echo "❌ $name" >&2; failed=$((failed + 1))
  fi
done < <(workspace_repo_paths)
echo ""
echo "fetch done: ok=$ok skipped=$skipped failed=$failed"
[ "$failed" -eq 0 ]
