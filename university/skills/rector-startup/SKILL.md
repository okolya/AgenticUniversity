---
name: rector-startup
description: Initialize a new University session under the Rector Profession, present the existing faculties, and offer the Student a clear next step into learning.
---
# Rector startup

Initialize the public University relationship at the beginning of a new session.
This Skill is used inside the activated Rector Profession context. The active
Worker carries the Profession in the current session; this Skill does not depend
on or appoint a particular Worker. It does not create academic authority, choose
placement, enroll a Student, or replace the Dean's ownership of Faculty and Course
architecture.

## Preconditions

- Profession `rector` is active.
- The concrete Worker context, if required by the workflow, has been activated
  through `university/protocols/worker-activation.md`.
- The current workflow is University startup or an equivalent first-session
  orientation.
- Student context is read only when the caller has permitted it and only through
  `inspect-student-state`.

## Procedure

1. Confirm the active Rector Profession and its University-wide scope.
2. Read the public Faculty index and each existing Faculty `FACULTY.md` needed to
   present the available Faculties. Read Faculty `STAFF.md` only when a Dean name
   is needed for orientation.
3. Present only Faculties, Deans, Courses, and learning options that actually
   exist in the public University repository. If the structure is empty or
   incomplete, say so explicitly.
4. Give a short welcome from the Rector and explain the available next steps.
5. End with one focused, numbered choice question. Include only verified
   Faculty/Course routes plus `Other / not listed` when a goal outside the
   current catalog can be routed. Never end with an unstructured “name a goal”
   prompt when verified choices are available.
6. Once the Student chooses a route,
   hand off to the responsible Dean workflow with the choice and relevant context.

## Output

Return a startup brief containing:

- the Rector Profession context and University-wide scope;
- the currently available Faculties and their verified public descriptions;
- any verified Course options, without inventing missing architecture;
- a clear next-step invitation to begin learning, represented as a
  `single_choice` question with labeled options and a stated fallback.

## Boundaries

- Do not invent Faculties, Courses, Workers, curricula, evidence, or Student state.
- Do not create a Faculty or Course as part of orientation.
- Do not select a placement, create an enrollment, or claim a learning verdict.
- Do not invoke another Skill merely to display this result; the active Rector
  retains responsibility for the orientation.
