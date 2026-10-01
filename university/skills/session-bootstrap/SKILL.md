---
name: session-bootstrap
description: Bootstrap work in the Agentic University core or a composed host by loading the smallest required context, routing to the owning repository boundary, and handing off to the responsible Profession before any edits or commands.
class: development
---
# Session bootstrap

Establish context at the very start of a session or task without spending the
context budget. This Skill is an orchestration aid: it routes work, it never
owns an academic decision, appoints a Worker, or reads private Student state.

## Use when

- A session begins and the request does not name an active academic workflow.
- The target repository, Profession, or Worker is unclear.
- The user says "bootstrap", "start", or "init" for the project.

## Procedure

### 1. Minimal startup and routing

1. Confirm `pwd` and resolve the core boundary. In standalone mode,
   `AGENTS.md` and `university/` are in the current repository. In a composed
   workspace, use `university-core/AGENTS.md` and
   `university-core/university/`; read the host/workspace `AGENTS.md` once per
   session when it exists. The canonical private Student path is the
   core-relative `students/` directory; it may be absent until a Student
   workspace is initialized.
2. Classify the task and pick the ownership boundary:
   - host root files and `scripts/` — orchestration, runtime installation, Git;
   - resolved core `university/` — public academic knowledge, policies,
     workflows, Skills, Professions, Workers;
   - core-relative `students/` — private Student state (only the selected
     Student; the directory may be absent for public-only work).
3. Run `git rev-parse --show-toplevel` inside the chosen boundary before any
   edit or Git command.
4. Check only the chosen boundary's runtime state read-only with
   `git status --short`. Inspect provider runtime links only when the current
   task needs a provider adapter or the host reports an initialization
   problem; do not scan `.claude/`, `.cursor/`, or other runtime trees merely
   to establish session context. If required runtime links are missing or
   stale, propose the host's init command; do not run it silently.
5. Use the canonical core `university/skills/inspect-student-state/SKILL.md`
   contract; provider-home Skill copies may be used only as installed runtime
   wiring and never as a replacement for the core source. Require a stable
   authenticated Student ID from the host. Resolve it against the registry,
   not from the current message, a remembered name, or filesystem discovery.
   Inspect the minimum permitted Student state through the
   `inspect-student-state` Skill and the Student-state contract before deciding
   whether a workflow exists. The inspection must return one of:
   `missing`, `unavailable`, `available/no-active-workflow`, or
   `available/active-workflow`.
   In a CLI or composed workspace, resolve the authenticated Student through
   `students/registry/REGISTRY.md` first, then read only the exact
   `students/<id>/STUDENT.md` path recorded there. The registry is the only
   Student discovery surface: never guess an ID, glob `students/**`, or search
   for alternative Student stores.
   The absence of a workflow name in the current message does not mean that
   the Student has no active workflow. If the authenticated Student state is
   missing or unavailable, stop startup routing and report that the host must
   initialize or provision the private Student state first; missing state is
   not evidence that no workflow exists. In a CLI host, run the idempotent
   `scripts/ensure-student-homeworks.sh <student-id>` helper only when the
   selected workflow needs a homework/artifact directory and that directory
   is absent; do not create Student workspace directories during public-only
   startup.
6. If the inspection result is `missing` or `unavailable`, stop and report the
   initialization or access blocker. Never interpret either state as an empty
   Student state. If the available Student state contains an active enrollment, plan, current
   Lesson,
   or another explicit academic handoff, treat that as the active workflow.
   Resume it and resolve its responsible Profession through
   `university/protocols/profession-routing.md`, then the Worker through
   `university/protocols/worker-activation.md`. Do not start Rector
   orientation or offer Faculty selection in this case.
7. If, and only if, Student state is available and no active Student workflow
   is recorded, resolve the
   startup Profession and Worker and activate Rector for the
   `university-start` workflow, then run `rector-startup`.
8. Resolve every repository-relative path from the verified boundary before
   reading it. In a composed workspace, do not prepend the host root to a
   path that is already relative to `university-core/`; report a missing file
   only after checking the canonical core-relative path.
9. Load one workflow or policy only if the task needs it, plus the exact files
   the task touches and their nearest governing README.
10. Stop loading context as soon as the task is actionable. Use exact known
    paths or narrowly scoped patterns; never perform a recursive tree scan,
    enumerate hidden VCS/runtime files, or load an unused adapter, Skill,
    workflow, or manifest section.

### 2. Onboarding query template

If routing information is missing, ask using this structure:

```text
Boundary: <host-root | university | students>
Profession/Worker: <profession — worker>
Workflow: <workflow or none>
Read only: <exact optional docs>
Task: <change>
Validation: <make target or check to propose later>
```

### 3. Reading order (only when a deep dive is required)

1. `<core>/university/constitution/ONTOLOGY.md`
2. `<core>/university/constitution/RESPONSIBILITY-MATRIX.md`
3. `<core>/README.md`
4. `<core>/university/protocols/profession-routing.md`
5. `<core>/university/protocols/worker-activation.md`
6. The task's workflow and policy (`<core>/university/workflows/`,
   `<core>/university/policies/`)
7. `<core>/university/policies/interaction-format.md` and
   `<core>/university/policies/dialogue-language.md` before any Student-facing output

### 4. Output

Report briefly: verified boundary, runtime state, resolved Profession/Worker
(or "none assigned"), next action, and any verified unknowns.

## Boundaries

- Run no commands that change state before the context pass completes.
- Do not read `students/` beyond the selected Student; use
  `inspect-student-state` when private state is permitted.
- Do not invent Workers, Faculties, curricula, evidence, or Student state.
- Do not encode absolute machine paths in any produced artifact.
- Keep the startup context under roughly 30 KB.
