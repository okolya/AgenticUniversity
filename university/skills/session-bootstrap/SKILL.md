---
name: session-bootstrap
description: Bootstrap work in the Agentic University workspace by loading the smallest required context, routing to the owning repository boundary, and handing off to the responsible Profession before any edits or commands.
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

1. Confirm `pwd` is the workspace root and that `AGENTS.md`, `university/`,
   and `students/` exist. Read root `AGENTS.md` once per session.
2. Classify the task and pick the ownership boundary:
   - root files and `scripts/` — orchestration, runtime installation, Git;
   - `university/` — public academic knowledge, policies, workflows, Skills,
     Professions, Workers;
   - `students/` — private Student state (only the selected Student).
3. Run `git rev-parse --show-toplevel` inside the chosen boundary before any
   edit or Git command.
4. Check runtime state read-only: `git status --short`, and whether
   `.claude/agents/` and `.claude/skills/` are populated. If runtime links are
   missing or stale, propose `make init`; do not run it silently.
5. Resolve the workflow and responsible Profession through
   `university/protocols/profession-routing.md`, then the Worker through
   `university/protocols/worker-activation.md`.
6. No workflow assigned and the task is a Student session: activate Rector and
   run `rector-startup`.
7. Load one workflow or policy only if the task needs it, plus the exact files
   the task touches and their nearest governing README.
8. Stop loading context as soon as the task is actionable. Do not scan trees.

### 2. Onboarding query template

If routing information is missing, ask using this structure:

```text
Boundary: <root | university | students>
Profession/Worker: <profession — worker>
Workflow: <workflow or none>
Read only: <exact optional docs>
Task: <change>
Validation: <make target or check to propose later>
```

### 3. Reading order (only when a deep dive is required)

1. `university/constitution/ONTOLOGY.md`
2. `university/constitution/RESPONSIBILITY-MATRIX.md`
3. `university/WORKSPACE.md`
4. `university/protocols/profession-routing.md`
5. `university/protocols/worker-activation.md`
6. The task's workflow and policy (`university/workflows/`, `university/policies/`)
7. `university/policies/interaction-format.md` and
   `university/policies/dialogue-language.md` before any Student-facing output

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
