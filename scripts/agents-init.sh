#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

for entry in \
  "Agents:${AGENTS_HOME:-$HOME/.agents}" \
  "Codex:${CODEX_HOME:-$HOME/.codex}" \
  "Claude Code:${CLAUDE_HOME:-$HOME/.claude}" \
  "Cursor:${CURSOR_HOME:-$HOME/.cursor}"; do
  agent_name="${entry%%:*}"
  target_dir="${entry#*:}"
  bash "$SCRIPT_DIR/install-university-agent-home-resources.sh" "$agent_name" "$target_dir"
done

bash "$SCRIPT_DIR/install-codex-config-toml.sh"
printf '✅ university-core home agent resources initialized\n'
