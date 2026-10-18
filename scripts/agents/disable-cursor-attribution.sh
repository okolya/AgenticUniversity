#!/usr/bin/env bash
set -euo pipefail

CURSOR_HOME_DIR="${CURSOR_HOME:-$HOME/.cursor}"
CONFIG="$CURSOR_HOME_DIR/cli-config.json"
BACKUP="$CURSOR_HOME_DIR/cli-config.json.backup"

mkdir -p "$CURSOR_HOME_DIR"

if [ ! -f "$CONFIG" ]; then
  printf '%s\n' '{' '  "attribution": {' '    "attributeCommitsToAgent": false,' '    "attributePRsToAgent": false' '  }' '}' > "$CONFIG"
  echo "✓ created Cursor CLI config with attribution disabled"
  exit 0
fi

if [ ! -e "$BACKUP" ] && [ ! -L "$BACKUP" ]; then
  cp "$CONFIG" "$BACKUP"
  echo "✓ backed up Cursor CLI config -> $BACKUP"
fi

python3 - "$CONFIG" <<'PY'
import re
import sys
from pathlib import Path

config_path = Path(sys.argv[1])
content = config_path.read_text()

attribution = re.compile(
    r'("attribution"\s*:\s*\{)(.*?)(\n\s*\})',
    re.DOTALL,
)
commit = re.compile(r'("attributeCommitsToAgent"\s*:\s*)(true|false)')
pr = re.compile(r'("attributePRsToAgent"\s*:\s*)(true|false)')

match = attribution.search(content)
if match:
    body = commit.sub(r'\1false', match.group(2))
    body = pr.sub(r'\1false', body)
    content = content[:match.start(2)] + body + content[match.end(2):]
else:
    closing = content.rfind("}")
    if closing < 0:
        raise SystemExit("Cursor CLI config is not an object")
    prefix = content[:closing].rstrip()
    separator = "," if prefix.endswith("}") else ""
    content = (
        prefix
        + separator
        + '\n  "attribution": {\n'
        + '    "attributeCommitsToAgent": false,\n'
        + '    "attributePRsToAgent": false\n'
        + "  }\n"
        + content[closing:]
    )

config_path.write_text(content)
PY

echo "✓ disabled Cursor commit and PR attribution globally"
