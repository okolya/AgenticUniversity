#!/usr/bin/env bash
# `make agents-init`: link the core's agent data into the provider homes.
# The work is done by the shared dev-agents tool from dev-agents.toml and pack.toml;
# this script only checks that the tool is installed and calls it.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CORE_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

command -v dev-agents >/dev/null 2>&1 || {
  echo "✗ dev-agents is not installed: in the shared-dev-agents checkout run \`make install\` (links it into ~/.local/bin)" >&2
  exit 1
}

dev-agents init --composition "$CORE_ROOT/dev-agents.toml" "$@"
# Host Cursor CLI: always opt out of commit/PR attribution (also declared as pack legacy after approve).
bash "$CORE_ROOT/scripts/agents/disable-cursor-attribution.sh"
printf '✅ university-core home agent resources initialized\n'
