# Student state authority

The private Student workspace owns personal mastery state.

## Read

Workers may read only the Student context needed by their active workflow and appointment scope.

## Write

- Lecturer, Teacher, and Laboratory Specialist may return formative observations; they do not mark verified mastery.
- Learning Analyst may record independent assessment evidence, criterion-level findings, competency verification, gaps, and retention findings when authorized by the active assessment workflow.
- Examiner may record Module examination evidence and the final Module-level verdict under `module-exit`.
- Dean may create/update enrollment and agreed planning state, persist post-examination application/certification plans, mark the private Student Module Enrollment completed when its plan is resolved, and may use verified evidence for placement/module-skipping decisions. Dean does not rewrite independent evidence or examination verdicts.
- Rector may initialize University-facing Student metadata and high-level goals. Rector does not own Faculty mastery decisions.

A Skill never gains write authority by itself. The active Profession + Workflow + Policy grants the operation.
