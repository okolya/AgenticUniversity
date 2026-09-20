#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/workspace-lib.sh"

while IFS= read -r repo; do
  name="$(basename "$repo")"
  git -C "$repo" remote get-url origin >/dev/null 2>&1 || { echo "⚠️  $name has no origin; skipped"; continue; }
  [ -z "$(git -C "$repo" status --porcelain)" ] || { echo "⚠️  $name has uncommitted changes; skipped"; continue; }
  git -C "$repo" rev-parse --verify HEAD >/dev/null 2>&1 || { echo "⚠️  $name has no commits; skipped"; continue; }
  branch="$(git -C "$repo" branch --show-current)"
  [ -n "$branch" ] || { echo "⚠️  $name is detached; skipped"; continue; }
  if git -C "$repo" rev-parse --abbrev-ref --symbolic-full-name '@{u}' >/dev/null 2>&1; then
    ahead="$(git -C "$repo" rev-list --count '@{u}..HEAD')"
    [ "$ahead" -gt 0 ] || continue
    git -C "$repo" push
  else
    git -C "$repo" push --set-upstream origin "$branch"
  fi
  echo "🚀 pushed $name"
done < <(workspace_repo_paths)
echo "✅ push-ready complete"
