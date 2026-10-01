#!/usr/bin/env python3
"""Generate staff indexes from canonical Worker appointment records."""
import argparse
import os
import re
import sys


ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
UNIVERSITY = os.path.join(ROOT, "university")
WORKERS_DIR = os.path.join(UNIVERSITY, "workers")
FACULTIES_DIR = os.path.join(UNIVERSITY, "faculties")
GLOBAL_TEMPLATE = os.path.join(UNIVERSITY, "templates", "staff", "REGISTRY.template.md")
FACULTY_TEMPLATE = os.path.join(
    UNIVERSITY, "templates", "faculty", "STAFF.template.md"
)
GLOBAL_REGISTRY = os.path.join(UNIVERSITY, "staff", "REGISTRY.md")


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def fields(path):
    result = {}
    for line in read(path).splitlines():
        match = re.match(r"^- ([a-z_]+):\s*(.*)$", line)
        if match:
            result[match.group(1)] = match.group(2).strip()
    required = ("name", "profession", "status", "appointment", "faculty", "scope")
    missing = [key for key in required if not result.get(key)]
    if missing:
        raise ValueError(f"{os.path.relpath(path, ROOT)} missing {', '.join(missing)}")
    return result


def worker_records():
    records = []
    for name in sorted(os.listdir(WORKERS_DIR)):
        path = os.path.join(WORKERS_DIR, name, "WORKER.md")
        if not os.path.isfile(path):
            continue
        data = fields(path)
        if data["name"].lower() != name.lower():
            raise ValueError(f"{os.path.relpath(path, ROOT)} name differs from directory")
        records.append((name, data))
    return records


def cell(value):
    return value.replace("|", "\\|")


def global_row(name, data):
    faculty_scope = data["faculty"] if data["faculty"].lower() != "none" else data["scope"]
    return (
        f"| {cell(data['name'])} | {cell(data['profession'])} | "
        f"{cell(data['appointment'])} | {cell(faculty_scope)} | "
        f"{cell(data['status'])} | `university/workers/{name}/WORKER.md` |"
    )


def faculty_row(name, data):
    return (
        f"| {cell(data['name'])} | {cell(data['profession'])} | "
        f"{cell(data['appointment'])} | {cell(data['status'])} | "
        f"`university/workers/{name}/WORKER.md` |"
    )


def render_template(path, replacements):
    rendered = read(path)
    for key, value in replacements.items():
        rendered = rendered.replace("{{" + key + "}}", value)
    if "{{" in rendered or "}}" in rendered:
        raise ValueError(f"{os.path.relpath(path, ROOT)} has unresolved placeholders")
    return rendered.rstrip() + "\n"


def render():
    records = worker_records()
    global_text = render_template(
        GLOBAL_TEMPLATE,
        {"WORKERS": "\n".join(global_row(name, data) for name, data in records)},
    )
    outputs = {GLOBAL_REGISTRY: global_text}

    faculty_names = {
        name: read(os.path.join(FACULTIES_DIR, name, "FACULTY.md")).splitlines()[0].removeprefix("# ").strip()
        for name in os.listdir(FACULTIES_DIR)
        if os.path.isfile(os.path.join(FACULTIES_DIR, name, "FACULTY.md"))
    }
    for slug, display_name in faculty_names.items():
        faculty_records = [
            (name, data)
            for name, data in records
            if data["faculty"].lower() == display_name.lower()
        ]
        target = os.path.join(FACULTIES_DIR, slug, "STAFF.md")
        outputs[target] = render_template(
            FACULTY_TEMPLATE,
            {
                "FACULTY_NAME": display_name,
                "WORKERS": "\n".join(
                    faculty_row(name, data) for name, data in faculty_records
                ),
            },
        )
    return outputs


def main(argv):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write generated indexes")
    parser.add_argument("--check", action="store_true", help="fail when indexes are stale")
    args = parser.parse_args(argv)
    if args.write == args.check:
        parser.error("exactly one of --write or --check is required")
    try:
        expected = render()
    except (OSError, ValueError) as exc:
        print(f"❌ cannot generate staff indexes: {exc}", file=sys.stderr)
        return 1
    for path, content in expected.items():
        actual = read(path) if os.path.isfile(path) else None
        if actual != content:
            if args.check:
                print(
                    f"❌ {os.path.relpath(path, ROOT)} is stale; run 'make generate-staff'",
                    file=sys.stderr,
                )
                return 1
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(content)
            print(f"✅ {os.path.relpath(path, ROOT)} regenerated")
    if args.check:
        print("✅ staff indexes match canonical Worker records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
