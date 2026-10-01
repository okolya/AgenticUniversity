#!/usr/bin/env python3
"""Mechanical integrity checks for the University core (standard library only).

Each check is a named function `check(core) -> list[str]` returning problems
(empty list = pass). Checks only read files under the core root; they never
change repository state.

Usage:
  check-core.py                 run all checks
  check-core.py --list          list check names
  check-core.py NAME [NAME...]  run only the named checks
  check-core.py --root DIR      check another core copy (used by the self-test)

Exit status: 0 all pass, 1 at least one problem, 2 usage error.
"""
import argparse
import os
import sys

REPO = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

CHECKS = {}


def check(name, group):
    """Register a check under a unique name and a group (structure, data, contract)."""

    def register(fn):
        if name in CHECKS:
            raise ValueError(f"duplicate check name: {name}")
        CHECKS[name] = (group, fn)
        return fn

    return register


class Core:
    """Read-only view of a core tree; `root` is the directory that contains `university/`."""

    def __init__(self, root):
        self.root = os.path.abspath(root)
        self.uni = os.path.join(self.root, "university")

    def path(self, *parts):
        return os.path.join(self.uni, *parts)

    def read(self, *parts):
        with open(self.path(*parts), encoding="utf-8") as fh:
            return fh.read()

    def files(self, sub="", suffix=".md"):
        """Yield university-relative paths of files under `sub` ending in `suffix`."""
        base = self.path(sub)
        for dirpath, _dirs, names in os.walk(base):
            for name in sorted(names):
                if name.endswith(suffix):
                    yield os.path.relpath(os.path.join(dirpath, name), self.uni)

    def relative(self, rel):
        return rel.replace(os.sep, "/")


import re

# Files that live only in the private `students/` repository; public docs may name them.
PRIVATE_SIDE = ("students/", "STUDENT.md")

BACKTICK = re.compile(r"`([^`\n]+)`")
MD_ROW = re.compile(r"^\|(.+)\|\s*$")


def norm(text):
    """Normalise a Profession/Worker label to a slug: 'Laboratory Specialist' -> 'laboratory-specialist'."""
    return re.sub(r"[^a-z0-9]+", "-", text.strip().lower()).strip("-")


def table_rows(text):
    """Return markdown table body rows as lists of stripped cells (header and separator skipped)."""
    rows = []
    for line in text.splitlines():
        m = MD_ROW.match(line)
        if not m:
            continue
        cells = [c.strip() for c in m.group(1).split("|")]
        if all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
            continue
        rows.append(cells)
    return rows[1:] if rows else rows


def worker_fields(core, name):
    """Parse the leading `- key: value` list of a WORKER.md into a dict."""
    fields = {}
    for line in core.read("workers", name, "WORKER.md").splitlines():
        m = re.match(r"^- ([a-z_]+):\s*(.*)$", line)
        if m:
            fields[m.group(1)] = m.group(2).strip()
    return fields


def worker_names(core):
    base = core.path("workers")
    return sorted(n for n in os.listdir(base) if os.path.isfile(os.path.join(base, n, "WORKER.md")))


def profession_names(core):
    base = core.path("professions")
    return sorted(n for n in os.listdir(base) if os.path.isdir(os.path.join(base, n)))


def skill_names(core):
    base = core.path("skills")
    return sorted(n for n in os.listdir(base) if os.path.isfile(os.path.join(base, n, "SKILL.md")))


def manifest_workers(core):
    """Workers from MANIFEST.md front matter: {name: {profession, scope, status}}."""
    out = {}
    for m in re.finditer(r"^\s+- \{(.*)\}\s*$", core.read("MANIFEST.md"), re.M):
        entry = dict(p.split(":", 1) for p in m.group(1).split(",") if ":" in p)
        entry = {k.strip(): v.strip() for k, v in entry.items()}
        if "profession" in entry and "status" in entry and "file" in entry and "workers/" in entry["file"]:
            out[entry["name"]] = entry
    return out


