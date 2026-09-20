#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
if [ ! -d "$ROOT/.git" ] && [ ! -f "$ROOT/.git" ]; then
  echo "Git is not initialized; no hooks expected"
  exit 0
fi
GIT_DIR="$(git -C "$ROOT" rev-parse --absolute-git-dir)"
test -x "$GIT_DIR/hooks/commit-msg"
echo "Git hooks OK"
