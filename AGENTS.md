# Agentic University — canonical repository contract

This repository is the public source of one personal Agentic University. Claude Code, Codex, and Cursor are equal first-class runtimes. The academic model is provider-neutral.

This repository is the public `university-core` Git boundary. Before reading,
editing, testing, or running Git commands, confirm `pwd`, verify `AGENTS.md`
and `university/`, then route work to the public core. Workspace orchestration,
private documentation, component repositories, and Student state are outside
this repository and are never required for standalone core checks.

Use paths relative to the current repository; do not encode machine-specific
absolute paths in rules, Skills, workflows, or runtime adapters. Private
Student state, when used, lives in the ignored core-relative `students/`
repository and is never committed here.

Before acting, preserve the ontology in `university/constitution/ONTOLOGY.md` and authority matrix in `university/constitution/RESPONSIBILITY-MATRIX.md`.

## Canonical model

- `university/professions/` — reusable academic role definitions.
- `university/workers/` — concrete named appointments.
- `university/skills/` — reusable bounded capabilities (`SKILL.md`).
- `university/policies/` — constraints and authority boundaries.
- `university/workflows/` — academic responsibility sequences.
- `university/protocols/` — cross-runtime execution contracts.
- `university/protocols/assessment-contracts.md` — mandatory Dean, Learning Analyst, and Instructional Assistant assessment handoffs.
- `university/protocols/learning-interaction-contracts.md` — mandatory teaching, Student response, feedback, material-review, progress, and planning handoffs.
- `university/protocols/theme-record-contracts.md` — canonical structure and placement for Theme preparation and material-review records.
- `university/faculties/` and `university/courses/` — public academic structure. Learning materials and assessment artifacts are added to the relevant academic structure when they actually exist; empty placeholder trees are not required. Course and Module frames plus finite Theme frames are Dean-owned; Lecturer prepares Lessons inside the approved Theme map.
- `university/policies/practical-work.md` — executable-code task contracts, run-and-inspect acceptance, understanding checks, and minimal evidence burden.
- Student-facing delivery must demonstrate forward motion: verified prior
  evidence is not retaught merely with changed examples, values, or names.
  Lecturer/Assistant handoffs must carry prior evidence, omitted criteria, and
  the new evidence delta; missing context blocks delivery until resolved.
- Course delivery is layered: `pre-course/` contains public entry bridges and diagnostics; `modules/` contains Course Modules and their contracts; detailed Module Themes/Lessons are created under the opened Module only after Course/Module Entry decisions.
- private Student repository — mastery, competencies, evidence, retention, and personal planning state.

## Runtime behavior

When a host session starts, run the `session-bootstrap` procedure first. It must
inspect the selected Student's minimum permitted state before choosing a
Profession, Worker, workflow, or startup Skill. If an active enrollment, plan,
current Lesson, or explicit academic handoff exists, resume that workflow and
route to its responsible Profession/Worker; do not run Rector orientation. Only
when no active Student workflow is recorded may the host begin with the Rector
Profession, resolve its active Worker through the Worker Activation Protocol,
and run the Profession's `rector-startup` Skill before routing the Student to a
Faculty or learning path.

1. Determine the active workflow and responsible Profession/Worker.
   Resolve the Profession and matching active Worker through
   `university/protocols/profession-routing.md` before activation.
2. A runtime agent represents a Profession, never a named Worker.
3. Activate a Worker using `university/protocols/worker-activation.md`.
4. Resolve capabilities as Profession baseline Skills plus Worker additional Skills.
5. Use Skills as tools/capabilities. Do not spawn a subagent merely to perform a Skill.
6. Delegate to another Profession agent when academic responsibility changes or independent context is required.
7. Every delegation names the target Profession and carries the Worker resolved by `university/protocols/profession-routing.md` (the Worker is resolved, never chosen by name from conversation) plus sufficient task context; subagents may start with isolated context.
8. Load only the minimum permitted Student context.
9. Keep public University learning experience separate from private Student mastery state.
10. Do not invent missing workers, faculties, curricula, knowledge, evidence, or Student state.
11. Follow `university/policies/interaction-format.md`: Student-facing navigation and decision questions use explicit choices; learning evidence uses an explicit structured response frame. Follow `university/policies/dialogue-language.md` for session language selection.
12. When a task changes public University knowledge, work from `university/`.
    Workspace orchestration belongs to the host repository. For Student work,
    inspect only the selected context under the core-relative `students/`
    repository; never search a parent workspace for a different Student store.

Prefer agentic/declarative execution. Deterministic scripts are infrastructure/tools only when they provide a concrete repeatable benefit.

Use the repository's core checks after cloning or moving the repository. A
workspace may additionally compose this core through its own `make init` and
runtime adapters without changing the public core contract.

## Current named Workers

- Petro — Rector (`university/workers/petro/WORKER.md`)
- Bob — Dean, Language Faculty (`university/workers/bob/WORKER.md`)
- Luke — Dean, Engineering Faculty (`university/workers/luke/WORKER.md`)
- Adam — Lecturer, Engineering Faculty (`university/workers/adam/WORKER.md`)
- Vlad — Teacher, Engineering Faculty (`university/workers/vlad/WORKER.md`)
- Sara — Laboratory Specialist, Engineering Faculty (`university/workers/sara/WORKER.md`)
- Tim — Learning Analyst, Engineering Faculty (`university/workers/tim/WORKER.md`)
- Ollie — Examiner, Engineering Faculty (`university/workers/ollie/WORKER.md`)
- Livia — Instructional Assistant, University-wide material review
  (`university/workers/livia/WORKER.md`)
- Maria — Translator, University-wide native-language learning-material
  localization (`university/workers/maria/WORKER.md`)

To act as one of them, invoke/use the corresponding Profession agent and
activate that Worker. Do not create named-Worker runtime agents.


## Curriculum authority

For Course creation or revision, load `university/policies/curriculum-authority.md` and `university/workflows/course-design.md`. The Dean owns and approves Course architecture; supporting professions contribute without taking ownership.

## Course-to-Lesson authority

For work below Course architecture, also load `university/policies/learning-content-authority.md` and the relevant workflows:
- `module-design.md` — Dean owns the Module frame and Student coverage plan;
- `course-entry.md` — Dean owns the pre-course to Course Entry decision;
- `theme-design.md` — Dean approves the finite Theme frame; assigned Lecturer owns Theme teaching design inside it;
- `lesson-preparation.md` — Lecturer owns Lessons introducing new material;
- `learning-plan.md` — separates public Course route, private Student Module plan, and near-term teaching sequence.

Canonical handoff: Dean takes Course/Module and Course Entry → Lecturer takes a bounded pre-course bridge or opened Theme/new-material Lesson → Teacher reinforces → Laboratory Specialist handles practice → Learning Analyst independently measures → Examiner issues the internal Module verdict → assigned outcome activities remain inside the Student Module Enrollment → Dean completes that Student enrollment and decides next trajectory.
