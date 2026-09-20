#!/usr/bin/env bash
# Compact status of all project repositories (root + components).
# Default output: summary + only non-clean repos.
# Verbose mode: --verbose or VERBOSE=1 (branch + last commit for every repo).
# Adapted from reference PHP workspace's scripts/check-all-repos-status.sh,
# using the template's shared scripts/lib/repositories.sh discovery helper.
#
# Usage: ./scripts/check-repos-status.sh [--verbose]

set -euo pipefail

UNIVERSITY_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ROOT="$UNIVERSITY_ROOT"
source "$UNIVERSITY_ROOT/scripts/workspace-lib.sh"

VERBOSE="${VERBOSE:-0}"
[[ "${VERBOSE}" == "true" ]] && VERBOSE=1
[[ "${1:-}" == "--verbose" ]] && VERBOSE=1

# repo_status_for: prints "status|issues|branch|last_commit" for one repo.
# status is one of: CLEAN, NEW, UNCOMMITTED, UNCOMMITTED+AHEAD, AHEAD, BEHIND, AHEAD+BEHIND, NOT_GIT.
repo_status_for() {
    local repo_path="$1"
    local status issues branch last_commit

    if [ ! -d "$repo_path/.git" ] && [ ! -f "$repo_path/.git" ]; then
        printf 'NOT_GIT|Not a git repository|N/A|N/A\n'
        return 0
    fi

    branch="$(git -C "$repo_path" branch --show-current 2>/dev/null || echo detached)"

    if git -C "$repo_path" rev-parse --verify HEAD >/dev/null 2>&1; then
        last_commit="$(git -C "$repo_path" log -1 --format='%h %s' --no-merges 2>/dev/null || echo 'no commits')"
    else
        printf 'NEW|Initial commit required|%s|new repository (no commits)\n' "$branch"
        return 0
    fi

    local has_uncommitted=false
    [ -n "$(git -C "$repo_path" status --porcelain 2>/dev/null)" ] && has_uncommitted=true

    local ahead behind
    ahead="$(git -C "$repo_path" rev-list --count '@{u}..HEAD' 2>/dev/null || echo 0)"
    behind="$(git -C "$repo_path" rev-list --count 'HEAD..@{u}' 2>/dev/null || echo 0)"

    if [ "$has_uncommitted" = true ] && [ "$ahead" -gt 0 ]; then
        status="UNCOMMITTED+AHEAD"
        issues="Uncommitted changes + ${ahead} commits ahead"
    elif [ "$has_uncommitted" = true ]; then
        status="UNCOMMITTED"
        issues="Has uncommitted changes"
    elif [ "$ahead" -gt 0 ] && [ "$behind" -gt 0 ]; then
        status="AHEAD+BEHIND"
        issues="${ahead} ahead, ${behind} behind origin"
    elif [ "$ahead" -gt 0 ]; then
        status="AHEAD"
        issues="${ahead} commits ahead of origin"
    elif [ "$behind" -gt 0 ]; then
        status="BEHIND"
        issues="${behind} commits behind origin"
    else
        status="CLEAN"
        issues=""
    fi

    printf '%s|%s|%s|%s\n' "$status" "$issues" "$branch" "$last_commit"
}

total_repos=0
clean_repos=0
dirty_repos=0
ahead_repos=0
behind_repos=0
failed_repos=0

echo "🔍 Checking repository status..."
echo ""



report_repo() {
    local repo_display="$1" repo_path="$2"
    total_repos=$((total_repos + 1))

    local status_info status issues branch last_commit
    status_info="$(repo_status_for "$repo_path")"
    status="$(echo "$status_info" | cut -d'|' -f1)"
    issues="$(echo "$status_info" | cut -d'|' -f2)"
    branch="$(echo "$status_info" | cut -d'|' -f3)"
    last_commit="$(echo "$status_info" | cut -d'|' -f4)"

    case "$status" in
        CLEAN)
            clean_repos=$((clean_repos + 1))
            if [ "$VERBOSE" = "1" ]; then
                printf "  %-25s %s\n" "${repo_display}:" "✅ CLEAN"
            fi
            ;;
        UNCOMMITTED|UNCOMMITTED+AHEAD)
            dirty_repos=$((dirty_repos + 1))
            printf "  %-25s ❌ %s" "${repo_display}:" "$status"
            [ -n "$issues" ] && printf " (%s)" "$issues"
            printf "\n"
            [ "$VERBOSE" = "1" ] && {
                printf "    Branch: %s\n" "$branch"
                printf "    Last commit: %s\n" "$last_commit"
            }
            ;;
        AHEAD|BEHIND|AHEAD+BEHIND)
            if [ "$status" = "BEHIND" ]; then
                behind_repos=$((behind_repos + 1))
            else
                ahead_repos=$((ahead_repos + 1))
            fi
            printf "  %-25s ❌ %s" "${repo_display}:" "$status"
            [ -n "$issues" ] && printf " (%s)" "$issues"
            printf "\n"
            [ "$VERBOSE" = "1" ] && {
                printf "    Branch: %s\n" "$branch"
                printf "    Last commit: %s\n" "$last_commit"
            }
            ;;
        NEW)
            dirty_repos=$((dirty_repos + 1))
            printf "  %-25s ⚠️  %s" "${repo_display}:" "$status"
            [ -n "$issues" ] && printf " (%s)" "$issues"
            printf "\n"
            ;;
        NOT_GIT)
            failed_repos=$((failed_repos + 1))
            printf "  %-25s ❌ %s" "${repo_display}:" "$status"
            [ -n "$issues" ] && printf " (%s)" "$issues"
            printf "\n"
            [ "$VERBOSE" = "1" ] && {
                printf "    Branch: %s\n" "$branch"
                printf "    Last commit: %s\n" "$last_commit"
            }
            ;;
    esac
}

while IFS= read -r path; do
    report_repo "$(basename "$path")" "$path"
done < <(workspace_repo_paths)

echo ""
echo "📊 Summary:"
echo "  Total repositories: $total_repos"
echo "  Clean: $clean_repos"
echo "  Dirty: $dirty_repos"
echo "  Ahead of origin: $ahead_repos"
echo "  Behind origin: $behind_repos"
echo "  Failed: $failed_repos"
echo ""

if [ "$dirty_repos" -eq 0 ] && [ "$ahead_repos" -eq 0 ] && [ "$behind_repos" -eq 0 ] && [ "$failed_repos" -eq 0 ]; then
    echo "🎉 All repositories are clean and up to date!"
    exit 0
else
    echo "⚠️  Some repositories need attention"
    exit 1
fi
