---
name: session-bootstrap
description: Bootstrap a University Developer session — work that changes the University's own protocols, Skills, workflows, plans, or ADRs — by loading the smallest required context and routing to the owning repository boundary before any edits or commands.
class: development
---
# Session bootstrap

Establish context at the very start of a **University Developer** session
(Branch 3 of `university/protocols/host-prompt-assembly.md` Session start,
ADR 0009) without spending the context budget. This Skill is an
orchestration aid: it routes University-maintenance work, it never owns an
academic decision, appoints a Worker, or reads private Student state.

It is not the entry point for a Student session (use
`university/skills/inspect-student-state/SKILL.md` via Branch 1) or a
University Worker session (use `protocols/profession-routing.md` +
`protocols/worker-activation.md` via Branch 2). `host-prompt-assembly.md`
Step 0 decides which branch a session belongs to before this Skill runs.

Branch 1's state machine (`missing`, `unavailable`,
`available/no-active-workflow`, `available/active-workflow`) is canonical in
`host-prompt-assembly.md` and is not re-decided here: it governs whether a
Student's stable, authenticated Student ID resolves to usable state before
any Developer-session delegation into Branch 1 reads that state.

## Use when

- The resolved session kind is University Developer (changing the
  University's own protocols, Skills, workflows, plans, or ADRs), and the
  target repository or task boundary is unclear.
- The user says "bootstrap", "start", or "init" for University development.

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
5. If the task needs a Student's current state for context (for example,
   reviewing why a Lesson evidence check failed), do not duplicate that
   lookup here — delegate to Branch 1 of `host-prompt-assembly.md` /
   `inspect-student-state`, and only for the one Student the task names.
   This Skill does not itself resolve or inspect Student identity.
6. If the task needs an academic-staff decision (Dean/Lecturer/etc. acting in
   a Profession) rather than a direct edit, delegate to Branch 2 of
   `host-prompt-assembly.md` (`protocols/profession-routing.md` +
   `protocols/worker-activation.md`) instead of acting as that Worker here.
7. Resolve every repository-relative path from the verified boundary before
   reading it. In a composed workspace, do not prepend the host root to a
   path that is already relative to `university-core/`; report a missing file
   only after checking the canonical core-relative path.
8. Load one workflow or policy only if the task needs it, plus the exact files
   the task touches and their nearest governing README.
9. Stop loading context as soon as the task is actionable. Use exact known
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