@check("worker-professions", "structure")
def check_worker_professions(core):
    problems = []
    professions = set(profession_names(core))
    for prof in sorted(professions):
        for fname in ("PROFESSION.md", "SKILLS.md"):
            if not os.path.isfile(core.path("professions", prof, fname)):
                problems.append(f"profession '{prof}' lacks {fname}")
    for name in worker_names(core):
        fields = worker_fields(core, name)
        prof = norm(fields.get("profession", ""))
        if not prof:
            problems.append(f"worker '{name}' declares no profession")
        elif prof not in professions:
            problems.append(f"worker '{name}' names unknown profession '{prof}'")
    return problems


@check("profession-template-contract", "structure")
def check_profession_template_contract(core):
    problems = []
    templates = {
        "PROFESSION.template.md": (
            "Nature",
            "Runtime rule",
            "Boundary",
            "Core responsibility",
            "profession-routing.md",
            "worker-activation.md",
        ),
        "SKILLS.template.md": (
            "baseline skills",
            "Worker-specific additions",
            "university/skills/<skill>/SKILL.md",
        ),
    }
    for filename, terms in templates.items():
        path = core.path("templates", "profession", filename)
        if not os.path.isfile(path):
            problems.append(f"missing profession template '{filename}'")
            continue
        text = core.read("templates", "profession", filename)
        for term in terms:
            if term not in text:
                problems.append(f"profession template '{filename}' lacks '{term}'")
    return problems


@check("faculty-structure", "structure")
def check_faculty_structure(core):
    problems = []
    base = core.path("faculties")
    for name in sorted(os.listdir(base)):
        path = os.path.join(base, name)
        if not os.path.isdir(path):
            continue
        for filename in ("FACULTY.md", "STAFF.md"):
            if not os.path.isfile(os.path.join(path, filename)):
                problems.append(f"faculty '{name}' lacks {filename}")
    return problems


@check("faculty-template-contract", "structure")
def check_faculty_template_contract(core):
    problems = []
    templates = {
        "FACULTY.template.md": (
            "status:",
            "domain:",
            "staff index:",
            "## Scope",
            "canonical Worker records",
        ),
        "STAFF.template.md": (
            "Discovery index only",
            "| Worker | Profession | Appointment | Status | Worker file |",
            "canonical appointment data",
        ),
    }
    for filename, terms in templates.items():
        path = core.path("templates", "faculty", filename)
        if not os.path.isfile(path):
            problems.append(f"missing faculty template '{filename}'")
            continue
        text = core.read("templates", "faculty", filename)
        for term in terms:
            if term not in text:
                problems.append(f"faculty template '{filename}' lacks '{term}'")
    return problems


@check("course-structure", "structure")
def check_course_structure(core):
    problems = []
    base = core.path("courses")
    for name in sorted(os.listdir(base)):
        path = os.path.join(base, name)
        if not os.path.isdir(path):
            continue
        if not os.path.isfile(os.path.join(path, "COURSE.md")):
            problems.append(f"course '{name}' lacks COURSE.md")
        modules = os.path.join(path, "modules")
        if not os.path.isdir(modules):
            continue
        for module in sorted(os.listdir(modules)):
            module_path = os.path.join(modules, module)
            if os.path.isdir(module_path) and not os.path.isfile(
                os.path.join(module_path, "MODULE.md")
            ):
                problems.append(f"course '{name}' module '{module}' lacks MODULE.md")
    return problems


@check("course-template-contract", "structure")
def check_course_template_contract(core):
    problems = []
    templates = {
        "COURSE.template.md": (
            "faculty:",
            "owner:",
            "## Course purpose",
            "## Module framework",
            "## Delivery layers",
            "Course architecture and Student delivery state are separate",
        ),
        "MODULE.template.md": (
            "## Identity",
            "## Entry Contract",
            "## Exit Contract",
            "## Theme Framework",
            "## Delivery boundary",
            "Student-specific",
        ),
    }
    for filename, terms in templates.items():
        path = core.path("templates", "course", filename)
        if not os.path.isfile(path):
            problems.append(f"missing course template '{filename}'")
            continue
        text = core.read("templates", "course", filename)
        for term in terms:
            if term not in text:
                problems.append(f"course template '{filename}' lacks '{term}'")
    return problems


