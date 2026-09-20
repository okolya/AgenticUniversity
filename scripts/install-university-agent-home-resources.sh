#!/usr/bin/env bash
set -euo pipefail

AGENT_NAME="${1:-}"
TARGET_DIR="${2:-}"

if [ -z "$AGENT_NAME" ] || [ -z "$TARGET_DIR" ]; then
  echo "Usage: $0 <agent-name> <target-dir>" >&2
  exit 2
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
UNIVERSITY_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
POLICIES_DIR="$UNIVERSITY_ROOT/university/policies"
WORKFLOWS_DIR="$UNIVERSITY_ROOT/university/workflows"
SKILLS_DIR="$UNIVERSITY_ROOT/university/skills"
NAMESPACE="university-"

die() { printf '✗ %s\n' "$*" >&2; exit 1; }

if [ -L "$TARGET_DIR" ]; then
  die "$TARGET_DIR is a symlink; refusing to modify a host runtime root"
fi
mkdir -p "$TARGET_DIR"

guard_target() {
  local target="$1" source="$2" resolved
  if [ -e "$target" ] || [ -L "$target" ]; then
    [ -L "$target" ] || die "$target is a regular file/directory; refusing to overwrite it"
    resolved="$(readlink -f "$target" 2>/dev/null || true)"
    [ "$resolved" = "$(readlink -f "$source" 2>/dev/null || true)" ] || die "$target points outside Agentic University"
    rm -f "$target"
  fi
}

cleanup_broken_links() {
  local target_dir="$1"
  [ -d "$target_dir" ] || return 0
  find "$target_dir" -maxdepth 1 -type l -name "${NAMESPACE}*" \
    ! -exec test -e {} \; -delete
}

link_files() {
  local source_dir="$1" target_dir="$2" pattern="$3" source base target
  mkdir -p "$target_dir"
  cleanup_broken_links "$target_dir"
  for source in "$source_dir"/$pattern; do
    [ -f "$source" ] || continue
    base="$(basename "$source")"
    target="$target_dir/$NAMESPACE$base"
    guard_target "$target" "$source"
    ln -s "$source" "$target"
  done
}

link_skills() {
  local target_dir="$1" source base target
  mkdir -p "$target_dir"
  cleanup_broken_links "$target_dir"
  for source in "$SKILLS_DIR"/*; do
    [ -d "$source" ] || continue
    [ -f "$source/SKILL.md" ] || continue
    base="$(basename "$source")"
    target="$target_dir/$NAMESPACE$base"
    guard_target "$target" "$source"
    ln -s "$source" "$target"
  done
}

link_files "$POLICIES_DIR" "$TARGET_DIR/policies" '*.md'
link_files "$WORKFLOWS_DIR" "$TARGET_DIR/workflows" '*.md'
link_skills "$TARGET_DIR/skills"

printf '✓ linked University resources to %s\n' "$TARGET_DIR"
