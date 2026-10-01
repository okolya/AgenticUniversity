#!/usr/bin/env python3
"""Generate or verify university/MANIFEST.md from canonical core records."""
import argparse
import os
import re
import sys


ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
UNIVERSITY = os.path.join(ROOT, "university")
MANIFEST = os.path.join(UNIVERSITY, "MANIFEST.md")
TEMPLATE = os.path.join(UNIVERSITY, "templates", "manifest", "MANIFEST.template.md")


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def metadata(text):
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        return {}
    result = {}
    key = None
    for raw in match.group(1).splitlines():
        item = re.match(r"^\s+-\s+\{(.*)\}\s*$", raw)
        if item and key:
            parts = dict(p.split(":", 1) for p in item.group(1).split(",") if ":" in p)
            if not isinstance(result.get(key), list):
                result[key] = []
            result[key].append({k.strip(): v.strip() for k, v in parts.items()})
            continue
        scalar = re.match(r"^([a-z_]+):\s*(.*)$", raw)
        if scalar:
            key, value = scalar.groups()
            result[key] = value.strip()
    return result


def frontmatter(path):
    data = metadata(read(path))
    if not data.get("name"):
        raise ValueError(f"{os.path.relpath(path, ROOT)} has no front matter name")
    return data


def dirs(sub, marker):
    base = os.path.join(UNIVERSITY, sub)
    return sorted(
        name
        for name in os.listdir(base)
        if os.path.isfile(os.path.join(base, name, marker))
    )


def files(sub, suffix):
    base = os.path.join(UNIVERSITY, sub)
    return sorted(
        name[: -len(suffix)]
        for name in os.listdir(base)
        if name.endswith(suffix) and name != "README.md"
    )


def manifest_startup():
    current = read(MANIFEST)
    values = {}
    for key in ("startup_profession", "startup_skill", "startup_workflow"):
        match = re.search(rf"^{key}:\s*(\S+)$", current, re.M)
        if not match:
            raise ValueError(f"MANIFEST.md has no {key}")
        values[key] = match.group(1)
    return values


def worker(name):
    path = os.path.join(UNIVERSITY, "workers", name, "WORKER.md")
    fields = {}
    for line in read(path).splitlines():
        match = re.match(r"^- ([a-z_]+):\s*(.*)$", line)
        if match:
            fields[match.group(1)] = match.group(2).strip()
    required = ("profession", "scope", "status")
    missing = [key for key in required if not fields.get(key)]
    if missing:
        raise ValueError(f"workers/{name}/WORKER.md missing {', '.join(missing)}")
    scope = fields["scope"].lower()
    if "engineering" in scope:
        scope = "engineering"
    elif "language" in scope:
        scope = "language"
    else:
        scope = "university"
    return (
        f"  - {{name: {name}, profession: {fields['profession'].lower().replace(' ', '-')}, "
        f"scope: {scope}, status: {fields['status']}, "
        f"file: workers/{name}/WORKER.md}}"
    )


def entries(sub, marker, class_required=False):
    result = []
    for name in dirs(sub, marker):
        data = frontmatter(os.path.join(UNIVERSITY, sub, name, marker))
        if class_required and data.get("class") not in {"learning", "administrative", "development", "technical"}:
            raise ValueError(f"{sub}/{name}/{marker} has invalid or missing class")
        result.append((name, data))
    return result


def render():
    startup = manifest_startup()
    professions = dirs("professions", "PROFESSION.md")
    workers = dirs("workers", "WORKER.md")
    skills = entries("skills", "SKILL.md", class_required=True)
    workflows = []
    for name in files("workflows", ".md"):
        data = frontmatter(os.path.join(UNIVERSITY, "workflows", f"{name}.md"))
        if data.get("class") not in {"learning", "administrative", "development", "technical"}:
            raise ValueError(f"workflows/{name}.md has invalid or missing class")
        workflows.append((name, data))
    policies = files("policies", ".md")
    protocols = files("protocols", ".md")
    faculties = dirs("faculties", "FACULTY.md")
    courses = dirs("courses", "COURSE.md")
    schemas = files("schemas", ".schema.json")

    lines = {}
    lines["STARTUP_PROFESSION"] = startup["startup_profession"]
    lines["STARTUP_SKILL"] = startup["startup_skill"]
    lines["STARTUP_WORKFLOW"] = startup["startup_workflow"]
    lines["PROFESSIONS"] = "\n".join(f"  - {name}" for name in professions)
    lines["WORKERS"] = "\n".join(worker(name) for name in workers)
    lines["SKILLS"] = "\n".join(
        f"  - {{name: {name}, class: {data['class']}}}" for name, data in skills
    )
    lines["WORKFLOWS"] = "\n".join(
        f"  - {{name: {name}, class: {data['class']}}}" for name, data in workflows
    )
    dependencies = []
    for name, data in workflows:
        for dependency in data.get("dependencies", []):
            if not isinstance(dependency, dict):
                raise ValueError(f"workflows/{name}/workflow.md has invalid dependency")
            dependencies.append((name, dependency))
    lines["DEPENDENCIES"] = "\n".join(
        f"  - {{workflow: {workflow}, kind: {dependency['kind']}, name: {dependency['name']}}}"
        for workflow, dependency in dependencies
    )
    lines["POLICIES"] = "\n".join(f"  - {name}" for name in policies)
    lines["PROTOCOLS"] = "\n".join(f"  - {name}" for name in protocols)
    lines["FACULTIES"] = "\n".join(f"  - {name}" for name in faculties)
    lines["COURSES"] = "\n".join(f"  - {name}" for name in courses)
    lines["SCHEMAS"] = "\n".join(f"  - {name}" for name in schemas)
    template = read(TEMPLATE)
    for key, value in lines.items():
        template = template.replace(f"{{{{{key}}}}}", value)
    if re.search(r"\{\{[A-Z_]+\}\}", template):
        raise ValueError("manifest template contains unresolved placeholders")
    return template.rstrip() + "\n"


def main(argv):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write the generated manifest")
    parser.add_argument("--check", action="store_true", help="fail when the manifest is stale")
    args = parser.parse_args(argv)
    if args.write and args.check:
        parser.error("--write and --check are mutually exclusive")
    try:
        expected = render()
    except (OSError, ValueError, KeyError) as exc:
        print(f"❌ cannot generate manifest: {exc}", file=sys.stderr)
        return 1
    actual = read(MANIFEST)
    if args.write:
        if actual != expected:
            with open(MANIFEST, "w", encoding="utf-8") as fh:
                fh.write(expected)
            print("✅ MANIFEST.md regenerated")
        else:
            print("✅ MANIFEST.md already current")
        return 0
    if actual != expected:
        print("❌ MANIFEST.md is stale; run 'make generate-manifest'", file=sys.stderr)
        return 1
    print("✅ MANIFEST.md matches canonical records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
