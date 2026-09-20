#!/usr/bin/env bash
set -euo pipefail

university_root() { cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd; }
workspace_root() { university_root; }

workspace_repo_paths() {
  local ws="$(workspace_root)" path
  for path in "$ws" "$ws/students"; do
    [ -d "$path/.git" ] || [ -f "$path/.git" ] || continue
    printf '%s\n' "$path"
  done
}

repo_name() { basename "$1"; }
