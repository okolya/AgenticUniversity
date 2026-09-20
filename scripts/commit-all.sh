#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/workspace-lib.sh"
WS="$(workspace_root)"
MSG_FILE="${UNIVERSITY_COMMIT_MESSAGES_FILE:-$WS/.UNIVERSITY-commit-messages.env}"

message_for(){
  local name="$1" v=""
  if [ -f "$MSG_FILE" ]; then v="$(grep -E "^${name}=" "$MSG_FILE" 2>/dev/null | tail -n1 | cut -d= -f2- || true)"; fi
  [ -n "$v" ] && printf '%s\n' "$v" || printf 'chore: update %s\n' "$name"
}

while IFS= read -r repo; do
  name="$(basename "$repo")"
  if [ -n "$(git -C "$repo" status --porcelain)" ]; then
    git -C "$repo" add -A
    git -C "$repo" commit -m "$(message_for "$name")"
    echo "✅ committed $name"
  fi
done < <(workspace_repo_paths)

if [ -f "$MSG_FILE" ]; then rm -f "$MSG_FILE"; fi
