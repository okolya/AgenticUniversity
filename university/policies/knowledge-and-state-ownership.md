# Knowledge and State Ownership

## Fundamental boundary

- **University owns behavior.** Professions, Workers, Skills, Policies, Workflows, Protocols and runtime definitions are public University assets.
- **University owns public/reusable accumulated knowledge.** Materials, explanations, exercises, labs, assessment methods, curated resources, teaching patterns and other depersonalized knowledge created during real learning belong to the public University.
- **Students owns only private educational state.** Identity/state, goals, enrollments, plans, mastery, gaps, evidence, retention, application/certification state and other student-specific facts belong to the private Students repository.
- **Workspace owns no separate academic layer.** The public root repository
  owns orchestration and the public University source under `university/`; it
  composes the nested private Students repository at runtime.

## Promotion rule

If an artifact created during a learning interaction becomes generally reusable and can be safely depersonalized, it MUST be stored in the public University rather than accumulated in the private Students repository.

Student-specific mastery conclusions and private context MUST NOT be promoted. Public knowledge must never expose one student's private state to another student.

## No copying of University definitions

The Students repository references public Faculty, Course, Module, competency and other University entities. It does not copy their canonical definitions. This prevents private state from becoming a stale fork of University knowledge.
