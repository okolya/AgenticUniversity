#!/usr/bin/env bash
# Shared template repository discovery for status, commit, and hooks.

set -euo pipefail

project_component_repo_paths() {
  local root="$1"
  local path

  while IFS= read -r path; do
    [ -d "$path/.git" ] || [ -f "$path/.git" ] || continue
    printf '%s\n' "$path"
  done < <(find "$root" -mindepth 1 -maxdepth 1 -type d | sort)
}

project_repo_name() {
  local root="$1"
  local repo_path="$2"

  if [ "$repo_path" = "$root" ]; then
    printf '.\n'
  else
    basename "$repo_path"
  fi
}
