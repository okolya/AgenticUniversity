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
  git -C "$STUDENTS" init -q -b main
  # Reuse the effective Git identity from University when available so the
  # freshly created private repository can be committed immediately.
  git_name="$(git -C "$UNI" config user.name 2>/dev/null || true)"
  git_email="$(git -C "$UNI" config user.email 2>/dev/null || true)"
  [ -z "$git_name" ] || git -C "$STUDENTS" config user.name "$git_name"
  [ -z "$git_email" ] || git -C "$STUDENTS" config user.email "$git_email"
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

# Runtime roots must be real workspace directories. Codex sandboxes may reject
# a writable root that is itself a symlink. Only University-owned legacy aliases
# are detached; foreign symlinks and files are refused.
prepare_runtime_dir() {
  local name="$1" target legacy resolved
  target="$WS/$name"
  legacy="$UNI/$name"

  if [ -L "$target" ]; then
    resolved="$(readlink -f "$target" 2>/dev/null || true)"
    [ "$resolved" = "$legacy" ] || fail "refusing to replace foreign runtime symlink: $target"
    rm -f "$target"
  elif [ -e "$target" ] && [ ! -d "$target" ]; then
    fail "runtime path exists but is not a directory: $target"
  fi

  mkdir -p "$target"
}

for d in .agents .claude .codex .cursor; do
  prepare_runtime_dir "$d"
done

# Remove only generated University runtime state left in the old repository
# runtime roots. The cleanup script refuses foreign files before removing.
"$SCRIPT_DIR/clean-agent-runtime.sh"

if "$SCRIPT_DIR/check-students-origin.sh"; then
  :
else
  printf '⚠ students repository exists locally but is not yet connected to a private origin remote.\n' >&2
fi

info "workspace root composed at $WS"
