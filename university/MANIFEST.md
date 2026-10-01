---
manifest_version: 1

# Entry points a host uses to start a session
startup_profession: rector
startup_skill: rector-startup
startup_workflow: university-start

professions:
  - dean
  - examiner
  - instructional-assistant
  - laboratory-specialist
  - learning-analyst
  - lecturer
  - rector
  - teacher
  - translator

workers:
  - {name: adam, profession: lecturer, scope: engineering, status: active, file: workers/adam/WORKER.md}
  - {name: bob, profession: dean, scope: language, status: active, file: workers/bob/WORKER.md}
  - {name: livia, profession: instructional-assistant, scope: university, status: active, file: workers/livia/WORKER.md}
  - {name: luke, profession: dean, scope: engineering, status: active, file: workers/luke/WORKER.md}
  - {name: maria, profession: translator, scope: university, status: active, file: workers/maria/WORKER.md}
  - {name: ollie, profession: examiner, scope: engineering, status: active, file: workers/ollie/WORKER.md}
  - {name: petro, profession: rector, scope: university, status: active, file: workers/petro/WORKER.md}
  - {name: sara, profession: laboratory-specialist, scope: engineering, status: active, file: workers/sara/WORKER.md}
  - {name: tim, profession: learning-analyst, scope: engineering, status: active, file: workers/tim/WORKER.md}
  - {name: vlad, profession: teacher, scope: engineering, status: active, file: workers/vlad/WORKER.md}

skills:
  - {name: appoint-worker, class: administrative}
  - {name: ask-question, class: learning}
  - {name: author-material, class: learning}
  - {name: build-assessment, class: learning}
  - {name: check-prerequisites, class: learning}
  - {name: create-enrollment, class: learning}
  - {name: create-lab, class: learning}
  - {name: evaluate-answer, class: learning}
  - {name: evaluate-exercise, class: learning}
  - {name: generate-exercise, class: learning}
  - {name: inspect-student-state, class: learning}
  - {name: localize-material, class: learning}
  - {name: module-planning, class: learning}
  - {name: rector-startup, class: learning}
  - {name: register-worker, class: administrative}
  - {name: research-materials, class: learning}
  - {name: review-learning-material, class: learning}
  - {name: run-diagnostic, class: learning}
  - {name: run-quiz, class: learning}
  - {name: session-bootstrap, class: maintenance}
  - {name: update-evidence, class: learning}

workflows:
  - course-design
  - course-entry
  - faculty-entry
  - learning-assessment
  - learning-material-review
  - learning-plan
  - lesson-preparation
  - module-design
  - module-entry
  - module-exit
  - retention-assessment
  - student-initialization
  - theme-assessment
  - theme-design
  - university-start
  - worker-appointment

policies:
  - academic-authority
  - ai-usage
  - assessment-independence
  - context-loading
  - curriculum-authority
  - dialogue-language
  - interaction-format
  - knowledge-and-state-ownership
  - learning-content-authority
  - learning-material-review
  - module-contracts
  - module-outcome-strategy
  - no-invention
  - practical-work
  - public-private-boundary
  - runtime-command-whitelist
  - runtime-portability
  - student-state-authority
  - worker-appointment

protocols:
  - artifact-verification
  - assessment-contracts
  - host-conformance
  - host-prompt-assembly
  - learning-interaction-contracts
  - profession-routing
  - student-state-contract
  - theme-record-contracts
  - worker-activation
  - workspace-composition

faculties:
  - engineering
  - language

courses:
  - ai-engineering

schemas:
  - student-state
---

# University Manifest

Single entry point for hosts that run this University (the CLI workspace or a
separate host such as an online chat bot). A host reads this file instead of
scanning the tree. All names resolve to core-relative paths:

| List | Location |
|---|---|
| `professions` | `professions/<name>/PROFESSION.md` and `SKILLS.md` |
| `workers` | `file` field (appointment record; canonical) |
| `skills` | `skills/<name>/SKILL.md` |
| `workflows`, `policies`, `protocols` | `<list>/<name>.md` |
| `faculties` | `faculties/<name>/FACULTY.md` |
| `courses` | `courses/<name>/COURSE.md` |
| `schemas` | `schemas/<name>.schema.json` (JSON Schema) and `schemas/<name>.example.json` (synthetic example) |

## Skill classes

- `learning` — used by Workers in Student sessions (including Student-state
  operations bounded by `protocols/student-state-contract.md`).
- `administrative` — staffing operations; never offered in a Student session.
- `maintenance` — University development and workspace tooling; CLI and
  maintainer only.

A host exposes only `learning` Skills in Student sessions.

## Versioning

There is no separate core version number yet. A host pins the core by Git tag
or commit.

## Consistency

The manifest must list exactly what exists. `make check-manifest` verifies
it; run it after adding or removing a Profession, Worker, Skill, Workflow,
Policy, Protocol, Faculty, or Course. Workers' records remain canonical;
`staff/REGISTRY.md` is a discovery index for the CLI.
