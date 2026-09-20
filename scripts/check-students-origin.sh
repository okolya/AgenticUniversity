#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/workspace-lib.sh"
STUDENTS="$(workspace_root)/students"

fail(){ printf '✗ %s\n' "$*" >&2; exit 1; }

[ -d "$STUDENTS/.git" ] || [ -f "$STUDENTS/.git" ] || fail "students/ is not a Git repository"
origin="$(git -C "$STUDENTS" remote get-url origin 2>/dev/null || true)"
[ -n "$origin" ] || fail "students repository has no origin remote. Add its private remote before using it as a persistent Student store."
printf '✓ students origin: %s\n' "$origin"