@check("schema-template-contract", "structure")
def check_schema_template_contract(core):
    import json

    problems = []
    path = core.path("templates", "schema", "SCHEMA.template.json")
    if not os.path.isfile(path):
        return ["missing schema template 'SCHEMA.template.json'"]
    text = core.read("templates", "schema", "SCHEMA.template.json")
    try:
        schema = json.loads(text)
    except json.JSONDecodeError as exc:
        return [f"schema template is not valid JSON: {exc.msg}"]
    for key in ("$schema", "$id", "title", "description", "type", "required", "properties"):
        if key not in schema:
            problems.append(f"schema template lacks '{key}'")
    if schema.get("$id") != "<schema-name>.schema.json":
        problems.append("schema template must keep the <schema-name> placeholder in $id")
    if schema.get("type") != "object":
        problems.append("schema template root type must be object")
    return problems


def skill_bullets(text):
    """Skill names from `- `skill`` bullets (first backtick token of each bullet)."""
    return [m.group(1) for m in re.finditer(r"^\s*[-*]\s+`([^`]+)`", text, re.M)]


VALID_CLASSES = {"learning", "administrative", "development", "technical"}


def front_matter(text):
    """Parse the small metadata subset used by Skill and workflow files."""
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        return {}
    data = {}
    key = None
    for raw in match.group(1).splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        item = re.match(r"^\s+-\s+\{(.*)\}\s*$", raw)
        if item and key:
            parts = dict(p.split(":", 1) for p in item.group(1).split(",") if ":" in p)
            data.setdefault(key, []).append({k.strip(): v.strip() for k, v in parts.items()})
            continue
        scalar = re.match(r"^([a-z_]+):\s*(.*)$", raw)
        if scalar:
            key, value = scalar.groups()
            data[key] = [] if not value else value.strip()
    return data


def manifest_capabilities(core):
    """Return manifest class maps and declared workflow dependencies."""
    text = core.read("MANIFEST.md")
    skills = {}
    workflows = {}
    skill_section = re.search(r"^skills:\n(.*?)(?=^workflows:\n)", text, re.M | re.S)
    if skill_section:
        for m in re.finditer(
            r"^\s+- \{name: ([a-z0-9-]+), class: ([a-z]+)\}",
            skill_section.group(1),
            re.M,
        ):
            skills[m.group(1)] = m.group(2)
    in_workflows = False
    for line in text.splitlines():
        if line == "workflows:":
            in_workflows = True
            continue
        if in_workflows and line and not line.startswith(" "):
            in_workflows = False
        if in_workflows:
            m = re.match(r"^\s+- \{name: ([a-z0-9-]+), class: ([a-z]+)\}", line)
            if m:
                workflows[m.group(1)] = m.group(2)
    dependencies = []
    in_dependencies = False
    for line in text.splitlines():
        if line == "dependencies:":
            in_dependencies = True
            continue
        if in_dependencies and line and not line.startswith(" "):
            in_dependencies = False
        if in_dependencies:
            m = re.match(
                r"^\s+- \{workflow: ([a-z0-9-]+), kind: (skill|workflow), name: ([a-z0-9-]+)\}",
                line,
            )
            if m:
                dependencies.append(
                    {"workflow": m.group(1), "kind": m.group(2), "name": m.group(3)}
                )
    return skills, workflows, dependencies


@check("capability-metadata", "contract")
def check_capability_metadata(core):
    problems = []
    manifest_skills, manifest_workflows, manifest_deps = manifest_capabilities(core)
    for name, expected in manifest_skills.items():
        metadata = front_matter(core.read("skills", name, "SKILL.md"))
        actual = metadata.get("class")
        if actual not in VALID_CLASSES:
            problems.append(f"skills/{name}/SKILL.md: invalid or missing class '{actual}'")
        elif actual != expected:
            problems.append(f"skills/{name}/SKILL.md: class '{actual}' differs from manifest '{expected}'")
    for name, expected in manifest_workflows.items():
        metadata = front_matter(core.read("workflows", f"{name}.md"))
        actual = metadata.get("class")
        if actual not in VALID_CLASSES:
            problems.append(f"workflows/{name}.md: invalid or missing class '{actual}'")
        elif actual != expected:
            problems.append(f"workflows/{name}.md: class '{actual}' differs from manifest '{expected}'")
        declared = {
            (item.get("kind"), item.get("name"))
            for item in metadata.get("dependencies", [])
            if isinstance(item, dict)
        }
        expected_deps = {
            (item["kind"], item["name"])
            for item in manifest_deps
            if item["workflow"] == name
        }
        if declared != expected_deps:
            problems.append(
                f"workflows/{name}.md: dependencies differ from manifest "
                f"(file={sorted(declared)}, manifest={sorted(expected_deps)})"
            )
    return problems


