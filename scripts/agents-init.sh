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
printf '✅ university-core home agent resources initialized\n'
