# Public / private boundary

University content and reusable learning experience are public by default. Personal mastery state, gaps, retention, assessment attempts/results as personal state, competencies, evidence, and personal planning state belong to the private Student workspace.

A learning interaction may be published when it is intentionally retained as reusable educational experience. Never publish private mastery conclusions merely because the interaction that produced them is public.

## Workspace repository boundary

The deployed core uses one public Git repository and one ignored nested private
Git repository: public University source lives under `university/`, while
private Student state lives under the core-relative `students/`. A larger host
may compose the core and add orchestration, but it does not relocate Student
state. The private Students repository contains no AI/runtime definitions and
no reusable University knowledge.
