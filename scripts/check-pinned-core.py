#!/usr/bin/env python3
"""Verify that a host points at one exact, clean core Git revision."""
import argparse
import os
import subprocess
import sys


def git(root, *args):
    return subprocess.check_output(
        ["git", "-C", root, *args], text=True, stderr=subprocess.STDOUT
    ).strip()


def main(argv):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=os.path.normpath(os.path.join(os.path.dirname(__file__), "..")))
    parser.add_argument("--revision", required=True, help="exact expected Git commit or tag")
    parser.add_argument("--allow-dirty", action="store_true", help="development-only override")
    args = parser.parse_args(argv)
    root = os.path.abspath(args.root)
    try:
        actual_root = git(root, "rev-parse", "--show-toplevel")
        actual_revision = git(root, "rev-parse", "HEAD")
        expected_revision = git(root, "rev-parse", f"{args.revision}^{{commit}}")
    except subprocess.CalledProcessError as exc:
        print(f"❌ cannot resolve core Git revision: {exc.output.strip()}", file=sys.stderr)
        return 2
    if os.path.realpath(actual_root) != os.path.realpath(root):
        print(f"❌ core root is not an independent Git boundary: {actual_root}", file=sys.stderr)
        return 1
    if actual_revision != expected_revision:
        print(
            f"❌ core revision mismatch: expected {expected_revision}, got {actual_revision}",
            file=sys.stderr,
        )
        return 1
    dirty = git(root, "status", "--porcelain")
    if dirty and not args.allow_dirty:
        print("❌ pinned core is dirty; validate a clean temporary copy", file=sys.stderr)
        return 1
    if not os.path.isfile(os.path.join(root, "university", "MANIFEST.md")):
        print("❌ pinned core has no university/MANIFEST.md", file=sys.stderr)
        return 1
    print(f"✅ core pinned to {actual_revision}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
