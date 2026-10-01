#!/usr/bin/env python3
"""Markdown link tooling for the University workspace.

  doc-links.py check  [--quiet]   verify relative links and #anchors in tracked *.md
  doc-links.py relink [--dry-run] rewrite inbound links/paths for staged renames

`relink` reads renames from the Git index (`git mv` stages them), fixes Markdown
link targets and exact root-relative paths in *.md files, and re-stages only the
files it changed. Files with unstaged edits are never touched (reported instead).
"""
import os
import re
import subprocess
import sys
import urllib.parse

ROOT = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip()
os.chdir(ROOT)

FENCE = re.compile(r"^\s*(```|~~~)")
INLINE_CODE = re.compile(r"`[^`\n]*`")
LINK = re.compile(r"(!?\[[^\]\n]*\]\()(<[^>\n]+>|[^)\s]+)((?:\s+\"[^\"]*\")?\))")
REFDEF = re.compile(r"^(\s{0,3}\[[^\]\n]+\]:\s+)(<[^>\n]+>|\S+)(.*)$")
SCHEME = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")


def git(*args):
    return subprocess.check_output(["git", *args], text=True)


def md_files():
    out = git("ls-files", "-z", "--", "*.md").split("\0")
    return [p for p in out if p and not os.path.islink(p) and os.path.isfile(p)]


def slug(heading):
    text = re.sub(r"[`*_~]|<[^>]+>|\[([^\]]*)\]\([^)]*\)", lambda m: m.group(1) or "", heading)
    text = text.strip().lower()
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


_anchor_cache = {}


def anchors(path):
    if path not in _anchor_cache:
        seen, result, fenced = {}, set(), False
        with open(path, encoding="utf-8", errors="replace") as fh:
            for line in fh:
                if FENCE.match(line):
                    fenced = not fenced
                    continue
                m = None if fenced else re.match(r"^#{1,6}\s+(.*?)\s*#*\s*$", line)
                if m:
                    base = slug(m.group(1))
                    n = seen.get(base, 0)
                    seen[base] = n + 1
                    result.add(base if n == 0 else f"{base}-{n}")
        _anchor_cache[path] = result
    return _anchor_cache[path]


def targets(line):
    """Yield (start, end, raw_target) for link targets in a line, skipping inline code."""
    spans = [(m.start(), m.end()) for m in INLINE_CODE.finditer(line)]
    inside = lambda i: any(a <= i < b for a, b in spans)
    for m in LINK.finditer(line):
        if not inside(m.start()):
            yield m.start(2), m.end(2), m.group(2)
    m = REFDEF.match(line)
    if m:
        yield m.start(2), m.end(2), m.group(2)


def split_target(raw):
    raw = raw.strip("<>")
    if not raw or raw.startswith("#") or SCHEME.match(raw) or raw.startswith("//"):
        return None
    path, _, anchor = raw.partition("#")
    path = urllib.parse.unquote(path.split("?", 1)[0])
    return path, anchor


def resolve(src, path):
    base = ROOT if path.startswith("/") else os.path.dirname(os.path.join(ROOT, src))
    return os.path.normpath(os.path.join(base, path.lstrip("/") if path.startswith("/") else path))


def check(quiet=False):
    problems = []
    for src in md_files():
        fenced = False
        with open(src, encoding="utf-8", errors="replace") as fh:
            for no, line in enumerate(fh, 1):
                if FENCE.match(line):
                    fenced = not fenced
                    continue
                if fenced:
                    continue
                for _, _, raw in targets(line):
                    parts = split_target(raw)
                    if parts is None:
                        continue
                    path, anchor = parts
                    if not path:
                        continue
                    dest = resolve(src, path)
                    if not dest.startswith(ROOT + os.sep) and dest != ROOT:
                        problems.append((src, no, raw, "points outside the repository"))
                    elif not os.path.exists(dest):
                        problems.append((src, no, raw, "target not found"))
                    elif anchor and dest.endswith(".md") and os.path.isfile(dest):
                        if urllib.parse.unquote(anchor).lower() not in anchors(dest):
                            problems.append((src, no, raw, "anchor not found"))
    if problems:
        print(f"❌ {len(problems)} broken documentation link(s):")
        for src, no, raw, why in problems:
            print(f"   {src}:{no}  ({raw})  {why}")
        print("💡 Fix the link, or after `git mv` run: make relink")
        return 1
    if not quiet:
        print("✅ Documentation links OK")
    return 0


def staged_renames():
    renames = {}
    raw = git("diff", "--cached", "-M", "--name-status", "--diff-filter=R", "-z").split("\0")
    i = 0
    while i < len(raw) and raw[i]:
        if raw[i].startswith("R") and i + 2 < len(raw):
            renames[raw[i + 1]] = raw[i + 2]
            i += 3
        else:
            i += 1
    return renames


def relink(dry_run=False):
    renames = staged_renames()
    if not renames:
        print("ℹ️  No staged renames; nothing to relink")
        return 0
    inverse = {new: old for old, new in renames.items()}
    unstaged = set(git("diff", "--name-only", "-z").split("\0"))
    changed, skipped = [], []

    for src in md_files():
        old_src = inverse.get(src, src)
        if not os.path.isfile(src):
            continue
        text = open(src, encoding="utf-8").read()
        lines, fenced, out = text.split("\n"), False, []
        for line in lines:
            if FENCE.match(line):
                fenced = not fenced
            elif not fenced:
                edits = []
                for start, end, raw in targets(line):
                    parts = split_target(raw)
                    if parts is None or not parts[0]:
                        continue
                    path, anchor = parts
                    old_abs = resolve(old_src, path)
                    old_rel = os.path.relpath(old_abs, ROOT)
                    new_rel = renames.get(old_rel)
                    if new_rel is None and (old_src == src or not os.path.exists(old_abs)):
                        continue
                    target_rel = new_rel or old_rel
                    if not os.path.exists(os.path.join(ROOT, target_rel)):
                        continue
                    if path.startswith("/"):
                        new_path = "/" + target_rel
                    else:
                        new_path = os.path.relpath(os.path.join(ROOT, target_rel), os.path.dirname(os.path.join(ROOT, src)))
                    if new_path != path:
                        edits.append((start, end, raw, new_path + ("#" + anchor if anchor else "")))
                for start, end, raw, new in sorted(edits, reverse=True):
                    wrapped = f"<{new}>" if raw.startswith("<") else urllib.parse.quote(new, safe="/#.-_~@:+") if " " in raw or "%" in raw else new
                    line = line[:start] + wrapped + line[end:]
                for old, new in renames.items():
                    line = re.sub(r"(?<![\w/.\-])" + re.escape(old) + r"(?![\w/\-])", new, line)
            out.append(line)
        new_text = "\n".join(out)
        if new_text != text:
            if src in unstaged:
                skipped.append(src)
            else:
                changed.append(src)
                if not dry_run:
                    open(src, "w", encoding="utf-8").write(new_text)

    for src in changed:
        print(("would relink " if dry_run else "🔗 relinked ") + src)
    if changed and not dry_run:
        git("add", "--", *changed)
    for src in skipped:
        print(f"⚠️  {src} needs relinking but has unstaged edits; stage or stash it and re-run `make relink`")
    return 0


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    flags = set(sys.argv[2:])
    if cmd == "check":
        sys.exit(check("--quiet" in flags))
    if cmd == "relink":
        sys.exit(relink("--dry-run" in flags))
    print(__doc__)
    sys.exit(2)
