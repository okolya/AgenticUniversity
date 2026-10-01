---
manifest_version: 2
# GENERATED from this template and canonical core records.

# Entry points a host uses to start a session
startup_profession: {{STARTUP_PROFESSION}}
startup_skill: {{STARTUP_SKILL}}
startup_workflow: {{STARTUP_WORKFLOW}}

professions:
{{PROFESSIONS}}

workers:
{{WORKERS}}

skills:
{{SKILLS}}

workflows:
{{WORKFLOWS}}

dependencies:
{{DEPENDENCIES}}

policies:
{{POLICIES}}

protocols:
{{PROTOCOLS}}

faculties:
{{FACULTIES}}

courses:
{{COURSES}}

schemas:
{{SCHEMAS}}
---

# University Manifest

Single entry point for hosts that run this University. A host reads this
generated discovery index instead of scanning the tree. Canonical records
remain in the listed Profession, Worker, Skill, workflow, policy, protocol,
Faculty, Course, and schema paths.

| List | Location |
|---|---|
| `professions` | `professions/<name>/PROFESSION.md` and `SKILLS.md` |
| `workers` | canonical appointment record at the `file` path |
| `skills` | `skills/<name>/SKILL.md` |
| `workflows`, `policies`, `protocols` | corresponding core directories |
| `faculties` | `faculties/<name>/FACULTY.md` |
| `courses` | `courses/<name>/COURSE.md` |
| `schemas` | `schemas/<name>.schema.json` and its example |

## Skill classes

- `learning` — used by Workers in Student sessions.
- `administrative` — staffing operations; never offered in a Student session.
- `development` — University development and workspace tooling.
- `technical` — bounded technical operations under authorized Worker workflows.

A host exposes only `learning` Skills in Student sessions. The manifest is
generated from canonical records and must be regenerated when those records
change.

## Versioning

There is no separate core version number yet. A host pins the core by Git tag
or commit.

## Consistency

`make check-manifest` verifies generated output and filesystem membership.
The pre-commit hook regenerates and stages this discovery index before checks.
