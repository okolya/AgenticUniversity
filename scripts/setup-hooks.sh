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
make generate
git add university/MANIFEST.md university/staff/REGISTRY.md university/faculties/*/STAFF.md
python3 scripts/generate-manifest.py --check
python3 scripts/generate-staff.py --check
npm run links-check-frail --silent
python3 scripts/check-manifest.py
python3 scripts/check-core.py --root .
HOOK

{
  cat <<'HOOK'
#!/usr/bin/env bash
set -euo pipefail
COMMIT_MSG_FILE="$1"

HOOK
  cat <<'HOOK'

MSG="$(cat "$COMMIT_MSG_FILE")"
grep -qE '^(feat|fix|docs|style|refactor|test|chore|ci|build|perf|revert)(\([^)]+\))?: .+' <<<"$MSG" || {
  echo "Invalid Conventional Commit message" >&2
  exit 1
}
HOOK
} > "$HOOKS/commit-msg"

chmod +x "$HOOKS/pre-commit" "$HOOKS/commit-msg"
echo "✅ university-core hooks installed"

# AI co-author trailers: one shared implementation, the dev-agents commit-msg block ([git] strip_ai_trailers in dev-agents.toml).
# It runs after this script so a rewritten hook gets the block back.
if [ -f "$ROOT/../dev-agents.toml" ]; then
    dev-agents hooks install --repo "$ROOT/.." --composition "$ROOT/../dev-agents.toml" >/dev/null \
        || { echo "❌ dev-agents hooks install failed: put shared-dev-agents on PATH (make install there) and re-run" >&2; exit 1; }
fi