@check("dependency-reachability", "contract")
def check_dependency_reachability(core):
    problems = []
    skills, workflows, dependencies = manifest_capabilities(core)
    known = {"skill": skills, "workflow": workflows}
    graph = {name: [] for name in workflows}
    for item in dependencies:
        source = item["workflow"]
        target = item["name"]
        if source not in workflows:
            problems.append(f"dependency source workflow '{source}' does not exist")
            continue
        if target not in known[item["kind"]]:
            problems.append(f"dependency target {item['kind']} '{target}' does not exist")
            continue
        source_class = workflows[source]
        target_class = known[item["kind"]][target]
        if source_class == "learning" and target_class in {"administrative", "development"}:
            problems.append(
                f"learning workflow '{source}' reaches forbidden {target_class} '{target}'"
            )
        if source_class == "learning" and target_class == "technical":
            problems.append(
                f"learning workflow '{source}' reaches unbounded technical '{target}'"
            )
        if item["kind"] == "workflow":
            graph[source].append(target)

    def visit(node, stack):
        if node in stack:
            return [f"dependency cycle: {' -> '.join(stack + [node])}"]
        failures = []
        for child in graph[node]:
            failures += visit(child, stack + [node])
        return failures

    for workflow in graph:
        problems += visit(workflow, [])
    return sorted(set(problems))


@check("correction-contract", "contract")
def check_correction_contract(core):
    problems = []
    policy = core.read("policies", "learning-material-review.md")
    profession = core.read("professions", "instructional-assistant", "PROFESSION.md")
    required_policy_terms = (
        "accepted",
        "deferred",
        "rejected",
        "15%",
        "issue",
        "Student",
        "named Worker",
    )
    for term in required_policy_terms:
        if term not in policy:
            problems.append(f"learning-material-review.md: missing correction contract term '{term}'")
    for term in ("bounded technical Skills", "approved correction", "policies/Skills/workflows/framework"):
        if term not in profession:
            problems.append(f"instructional-assistant/PROFESSION.md: missing '{term}'")
    return problems


@check("correction-fixtures", "contract")
def check_correction_fixtures(core):
    problems = []

    def percentage(before, after):
        return abs(after - before) / before * 100

    cases = {
        "growth": percentage(100, 115),
        "reduction": percentage(100, 85),
        "replacement": 15,
        "combined": max(percentage(100, 108), 20),
    }
    if cases["growth"] != 15 or cases["reduction"] != 15:
        problems.append("15% growth/reduction arithmetic fixture is invalid")
    if max(cases["combined"], cases["replacement"]) != 20:
        problems.append("larger text/learning impact fixture is invalid")
    if not all(cases[name] >= 15 for name in ("growth", "reduction", "replacement")):
        problems.append("threshold boundary fixture is invalid")
    protocol = core.read("protocols", "correction-governance.md")
    for term in ("ready-to-apply", "deferred", "blocked", "Profession", "named Worker identities"):
        if term not in protocol:
            problems.append(f"correction-governance.md: missing fixture term '{term}'")
    return problems


@check("correction-target-boundary", "contract")
def check_correction_target_boundary(core):
    problems = []
    text = core.read("skills", "approved-material-patch", "SKILL.md")
    for term in ("MATERIALS", "Policies", "Skills", "workflows", "service files", "explicit blocker"):
        if term not in text:
            problems.append(f"approved-material-patch: missing target boundary '{term}'")
    return problems


