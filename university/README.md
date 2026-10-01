# University

This directory is the public academic core.

- `constitution/` — university-wide principles and authority boundaries.
- `professions/` — profession templates: Rector, Dean, Lecturer, Translator, Instructional Assistant, Teacher, Laboratory Specialist, Learning Analyst, Examiner.
- `workers/` — concrete named Worker appointments.
- `skills/` — reusable capabilities shared across professions and faculties.
- `policies/` — privacy, publication, AI usage, assessment independence, evidence, access, appointment and source-quality rules.
- `workflows/` — student initialization, faculty entry, module entry, lesson, assessment and module exit processes.
- `faculties/` — Faculty definitions and Faculty staff indexes.
- `courses/` — public Course architecture. Each Course separates `pre-course/`
  entry bridges and diagnostics from `modules/`; detailed Themes and Lessons
  are created under an opened Module just in time.
- `schemas/` — machine-readable Student-state and interaction-response schemas
  with synthetic examples.
- `decisions/` — architecture decision records (ADRs).
- `MANIFEST.md` — generated single entry point listing what exists, for CLI and
  other hosts (`make generate-manifest`, `make check-manifest`).
- `templates/student/` — public template/schema for creating private student
  state inside the ignored core-relative `students/` repository.
- `protocols/` — interaction contracts between university, workers, skills and student workspace.

## Staffing

Named Workers are appointments of reusable Professions. Use the `appoint-worker` Skill and `worker-appointment` workflow. Staff are discoverable through the University and Faculty registries and the `workers` list of `MANIFEST.md`. Named Workers never receive their own runtime agents.


## Completion semantics

Public University Modules are reusable academic structures and are not closed by individual learners. Completion is recorded only in the private Student Module Enrollment / learning plan. Internal examination may be followed by application or external-certification activity before that enrollment is completed.
