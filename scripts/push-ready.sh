#!/usr/bin/env bash
# Push every component repo (and root) that is already committed and ahead
# of origin — no commit logic, just push. Use after committing by hand in
# individual repos, when commit-all's commit step is not wanted.

set -euo pipefail

UNIVERSITY_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ROOT="$(cd "$UNIVERSITY_ROOT/.." && pwd)"

remote_push_available() {
    local remote_url host
    remote_url="$(git remote get-url origin 2>/dev/null || true)"
    [ -n "$remote_url" ] || return 1
    case "$remote_url" in
        git@*:*) host="${remote_url#git@}"; host="${host%%:*}" ;;
        ssh://*) host="${remote_url#ssh://}"; host="${host%%/*}"; host="${host%%:*}" ;;
        http://*|https://*) host="${remote_url#*://}"; host="${host%%/*}"; host="${host%%:*}" ;;
        *) return 0 ;;
    esac
    command -v getent >/dev/null 2>&1 || return 0
    getent hosts "$host" >/dev/null 2>&1
}

push_repo() {
    local repo_name="$1" repo_path="$2"
    [ -d "$repo_path/.git" ] || [ -f "$repo_path/.git" ] || return 0

    cd "$repo_path"
    local ahead
    ahead="$(git rev-list --count '@{u}..HEAD' 2>/dev/null || echo 0)"
    if [ "$ahead" -eq 0 ]; then
        cd "$ROOT"
        return 0
    fi

    if [ -n "$(git status --porcelain)" ]; then
        echo "⚠️  $repo_name has uncommitted changes — skipping (commit first)"
        cd "$ROOT"
        return 0
    fi

    if ! remote_push_available; then
        echo "⚠️  $repo_name: remote host unreachable — skipping"
        cd "$ROOT"
        return 0
    fi

    if git rev-parse --abbrev-ref --symbolic-full-name '@{u}' >/dev/null 2>&1; then
        git push
    else
        git push --set-upstream origin "$(git branch --show-current)"
    fi
    echo "🚀 pushed $repo_name ($ahead commit(s))"
    cd "$ROOT"
}

while IFS= read -r path; do
    [ -d "$path/.git" ] || [ -f "$path/.git" ] || continue
    push_repo "$(basename "$path")" "$path"
done < <(workspace_repo_paths)


echo "✅ push-ready complete"
