#!/usr/bin/env python3
"""Verify university/MANIFEST.md lists exactly what exists under university/.

The manifest front matter uses a constrained YAML subset (scalars, lists of
scalars, lists of inline `{k: v, ...}` maps) that this script parses without
third-party packages. Exit 1 on any mismatch.
"""
import json
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "university")
ROOT = os.path.normpath(ROOT)


def parse_front_matter(path):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        sys.exit("❌ MANIFEST.md has no front matter")
    data, key = {}, None
    for raw in m.group(1).split("\n"):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        item = re.match(r"^\s+-\s+(.*)$", raw)
        if item and key is not None:
            value = item.group(1).strip()
            if value.startswith("{"):
                value = dict(
                    (k.strip(), v.strip())
                    for k, v in (p.split(":", 1) for p in value.strip("{}").split(","))
                )
            data[key].append(value)
            continue
        top = re.match(r"^([A-Za-z_]+):\s*(.*)$", raw)
        if top:
            key = top.group(1)
            data[key] = [] if top.group(2) == "" else top.group(2).strip()
    return data


def validate(value, schema, root, path="$"):
    """Validate the JSON Schema subset used by university/schemas (type, enum, required,
    properties, additionalProperties, items, $ref to #/$defs)."""
    errors = []
    if "$ref" in schema:
        schema = root["$defs"][schema["$ref"].split("/")[-1]]
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: {value!r} not in {schema['enum']}")
    t = schema.get("type")
    kinds = {"object": dict, "array": list, "string": str}
    if t and not isinstance(value, kinds[t]):
        return errors + [f"{path}: expected {t}"]
    if t == "object":
        props = schema.get("properties", {})
        for k in schema.get("required", []):
            if k not in value:
                errors.append(f"{path}: missing '{k}'")
        for k, v in value.items():
            if k in props:
                errors += validate(v, props[k], root, f"{path}.{k}")
            elif schema.get("additionalProperties") is False:
                errors.append(f"{path}: unexpected '{k}'")
    if t == "array":
        for i, item in enumerate(value):
            errors += validate(item, schema["items"], root, f"{path}[{i}]")
    return errors


def listing(sub, want_dirs=None, suffix=None, marker=None):
    base = os.path.join(ROOT, sub)
    out = set()
    for name in os.listdir(base):
        full = os.path.join(base, name)
        if want_dirs and os.path.isdir(full) and (not marker or os.path.isfile(os.path.join(full, marker))):
            out.add(name)
        elif suffix and os.path.isfile(full) and name.endswith(suffix) and name != "README.md":
            out.add(name[: -len(suffix)])
    return out


def field(path, label):
    m = re.search(rf"^- {label}:\s*(.+)$", open(path, encoding="utf-8").read(), re.M)
    return m.group(1).strip() if m else None


def main():
    man = parse_front_matter(os.path.join(ROOT, "MANIFEST.md"))
    problems = []

    def same(label, declared, actual):
        declared, actual = set(declared), set(actual)
        for x in sorted(actual - declared):
            problems.append(f"{label}: '{x}' exists but is not in the manifest")
        for x in sorted(declared - actual):
            problems.append(f"{label}: '{x}' is in the manifest but missing on disk")

    same("professions", man["professions"], listing("professions", want_dirs=True, marker="PROFESSION.md"))
    same("policies", man["policies"], listing("policies", suffix=".md"))
    same("protocols", man["protocols"], listing("protocols", suffix=".md"))
    same("workflows", man["workflows"], listing("workflows", suffix=".md"))
    same("faculties", man["faculties"], listing("faculties", want_dirs=True, marker="FACULTY.md"))
    same("courses", man["courses"], listing("courses", want_dirs=True, marker="COURSE.md"))
    same("skills", [s["name"] for s in man["skills"]], listing("skills", want_dirs=True, marker="SKILL.md"))
    same("workers", [w["name"] for w in man["workers"]], listing("workers", want_dirs=True, marker="WORKER.md"))

    same("schemas", man.get("schemas", []), {n[: -len(".schema.json")] for n in os.listdir(os.path.join(ROOT, "schemas")) if n.endswith(".schema.json")})
    for name in man.get("schemas", []):
        schema_path = os.path.join(ROOT, "schemas", f"{name}.schema.json")
        example_path = os.path.join(ROOT, "schemas", f"{name}.example.json")
        if not os.path.isfile(schema_path):
            continue
        if not os.path.isfile(example_path):
            problems.append(f"schemas: '{name}' has no example file")
            continue
        schema = json.load(open(schema_path, encoding="utf-8"))
        for err in validate(json.load(open(example_path, encoding="utf-8")), schema, schema):
            problems.append(f"schemas: {name} example {err}")

    classes = {"learning", "administrative", "maintenance"}
    for s in man["skills"]:
        if s.get("class") not in classes:
            problems.append(f"skills: '{s['name']}' has invalid class '{s.get('class')}'")
    professions = set(man["professions"])
    for w in man["workers"]:
        path = os.path.join(ROOT, w["file"])
        if not os.path.isfile(path):
            problems.append(f"workers: file '{w['file']}' not found")
            continue
        prof = (field(path, "profession") or "").lower().replace(" ", "-")
        if prof != w["profession"] or prof not in professions:
            problems.append(f"workers: '{w['name']}' profession is '{prof}' in WORKER.md, '{w['profession']}' in manifest")
        if (field(path, "status") or "") != w["status"]:
            problems.append(f"workers: '{w['name']}' status differs from WORKER.md")
    for key in ("startup_skill", "startup_profession", "startup_workflow"):
        if key not in man:
            problems.append(f"entry point '{key}' missing")

    if problems:
        print(f"❌ {len(problems)} manifest problem(s):")
        for p in problems:
            print("   " + p)
        print("💡 Update university/MANIFEST.md to match the University contents.")
        return 1
    print("✅ Manifest matches University contents")
    return 0


if __name__ == "__main__":
    sys.exit(main())
