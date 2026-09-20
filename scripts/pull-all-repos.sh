#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/workspace-lib.sh"
while IFS= read -r repo; do
  name="$(basename "$repo")"
  if [ -n "$(git -C "$repo" status --porcelain)" ]; then
    echo "❌ $name has uncommitted changes; refusing pull" >&2; exit 1
  fi
  if git -C "$repo" remote get-url origin >/dev/null 2>&1; then
    git -C "$repo" pull --ff-only
    echo "⬇️  pulled $name"
  else
    echo "⚠️  $name has no origin; skipped"
  fi
done < <(workspace_repo_paths)
