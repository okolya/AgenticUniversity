#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
UNIVERSITY_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PROJECT_ROOT="$UNIVERSITY_ROOT"
RUNTIME_ROOT="$UNIVERSITY_ROOT/agent-runtime/adapters"
UNIVERSITY_SKILLS="$UNIVERSITY_ROOT/university/skills"
NAMESPACE="university"

fail() { printf '✗ %s\n' "$*" >&2; exit 1; }
info() { printf '✓ %s\n' "$*"; }
warn() { printf '⚠ %s\n' "$*"; }

relative_link() {
  local source="$1" target="$2" rel
  [ -e "$source" ] || fail "missing source: $source"
  mkdir -p "$(dirname "$target")"

  # Never replace project-owned files/directories or foreign symlinks.
  if [ -e "$target" ] || [ -L "$target" ]; then
    if [ -L "$target" ]; then
      local current expected
      current="$(readlink -f "$target" 2>/dev/null || true)"
      expected="$(readlink -f "$source" 2>/dev/null || true)"
      if [ -n "$current" ] && [ "$current" = "$expected" ]; then
        return 0
      fi
    fi
    fail "refusing to replace existing project path: $target"
  fi

  rel="$(realpath --relative-to="$(dirname "$target")" "$source")"
  ln -s "$rel" "$target"
}

# Remove only links that both carry our namespace and resolve inside this
# checkout. Foreign links are never touched.
remove_stale_managed_links() {
  local target_dir="$1" expected_root="$2" link resolved base
  [ -d "$target_dir" ] || return 0
  while IFS= read -r -d '' link; do
    base="$(basename "$link")"
    [[ "$base" == ${NAMESPACE}-* ]] || continue
    resolved="$(readlink -f "$link" 2>/dev/null || true)"
    if [ -z "$resolved" ] || [[ "$resolved" == "$expected_root"/* ]]; then
      rm -f "$link"
    fi
  done < <(find "$target_dir" -mindepth 1 -maxdepth 1 -type l -print0)
}

link_named_files() {
  local source_dir="$1" target_dir="$2" pattern="$3" source target
  mkdir -p "$target_dir"
  remove_stale_managed_links "$target_dir" "$RUNTIME_ROOT"
  shopt -s nullglob
  for source in "$source_dir"/$pattern; do
    target="$target_dir/${NAMESPACE}-$(basename "$source")"
    relative_link "$source" "$target"
  done
  shopt -u nullglob
}

link_skills() {
  local target_root="$1" skill target
  mkdir -p "$target_root"
  remove_stale_managed_links "$target_root" "$UNIVERSITY_SKILLS"
  shopt -s nullglob
  for skill in "$UNIVERSITY_SKILLS"/*; do
    [ -d "$skill" ] || continue
    [ -f "$skill/SKILL.md" ] || continue
    target="$target_root/${NAMESPACE}-$(basename "$skill")"
    relative_link "$skill" "$target"
  done
  shopt -u nullglob
}

link_namespace_dir() {
  local runtime_dir="$1" name="$2" source="$3" target
  target="$runtime_dir/$NAMESPACE/$name"
  relative_link "$source" "$target"
}

printf 'Initializing Agentic University runtime adapters (non-destructive)\n'
printf 'Project: %s\n' "$PROJECT_ROOT"

# Skills are namespaced so an existing project can keep skills with the same names.
link_skills "$PROJECT_ROOT/.agents/skills"
link_skills "$PROJECT_ROOT/.claude/skills"
link_skills "$PROJECT_ROOT/.codex/skills"
link_skills "$PROJECT_ROOT/.cursor/skills"
info "linked namespaced University skills without touching project skills"

# Runtime-specific profession agents are also namespaced.
link_named_files "$RUNTIME_ROOT/claude/agents" "$PROJECT_ROOT/.claude/agents" '*.md'
info "linked Claude University profession agents"
link_named_files "$RUNTIME_ROOT/codex/agents" "$PROJECT_ROOT/.codex/agents" '*.toml'
info "linked Codex University profession agents"
link_named_files "$RUNTIME_ROOT/cursor/agents" "$PROJECT_ROOT/.cursor/agents" '*.md'
info "linked Cursor University profession agents"
link_named_files "$RUNTIME_ROOT/cursor/rules" "$PROJECT_ROOT/.cursor/rules" '*.mdc'
info "linked Cursor University rules"

# Policies/workflows live below a University namespace instead of claiming
# .claude/policies, .codex/workflows, etc. from the host project.
for runtime in .claude .codex .cursor; do
  mkdir -p "$PROJECT_ROOT/$runtime/$NAMESPACE"
  link_namespace_dir "$PROJECT_ROOT/$runtime" policies "$UNIVERSITY_ROOT/university/policies"
  link_namespace_dir "$PROJECT_ROOT/$runtime" workflows "$UNIVERSITY_ROOT/university/workflows"
done
info "linked policies and workflows under runtime-specific University namespaces"

# Install public University resources into each provider home with a namespace.
for entry in "Agents:${AGENTS_HOME:-$HOME/.agents}" "Codex:${CODEX_HOME:-$HOME/.codex}" "Claude Code:${CLAUDE_HOME:-$HOME/.claude}" "Cursor:${CURSOR_HOME:-$HOME/.cursor}"; do
  agent_name="${entry%%:*}"
  target_dir="${entry#*:}"
  "$SCRIPT_DIR/install-university-agent-home-resources.sh" "$agent_name" "$target_dir"
done
info "installed namespaced University Skills, policies, and workflows into provider homes"

"$SCRIPT_DIR/install-codex-config-toml.sh"
info "installed the University Codex project overlay"

printf '✅ Agent runtime initialization complete; existing project agent assets were preserved\n'
