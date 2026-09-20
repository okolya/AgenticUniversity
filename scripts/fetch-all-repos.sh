#!/usr/bin/env bash
# Fetch origin for every Project Template repository (root + components). Adapted
# from reference PHP workspace's scripts/fetch-all-repos.sh, without the parallel JOBS
# worker pool — Project Template has a handful of repos, not dozens of package
# submodules, so sequential fetch is fast enough and keeps output ordered.
# Does not checkout or merge.
#
# Usage:
#   ./scripts/fetch-all-repos.sh
#   make fetch-all

set -euo pipefail

UNIVERSITY_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ROOT="$(cd "$UNIVERSITY_ROOT/.." && pwd)"

echo "⬇️  git fetch origin (all repositories)"
echo ""

ok=0
failed=0
skipped=0

fetch_one() {
    local repo_display="$1" repo_path="$2"

    if [ ! -d "$repo_path/.git" ] && [ ! -f "$repo_path/.git" ]; then
        skipped=$((skipped + 1))
        return 0
    fi

    if (cd "$repo_path" && git fetch origin --prune --tags 2>&1); then
        ok=$((ok + 1))
    else
        echo "❌ $repo_display"
        failed=$((failed + 1))
    fi
}

fetch_one "(root)" "$ROOT"
while IFS= read -r path; do
    [ -d "$path/.git" ] || [ -f "$path/.git" ] || continue
    fetch_one "$(basename "$path")" "$path"
done < <(workspace_repo_paths)

echo ""
echo "✅ fetch done: ok=${ok} skipped=${skipped} failed=${failed}"
[ "$failed" -eq 0 ] || exit 1
exit 0
