#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/workspace-lib.sh"
UNI="$(university_root)"
WS="$(workspace_root)"
STUDENTS="$WS/students"

fail(){ printf '✗ %s\n' "$*" >&2; exit 1; }
info(){ printf '✓ %s\n' "$*"; }

link_safe() {
  local source="$1" target="$2" rel current expected
  [ -e "$source" ] || fail "missing source: $source"
  mkdir -p "$(dirname "$target")"
  if [ -e "$target" ] || [ -L "$target" ]; then
    if [ -L "$target" ]; then
      current="$(readlink -f "$target" 2>/dev/null || true)"
      expected="$(readlink -f "$source" 2>/dev/null || true)"
      [ -n "$current" ] && [ "$current" = "$expected" ] && return 0
    fi
    fail "refusing to replace existing workspace path: $target"
  fi
  rel="$(realpath --relative-to="$(dirname "$target")" "$source")"
  ln -s "$rel" "$target"
}

# Private Students repository: create only when absent; never overwrite existing state.
if [ ! -e "$STUDENTS" ]; then
  mkdir -p "$STUDENTS/students" "$STUDENTS/registry"
  cat > "$STUDENTS/README.md" <<'TXT'
# Private Students Repository

This repository stores only private educational state for real students.

It does not own AI agents, professions, skills, policies, workflows, public course/module definitions, teaching materials, or reusable knowledge. Those belong to the sibling public `university/` repository.

- `registry/REGISTRY.md` is the private operational index of registered students.
- `students/<student-id>/` contains only that student's private learning-process state.
- Public University entities are referenced, not copied.
- Reusable depersonalized knowledge discovered during learning is promoted to the public University.
TXT
  cp "$UNI/university/templates/students-workspace/REGISTRY.template.md" "$STUDENTS/registry/REGISTRY.md"
  touch "$STUDENTS/students/.gitkeep"
  git -C "$STUDENTS" init -q
  info "created private Students Git repository at $STUDENTS"
else
  [ -d "$STUDENTS" ] || fail "$STUDENTS exists and is not a directory"
  [ -d "$STUDENTS/.git" ] || [ -f "$STUDENTS/.git" ] || fail "existing students/ is not a Git repository; refusing to modify it"
  info "existing private Students repository preserved"
fi

# Root entry files are direct University links.
link_safe "$UNI/WORKSPACE.md" "$WS/README.md"
for f in AGENTS.md CLAUDE.md CODEX.md CURSOR.md; do
  link_safe "$UNI/$f" "$WS/$f"
done

# Runtime directories are links to the University checkout. The University repo
# owns all generated runtime content; Students owns none of it.
for d in .agents .claude .codex .cursor; do
  if [ ! -e "$UNI/$d" ] && [ ! -L "$UNI/$d" ]; then
    mkdir -p "$UNI/$d"
  fi
  link_safe "$UNI/$d" "$WS/$d"
done

if "$SCRIPT_DIR/check-students-origin.sh"; then
  :
else
  printf '⚠ students repository exists locally but is not yet connected to a private origin remote.\n' >&2
fi

info "workspace root composed at $WS"
