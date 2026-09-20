# Agentic University — canonical repository contract

This repository is the public source of one personal Agentic University. Claude Code, Codex, and Cursor are equal first-class runtimes. The academic model is provider-neutral.

The AgenticUniversity workspace root is the public Git repository and
composition root. Before reading, editing, testing, or running Git commands,
confirm `pwd`, verify `AGENTS.md`, `university/`, and `students/`, then route
the work to its ownership boundary:

- root files and `scripts/` — orchestration, runtime installation, and Git
  operations;
- `university/` — public University source, academic knowledge, policies,
  workflows, Skills, professions, and Workers;
- `students/` — private Student repository with its own Git boundary.

The root Git repository must never track `students/` contents. Use paths
relative to the root repository; do not encode machine-specific absolute paths
in rules, Skills, workflows, or runtime adapters.

Before acting, preserve the ontology in `university/constitution/ONTOLOGY.md` and authority matrix in `university/constitution/RESPONSIBILITY-MATRIX.md`.

## Canonical model

- `university/professions/` — reusable academic role definitions.
- `university/workers/` — concrete named appointments.
- `university/skills/` — reusable bounded capabilities (`SKILL.md`).
- `university/policies/` — constraints and authority boundaries.
- `university/workflows/` — academic responsibility sequences.
- `university/protocols/` — cross-runtime execution contracts.
- `university/faculties/` and `university/courses/` — public academic structure. Learning materials and assessment artifacts are added to the relevant academic structure when they actually exist; empty placeholder trees are not required. Course architecture is Dean-owned; detailed Module content is created only when needed.
- private Student repository — mastery, competencies, evidence, retention, and personal planning state.

## Runtime behavior

When a new University session starts without an already assigned academic
workflow, begin with the Rector Profession and resolve its active Worker through
the Worker Activation Protocol. Run the Profession's `rector-startup` Skill before
routing the Student to a Faculty or learning path.

1. Determine the active workflow and responsible Profession/Worker.
2. A runtime agent represents a Profession, never a named Worker.
3. Activate a Worker using `university/protocols/worker-activation.md`.
4. Resolve capabilities as Profession baseline Skills plus Worker additional Skills.
5. Use Skills as tools/capabilities. Do not spawn a subagent merely to perform a Skill.
6. Delegate to another Profession agent when academic responsibility changes or independent context is required.
7. Every delegation must explicitly identify the target Worker and sufficient task context; subagents may start with isolated context.
8. Load only the minimum permitted Student context.
9. Keep public University learning experience separate from private Student mastery state.
10. Do not invent missing workers, faculties, curricula, knowledge, evidence, or Student state.
11. Follow `university/policies/interaction-format.md`: Student-facing navigation and decision questions use explicit choices; learning evidence uses an explicit structured response frame. Follow `university/policies/dialogue-language.md` for session language selection.
12. When a task changes public University knowledge, work from `university/`;
    when it changes orchestration or runtime behavior, work from root; when it
    changes private Student state, work from `students/` and load only the
    selected Student context. Verify the selected repository with
    `git rev-parse --show-toplevel` before edits or commands.

Prefer agentic/declarative execution. Deterministic scripts are infrastructure/tools only when they provide a concrete repeatable benefit.

Run `make init` from the root after cloning or moving the repository. It
initializes Claude, Codex, Cursor, host-level public Skills, and project Git
hooks without replacing unrelated runtime assets.

## Current named Workers

- Petro — Rector (`university/workers/petro/WORKER.md`)
- Bob — Dean, Language Faculty (`university/workers/bob/WORKER.md`)
- Luke — Dean, Engineering Faculty (`university/workers/luke/WORKER.md`)

To act as one of them, invoke/use the corresponding Profession agent and activate that Worker. Do not create `petro`, `bob`, or `luke` runtime agents.


## Curriculum authority

For Course creation or revision, load `university/policies/curriculum-authority.md` and `university/workflows/course-design.md`. The Dean owns and approves Course architecture; supporting professions contribute without taking ownership.

## Course-to-Lesson authority

For work below Course architecture, also load `university/policies/learning-content-authority.md` and the relevant workflows:
- `module-design.md` — Dean owns the Module frame and Student coverage plan;
- `theme-design.md` — assigned Lecturer owns Theme teaching design;
- `lesson-preparation.md` — Lecturer owns Lessons introducing new material;
- `learning-plan.md` — separates public Course route, private Student Module plan, and near-term teaching sequence.

Canonical handoff: Dean takes Course/Module → Lecturer takes Theme/new-material Lesson → Teacher reinforces → Laboratory Specialist handles practice → Learning Analyst independently measures → Examiner issues the internal Module verdict → assigned outcome activities remain inside the Student Module Enrollment → Dean completes that Student enrollment and decides next trajectory.
