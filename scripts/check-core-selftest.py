#!/usr/bin/env python3
"""Prove every core check can fail.

For each check in check-core.py this copies the core to a temporary directory,
first requires the clean copy to pass, then injects one deliberate defect and
requires the check to report a problem. A check without an injector fails the
self-test, so new checks cannot be added unproven. Standard library only; the
real repository is never modified.
"""
import importlib.util
import os
import re
import shutil
import sys
import tempfile

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("check_core", os.path.join(HERE, "check-core.py"))
cc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cc)

INJECTORS = {}


def defect(name):
    def register(fn):
        INJECTORS[name] = fn
        return fn

    return register


def edit(root, rel, fn):
    path = os.path.join(root, "university", rel)
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    new = fn(text)
    if new == text:
        raise RuntimeError(f"injector for {rel} changed nothing")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(new)


def append(root, rel, extra):
    edit(root, rel, lambda t: t + extra)


@defect("capability-metadata")
def _(root):
    edit(root, "skills/author-material/SKILL.md", lambda t: t.replace("class: development", "class: maintenance", 1))


@defect("dependency-reachability")
def _(root):
    edit(
        root,
        "MANIFEST.md",
        lambda t: t.replace(
            "dependencies:\n",
            "dependencies:\n  - {workflow: course-entry, kind: skill, name: author-material}\n",
            1,
        ),
    )


@defect("correction-contract")
def _(root):
    edit(
        root,
        "policies/learning-material-review.md",
        lambda t: t.replace("The Lecturer must explicitly", "The Lecturer may optionally", 1)
        .replace("15%", "ten percent"),
    )


@defect("correction-fixtures")
def _(root):
    edit(
        root,
        "protocols/correction-governance.md",
        lambda t: t.replace("ready-to-apply", "ready", 1),
    )


@defect("correction-target-boundary")
def _(root):
    edit(
        root,
        "skills/approved-material-patch/SKILL.md",
        lambda t: t.replace("service files", "runtime files", 1),
    )


@defect("host-profile-contract")
def _(root):
    edit(
        root,
        "protocols/host-conformance.md",
        lambda t: t.replace("pinned core copy", "core copy", 1),
    )


@defect("worker-professions")
def _(root):
    edit(root, "workers/adam/WORKER.md", lambda t: t.replace("- profession: Lecturer", "- profession: Wizard", 1))


@defect("profession-template-contract")
def _(root):
    os.remove(os.path.join(root, "university", "templates", "profession", "SKILLS.template.md"))


@defect("faculty-structure")
def _(root):
    os.remove(os.path.join(root, "university", "faculties", "language", "STAFF.md"))


@defect("faculty-template-contract")
def _(root):
    os.remove(os.path.join(root, "university", "templates", "faculty", "STAFF.template.md"))


@defect("course-structure")
def _(root):
    os.remove(os.path.join(root, "university", "courses", "ai-engineering", "modules", "module-01-python-ai-engineering", "MODULE.md"))


@defect("course-template-contract")
def _(root):
    os.remove(os.path.join(root, "university", "templates", "course", "MODULE.template.md"))


@defect("schema-template-contract")
def _(root):
    os.remove(os.path.join(root, "university", "templates", "schema", "SCHEMA.template.json"))


@defect("skills-exist")
def _(root):
    append(root, "professions/dean/SKILLS.md", "\n- `no-such-skill`\n")


@defect("backtick-refs")
def _(root):
    append(root, "workflows/course-entry.md", "\nSee `protocols/no-such-protocol.md`.\n")


@defect("staff-consistency")
def _(root):
    edit(root, "staff/REGISTRY.md", lambda t: t.replace("| Adam | Lecturer |", "| Adam | Teacher |", 1))


@defect("routing-coverage")
def _(root):
    edit(root, "protocols/profession-routing.md",
         lambda t: "\n".join(l for l in t.splitlines() if "| Translator |" not in l) + "\n")


@defect("no-emails")
def _(root):
    append(root, "README.md", "\nContact: someone@example.org\n")


@defect("no-machine-paths")
def _(root):
    append(root, "README.md", "\nSee /home/someone/project/file.txt\n")


@defect("no-credentials")
def _(root):
    append(root, "README.md", "\napi_key = abcd1234efgh5678\n")


@defect("no-session-statements")
def _(root):
    append(root, "policies/dialogue-language.md", "\nThe detected language is Ukrainian.\n")


@defect("no-private-terms")
def _(root):
    # A private Student exists only in the temporary copy; the term is never stored in the repository.
    os.makedirs(os.path.join(root, "students", "zzplanted"), exist_ok=True)
    with open(os.path.join(root, "students", "zzplanted", "STUDENT.md"), "w", encoding="utf-8") as fh:
        fh.write("# Student\n\nid: zzplanted\n")
    append(root, "README.md", "\nWorked example for zzplanted.\n")


@defect("state-authority")
def _(root):
    edit(root, "protocols/student-state-contract.md",
         lambda t: t.replace("- Dean and Rector — `add-note`", "- Dean and Rector — (removed)", 1))


@defect("state-schema")
def _(root):
    edit(root, "schemas/student-state.schema.json",
         lambda t: t.replace('"limitation"', '"zzunexplained_field"', 1))


@defect("workflow-skills")
def _(root):
    append(root, "workflows/learning-plan.md", "\nThe Dean uses the Skill `record-imaginary` here.\n")


@defect("skills-reachable")
def _(root):
    # Orphan a learning Skill: register it in the manifest without any Profession or Worker using it.
    edit(root, "MANIFEST.md",
         lambda t: t.replace("  - {name: appoint-worker,", "  - {name: zz-orphan, class: learning}\n  - {name: appoint-worker,", 1))


def main():
    missing = sorted(set(cc.CHECKS) - set(INJECTORS))
    stale = sorted(set(INJECTORS) - set(cc.CHECKS))
    failures = [f"check '{n}' has no injected defect" for n in missing]
    failures += [f"injector '{n}' matches no check" for n in stale]
    tmp_base = tempfile.mkdtemp(prefix="core-selftest-")
    try:
        for name in cc.CHECKS:
            if name not in INJECTORS:
                continue
            root = os.path.join(tmp_base, name)
            os.makedirs(root)
            shutil.copytree(os.path.join(cc.REPO, "university"), os.path.join(root, "university"))
            fn = cc.CHECKS[name][1]
            if fn(cc.Core(root)):
                failures.append(f"'{name}' fails on the clean copy; self-test cannot attribute a defect")
                continue
            INJECTORS[name](root)
            if fn(cc.Core(root)):
                print(f"✅ {name}: failed on injected defect")
            else:
                print(f"❌ {name}: did NOT fail on injected defect")
                failures.append(f"'{name}' did not detect its injected defect")
    finally:
        shutil.rmtree(tmp_base, ignore_errors=True)
    for f in failures:
        print(f"   - {f}")
    print(f"{len(cc.CHECKS) - len(failures)}/{len(cc.CHECKS)} checks proven" if not failures else "self-test FAILED")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
