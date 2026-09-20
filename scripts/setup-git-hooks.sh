#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
if [ ! -d "$ROOT/.git" ] && [ ! -f "$ROOT/.git" ]; then
  echo "⚠️  Git is not initialized; hooks skipped"
  exit 0
fi
GIT_DIR="$(git -C "$ROOT" rev-parse --absolute-git-dir)"
mkdir -p "$GIT_DIR/hooks"
cat > "$GIT_DIR/hooks/commit-msg" <<'HOOK'
#!/usr/bin/env bash
set -euo pipefail
MSG_FILE="$1"
MSG="$(cat "$MSG_FILE")"
if ! printf '%s\n' "$MSG" | grep -qE '^(feat|fix|docs|style|refactor|test|chore|ci|build|perf|revert)(\([^)]+\))?: .+'; then
  echo "❌ Invalid commit message format"
  echo "💡 Use Conventional Commits, e.g. feat: add module workflow"
  exit 1
fi
HOOK
chmod +x "$GIT_DIR/hooks/commit-msg"
echo "✅ Root Git hooks installed"
