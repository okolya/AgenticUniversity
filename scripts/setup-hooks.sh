#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
GIT_DIR="$(git -C "$ROOT" rev-parse --absolute-git-dir)"
HOOKS="$GIT_DIR/hooks"
mkdir -p "$HOOKS"

cat > "$HOOKS/pre-commit" <<'HOOK'
#!/usr/bin/env bash
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"
npm run links-check-frail --silent
python3 scripts/check-manifest.py
python3 scripts/check-core.py --root .
HOOK

cat > "$HOOKS/commit-msg" <<'HOOK'
#!/usr/bin/env bash
set -euo pipefail
MSG="$(cat "$1")"
grep -qE '^(feat|fix|docs|style|refactor|test|chore|ci|build|perf|revert)(\([^)]+\))?: .+' <<<"$MSG" || {
  echo "Invalid Conventional Commit message" >&2
  exit 1
}
HOOK

chmod +x "$HOOKS/pre-commit" "$HOOKS/commit-msg"
echo "✅ university-core hooks installed"