@check("host-profile-contract", "contract")
def check_host_profile_contract(core):
    problems = []
    text = core.read("protocols", "host-conformance.md") + "\n" + core.read(
        "protocols", "host-prompt-assembly.md"
    )
    for term in ("learning", "development", "technical", "CLI", "Worker", "pinned"):
        if term not in text:
            problems.append(f"host contract: missing profile term '{term}'")
    return problems


@check("skills-exist", "structure")
def check_skills_exist(core):
    problems = []
    known = set(skill_names(core))
    for prof in profession_names(core):
        rel = f"professions/{prof}/SKILLS.md"
        for skill in skill_bullets(core.read("professions", prof, "SKILLS.md")):
            if skill not in known:
                problems.append(f"{rel}: skill '{skill}' does not exist")
    for name in worker_names(core):
        text = core.read("workers", name, "WORKER.md")
        m = re.search(r"^## Additional worker skills\s*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
        for skill in skill_bullets(m.group(1)) if m else []:
            if skill not in known:
                problems.append(f"workers/{name}/WORKER.md: skill '{skill}' does not exist")
    return problems


@check("backtick-refs", "structure")
def check_backtick_refs(core):
    """Backticked .md/.json paths, `skills/NAME` and `university-NAME` in workflows, policies, protocols."""
    problems = []
    known_skills = set(skill_names(core))
    basenames = {}
    for rel in core.files("", ".md"):
        basenames.setdefault(os.path.basename(rel), []).append(rel)
    for rel in core.files("schemas", ".json"):
        basenames.setdefault(os.path.basename(rel), []).append(rel)
    for sub in ("workflows", "policies", "protocols"):
        for rel in core.files(sub):
            here = os.path.dirname(rel)
            for token in BACKTICK.findall(core.read(rel)):
                if re.search(r"[\s*<>{}]|\.\.\.", token):
                    continue
                if token.startswith(PRIVATE_SIDE[0]) or token in PRIVATE_SIDE:
                    continue
                t = token[len("university/"):] if token.startswith("university/") else token
                m = re.fullmatch(r"skills/([a-z0-9-]+)/?", t)
                if m and m.group(1) not in known_skills:
                    problems.append(f"{rel}: skill path `{token}` does not exist")
                    continue
                m = re.fullmatch(r"university-([a-z0-9-]+)", token)
                if m and m.group(1) not in known_skills:
                    problems.append(f"{rel}: skill `{token}` does not exist")
                    continue
                if not re.search(r"\.(md|json)$", t):
                    continue
                candidates = [os.path.join(here, t), t]
                if any(os.path.isfile(core.path(c)) for c in candidates):
                    continue
                if "/" not in t and t in basenames:
                    continue
                problems.append(f"{rel}: reference `{token}` does not resolve")
    return problems


def index_workers(core, rel):
    """Workers from a staff table: {name: (profession slug, status)}."""
    out = {}
    for cells in table_rows(core.read(rel)):
        if len(cells) >= 5 and cells[0]:
            status = cells[-2].lower()
            out[cells[0].lower()] = (norm(cells[1]), status)
    return out


@check("staff-consistency", "structure")
def check_staff_consistency(core):
    problems = []
    truth = {n: (norm(worker_fields(core, n).get("profession", "")), worker_fields(core, n).get("status", "").lower())
             for n in worker_names(core)}
    views = {"MANIFEST.md": {n: (e["profession"], e["status"].lower()) for n, e in manifest_workers(core).items()},
             "staff/REGISTRY.md": index_workers(core, "staff/REGISTRY.md")}
    faculty_members = {}
    for rel in core.files("faculties", "STAFF.md"):
        view = index_workers(core, rel)
        views[rel] = view
        faculty_members.update({n: rel for n in view})
    for label, view in views.items():
        for name, value in view.items():
            if name not in truth:
                problems.append(f"{label}: lists '{name}' but workers/{name}/WORKER.md is missing")
            elif value != truth[name]:
                problems.append(f"{label}: '{name}' is {value}, WORKER.md says {truth[name]}")
    for label in ("MANIFEST.md", "staff/REGISTRY.md"):
        for name in sorted(set(truth) - set(views[label])):
            problems.append(f"{label}: missing worker '{name}'")
    for name in sorted(truth):
        fac = worker_fields(core, name).get("scope", "")
        if fac.lower().endswith("faculty") and name not in faculty_members:
            problems.append(f"worker '{name}' has Faculty scope '{fac}' but appears in no Faculty STAFF.md")
    return problems


@check("routing-coverage", "structure")
def check_routing_coverage(core):
    problems = []
    text = core.read("protocols", "profession-routing.md")
    routed = set()
    for cells in table_rows(text):
        if len(cells) >= 2:
            routed.add(norm(cells[1]))
    active = {e["profession"] for e in manifest_workers(core).values() if e["status"] == "active"}
    professions = set(profession_names(core))
    for prof in sorted(routed - professions):
        problems.append(f"profession-routing.md routes to unknown profession '{prof}'")
    for prof in sorted(professions - routed):
        problems.append(f"profession '{prof}' has no row in the profession-routing.md table")
    for prof in sorted(routed & professions):
        if prof not in active and not re.search(rf"no active {re.escape(prof.replace('-', ' '))}", text, re.I):
            problems.append(f"profession '{prof}' is routed but has no active Worker and the gap is not stated")
    return problems


CREDENTIAL_PATTERNS = [
    ("private key block", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("AWS access key id", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("GitHub token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b")),
    ("API-style secret key", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b")),
    ("Slack token", re.compile(r"\bxox[abposr]-[A-Za-z0-9-]{10,}")),
    ("assigned credential", re.compile(r"(?i)\b(password|passwd|api[_-]?key|secret|access[_-]?token)\b\s*[:=]\s*[\"']?[A-Za-z0-9/+_.-]{8,}")),
    ("URL with credentials", re.compile(r"\b[a-z][a-z0-9+.-]*://[^\s/:@]+:[^\s/@]+@")),
]
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}")
MACHINE_PATH = re.compile(r"(?<![\w.~])(/home/[^\s`]+|/Users/[^\s`]+|/root/[^\s`]+|[A-Za-z]:\\(Users|Documents)\\)")
LANGUAGES = "ukrainian|english|polish|german|french|spanish|russian|italian"
SESSION_STATEMENTS = re.compile(
    rf"(?i)\b((detected|selected|current|session) (dialogue )?language (is|was)|"
    rf"this session (uses|is in)) (ukrainian|english|polish|german|french|spanish|russian|italian)\b"
)
SKIP_TEXT_DIRS = ("planning/completed",)


def public_text_files(core, suffixes=(".md", ".json")):
    for suffix in suffixes:
        for rel in core.files("", suffix):
            rel = core.relative(rel)
            if not rel.startswith(SKIP_TEXT_DIRS):
                yield rel


def scan(core, pattern_for_line, ignore_planning_self=True):
    problems = []
    for rel in public_text_files(core):
        for n, line in enumerate(core.read(rel).splitlines(), 1):
            what = pattern_for_line(line)
            if what:
                problems.append(f"{rel}:{n}: {what}")
    return problems


@check("no-emails", "data")
def check_no_emails(core):
    return scan(core, lambda line: "email address" if EMAIL.search(line) else None)


@check("no-machine-paths", "data")
def check_no_machine_paths(core):
    return scan(core, lambda line: "absolute machine path" if MACHINE_PATH.search(line) else None)


@check("no-credentials", "data")
def check_no_credentials(core):
    def find(line):
        for label, pattern in CREDENTIAL_PATTERNS:
            if pattern.search(line):
                return label
        return None

    return scan(core, find)


@check("no-session-statements", "data")
def check_no_session_statements(core):
    problems = []
    for sub in ("policies", "protocols", "workflows", "professions", "skills", "workers"):
        for rel in core.files(sub):
            for n, line in enumerate(core.read(rel).splitlines(), 1):
                if SESSION_STATEMENTS.search(line):
                    problems.append(f"{rel}:{n}: session-specific statement")
    return problems


def private_terms(root):
    """Student ids and names from the local private `students/`, read at run time, never stored.

    Returns None when `students/` is absent. Terms come from `students/<id>/STUDENT.md`
    directory ids and from `- Name — path` lines of the Student registry.
    """
    base = os.path.join(root, "students")
    if not os.path.isdir(base):
        return None
    terms = set()
    for name in os.listdir(base):
        if os.path.isfile(os.path.join(base, name, "STUDENT.md")):
            terms.add(name)
    registry = os.path.join(base, "registry", "REGISTRY.md")
    if os.path.isfile(registry):
        with open(registry, encoding="utf-8") as fh:
            for line in fh:
                m = re.match(r"^\s*[-*]\s+([^—–\n`]+?)\s+[—–-]\s+`?students/", line)
                if m:
                    terms.add(m.group(1))
    return {t for t in terms if len(t.strip()) >= 3}


@check("no-private-terms", "data")
def check_no_private_terms(core):
    terms = private_terms(core.root)
    if terms is None:
        print("   ℹ️  students/ not found: private-term check skipped")
        return []
    if not terms:
        print("   ℹ️  students/ has no registered Students: private-term check has nothing to look for")
        return []
    pattern = re.compile(r"(?<!\w)(" + "|".join(re.escape(t) for t in sorted(terms)) + r")(?!\w)", re.I)
    problems = []
    for rel in public_text_files(core):
        for n, line in enumerate(core.read(rel).splitlines(), 1):
            if pattern.search(line):
                problems.append(f"{rel}:{n}: private Student identifier or name (term not shown)")
    return problems


def section(text, heading):
    """Body of the `## heading` section (up to the next `## `), or ''."""
    m = re.search(rf"^## {re.escape(heading)}\s*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    return m.group(1) if m else ""


def contract_operations(core):
    """Operation names (first column of the Operations table) of student-state-contract.md."""
    text = section(core.read("protocols", "student-state-contract.md"), "Operations")
    return [m.group(1) for cells in table_rows(text) for m in [re.match(r"^`([^`]+)`", cells[0])] if m]


@check("state-authority", "contract")
def check_state_authority(core):
    """Operations table, Authority list and policies/student-state-authority.md agree."""
    problems = []
    contract = core.read("protocols", "student-state-contract.md")
    ops = contract_operations(core)
    authority = section(contract, "Authority")
    professions = set(profession_names(core))
    workflows = {os.path.splitext(os.path.basename(r))[0] for r in core.files("workflows")}
    listed = set(re.findall(r"`([a-z-]+)`", authority)) - workflows
    for op in ops:
        if op != "read" and op not in listed:
            problems.append(f"operation '{op}' has no owner in the Authority list")
    for op in sorted(listed - set(ops)):
        problems.append(f"Authority list names '{op}', which is not an operation of the contract")
    contract_roles = set()
    for line in authority.splitlines():
        m = re.match(r"^- ([A-Z][A-Za-z ,]+?) —", line)
        if not m:
            continue
        for role in re.split(r",| and ", m.group(1)):
            if role.strip():
                slug = norm(role)
                contract_roles.add(slug)
                if slug not in professions:
                    problems.append(f"Authority list names unknown profession '{role.strip()}'")
    policy = section(core.read("policies", "student-state-authority.md"), "Write")
    policy_roles = {norm(m.group(1)) for m in re.finditer(r"^- ([A-Z][a-z]+(?: [A-Z][a-z]+)?)(?: may|,| and)", policy, re.M)}
    policy_roles |= {norm(r) for m in re.finditer(r"^- ([A-Z][A-Za-z ,]+?) may", policy, re.M) for r in re.split(r",| and ", m.group(1)) if r.strip()}
    for role in sorted(policy_roles - contract_roles):
        problems.append(f"policies/student-state-authority.md grants writes to '{role}', absent from the contract Authority list")
    for role in sorted(contract_roles - policy_roles):
        problems.append(f"contract Authority list names '{role}', absent from policies/student-state-authority.md")
    return problems


def stem_hits(field, text):
    """True when every underscore-separated part of `field` (as a stem) occurs in `text`."""
    low = text.lower()
    return all(part[: max(3, len(part) - 2)] in low for part in field.split("_"))


@check("state-schema", "contract")
def check_state_schema(core):
    """Schema entities and field names are described in the contract Entities table."""
    import json

    problems = []
    schema = json.loads(core.read("schemas", "student-state.schema.json"))
    rows = {re.sub(r"[^a-z]", "", c[0].lower()): c for c in table_rows(section(core.read("protocols", "student-state-contract.md"), "Entities"))}
    defs = schema.get("$defs", {})
    for entity in ("student", "enrollment", "plan", "evidence", "decision", "note"):
        if entity not in defs:
            problems.append(f"schema has no definition for contract entity '{entity}'")
            continue
        if entity not in rows:
            problems.append(f"schema entity '{entity}' is absent from the contract Entities table")
            continue
        row = " ".join(rows[entity])
        for field in defs[entity].get("properties", {}):
            if field in ("id", "recorded", "text"):
                continue
            if not stem_hits(field, row + " " + core.read("protocols", "student-state-contract.md")):
                problems.append(f"schema field '{entity}.{field}' is not described in the contract")
    for name in rows:
        if name != "registry" and name not in defs:
            problems.append(f"contract entity '{name}' has no schema definition")
    return problems


STATE_OP_PREFIXES = ("record-", "append-", "update-", "complete-", "add-", "initialize-")


@check("workflow-skills", "contract")
def check_workflow_skills(core):
    """Backticked kebab-case names in workflows are Skills, contract operations, or known files."""
    problems = []
    known = set(skill_names(core)) | set(contract_operations(core))
    stems = {os.path.splitext(os.path.basename(r))[0] for r in core.files("", ".md")}
    for rel in core.files("workflows"):
        for token in BACKTICK.findall(core.read(rel)):
            if not re.fullmatch(r"[a-z]+(-[a-z]+)+", token):
                continue
            if token.startswith(STATE_OP_PREFIXES) and token not in known:
                problems.append(f"{rel}: `{token}` looks like a state operation or Skill but exists as neither")
            elif token not in known and token not in stems and token not in ("single-choice",):
                if re.search(rf"(?i)skill[^\n]*`{re.escape(token)}`|`{re.escape(token)}`[^\n]*skill", core.read(rel)):
                    problems.append(f"{rel}: `{token}` is named as a Skill but does not exist")
    return problems


@check("skills-reachable", "contract")
def check_skills_reachable(core):
    """Every `learning` Skill is in some Profession baseline or Worker addition."""
    problems = []
    used = set()
    for prof in profession_names(core):
        used |= set(skill_bullets(core.read("professions", prof, "SKILLS.md")))
    for name in worker_names(core):
        m = re.search(r"^## Additional worker skills\s*\n(.*?)(?=^## |\Z)", core.read("workers", name, "WORKER.md"), re.M | re.S)
        if m:
            used |= set(skill_bullets(m.group(1)))
    skills, _workflows, _dependencies = manifest_capabilities(core)
    for name, cls in skills.items():
        if cls == "learning" and name not in used:
            problems.append(f"learning Skill '{name}' is in no Profession baseline or Worker addition")
    return problems


def run(core, names):
    failed = 0
    for name in names:
        group, fn = CHECKS[name]
        problems = fn(core)
        if problems:
            failed += 1
            print(f"❌ {name} [{group}]")
            for problem in problems:
                print(f"   - {problem}")
        else:
            print(f"✅ {name} [{group}]")
    total = len(names)
    print(f"{total - failed}/{total} checks passed")
    return 1 if failed else 0


def main(argv):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("names", nargs="*", help="check names (default: all)")
    parser.add_argument("--list", action="store_true", help="list check names and exit")
    parser.add_argument("--root", default=REPO, help="directory containing university/")
    args = parser.parse_args(argv)

    if args.list:
        for name, (group, _fn) in CHECKS.items():
            print(f"{name}\t{group}")
        return 0
    unknown = [n for n in args.names if n not in CHECKS]
    if unknown:
        print(f"unknown check(s): {', '.join(unknown)}", file=sys.stderr)
        return 2
    if not os.path.isdir(os.path.join(args.root, "university")):
        print(f"no university/ under {args.root}", file=sys.stderr)
        return 2
    if not CHECKS:
        print("no checks registered", file=sys.stderr)
        return 2
    return run(Core(args.root), args.names or list(CHECKS))


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
