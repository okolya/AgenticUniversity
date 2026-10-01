---
manifest_version: 2
# GENERATED from this template and canonical core records.

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
  - {name: emma, profession: learning-analyst, scope: language, status: active, file: workers/emma/WORKER.md}
  - {name: ferdinand, profession: lecturer, scope: language, status: active, file: workers/ferdinand/WORKER.md}
  - {name: livia, profession: instructional-assistant, scope: university, status: active, file: workers/livia/WORKER.md}
  - {name: luke, profession: dean, scope: engineering, status: active, file: workers/luke/WORKER.md}
  - {name: maria, profession: translator, scope: language, status: active, file: workers/maria/WORKER.md}
  - {name: oleg, profession: examiner, scope: language, status: active, file: workers/oleg/WORKER.md}
  - {name: ollie, profession: examiner, scope: engineering, status: active, file: workers/ollie/WORKER.md}
  - {name: petro, profession: rector, scope: university, status: active, file: workers/petro/WORKER.md}
  - {name: sara, profession: laboratory-specialist, scope: engineering, status: active, file: workers/sara/WORKER.md}
  - {name: simeon, profession: laboratory-specialist, scope: language, status: active, file: workers/simeon/WORKER.md}
  - {name: tim, profession: learning-analyst, scope: engineering, status: active, file: workers/tim/WORKER.md}
  - {name: viktor, profession: teacher, scope: language, status: active, file: workers/viktor/WORKER.md}
  - {name: vlad, profession: teacher, scope: engineering, status: active, file: workers/vlad/WORKER.md}

skills:
  - {name: appoint-worker, class: administrative}
  - {name: approved-material-patch, class: technical}
  - {name: ask-question, class: learning}
  - {name: author-material, class: development}
  - {name: build-assessment, class: learning}
  - {name: check-prerequisites, class: learning}
  - {name: correction-checks, class: technical}
  - {name: correction-git, class: technical}
  - {name: create-enrollment, class: learning}
  - {name: create-lab, class: learning}
  - {name: evaluate-answer, class: learning}
  - {name: evaluate-exercise, class: learning}
  - {name: generate-exercise, class: learning}
  - {name: inspect-student-state, class: learning}
  - {name: issue-management, class: technical}
  - {name: localize-material, class: learning}
  - {name: module-planning, class: development}
  - {name: rector-startup, class: learning}
  - {name: register-worker, class: administrative}
  - {name: research-materials, class: development}
  - {name: review-learning-material, class: learning}
  - {name: run-diagnostic, class: learning}
  - {name: run-quiz, class: learning}
  - {name: session-bootstrap, class: development}
  - {name: update-evidence, class: learning}

workflows:
  - {name: course-design, class: development}
  - {name: course-entry, class: learning}
  - {name: faculty-entry, class: learning}
  - {name: learning-assessment, class: learning}
  - {name: learning-material-review, class: learning}
  - {name: learning-plan, class: development}
  - {name: lesson-preparation, class: development}
  - {name: module-design, class: development}
  - {name: module-entry, class: learning}
  - {name: module-exit, class: learning}
  - {name: retention-assessment, class: learning}
  - {name: student-initialization, class: learning}
  - {name: theme-assessment, class: learning}
  - {name: theme-design, class: development}
  - {name: university-start, class: learning}
  - {name: worker-appointment, class: administrative}

dependencies:
  - {workflow: course-design, kind: skill, name: research-materials}
  - {workflow: course-entry, kind: skill, name: update-evidence}
  - {workflow: faculty-entry, kind: skill, name: create-enrollment}
  - {workflow: learning-material-review, kind: skill, name: review-learning-material}
  - {workflow: lesson-preparation, kind: skill, name: research-materials}
  - {workflow: lesson-preparation, kind: skill, name: author-material}
  - {workflow: module-design, kind: skill, name: module-planning}
  - {workflow: module-entry, kind: skill, name: check-prerequisites}
  - {workflow: theme-assessment, kind: skill, name: update-evidence}
  - {workflow: worker-appointment, kind: skill, name: appoint-worker}
  - {workflow: worker-appointment, kind: skill, name: register-worker}

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
  - correction-governance
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
  - german-between-b1-and-b2

schemas:
  - interaction-response
  - student-state
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
