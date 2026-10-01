# ADR 0010: Preparing Course material ahead of Students

- Status: accepted
- Date: 2026-10-01

## Context

`curriculum-authority.md` and `module-contracts.md` made a Course a route of
intended competencies, not a pre-authored syllabus. Detailed Themes, Lessons,
exercises, and labs were created near Module Entry from one Student's verified
state, and authoring them earlier "merely for completeness" was forbidden.
`learning-content-authority.md` said a Lesson is created just in time for the
current Student.

This was shaped by the AI Engineering Course, where the direction keeps
changing. It does not fit a Course whose route is stable and is taken by many
Students, such as the Language Faculty Course «Між B1 та B2», which has
established external roadmaps to calibrate against. The owner asked for its
Themes and Lessons to be prepared before any Student enters. The Dean refused,
because the rule is a University policy and the Dean cannot waive it.

The owner's position: preparing a Course ahead of its learners is the normal
process.

## Options considered

- **Keep just-in-time only** — a stable Course is rebuilt for every Student.
  Rejected as the cause of the problem.
- **Two Course types, `standard` and `individual`, declared in every
  `COURSE.md`** — drafted first. Examined against the Student path, the types
  differed only in when material is created: entry, placement, narrowing,
  evidence, and the evidence-delta check are per Student in both. A mandatory
  marker for a timing difference is more machinery than the difference justifies.
  Rejected.
- **One model: material may be prepared ahead or just in time, for approved
  Theme frames only** — chosen.
- **Pre-author only after the first Student** — safest for quality but does not
  allow preparing a Course ahead. Kept as a mitigation (`unpiloted`), not as the
  rule.

## Decision

Detailed Themes, Lessons, exercises, and labs may be prepared in two ways, and
one Course may use both:

1. **Ahead of any Student**, only for a Dean-approved Theme frame and its finite
   Lesson map, by the Profession that owns them under
   `learning-content-authority.md`, and reviewed by the Instructional Assistant.
   They are public University material.
2. **Just in time**, when no suitable prepared material exists or the Student's
   state calls for something new, as before.

Material prepared ahead carries an `unpiloted` mark until a Student has passed
it; the mark does not block delivery, and the material may be revised afterwards.
Detailed content is never generated merely to make a Course look complete.

Per Student, in every case: Course Entry, placement, skip and narrowing, the
Student's plan, the evidence delta, independent evidence, and the Module verdict.
A prepared Lesson is delivered only after the responsible Worker checks, against
that Student's verified evidence, that it adds a new evidence delta; a Lesson that
repeats a demonstrated criterion is skipped or returned to the Dean.

## Consequences

- `curriculum-authority.md`, `module-contracts.md`,
  `learning-content-authority.md`, `course-design.md`, `module-design.md`,
  `theme-design.md`, `lesson-preparation.md`, the Course template, and the core
  `AGENTS.md` summary say that material may be prepared ahead or just in time.
- The Lesson step for prepared material changes from "prepare for this Student"
  to "confirm the prepared Lesson fits this Student". The evidence-delta check
  and the Instructional Assistant's duplication test move to delivery.
- No Course needs a new declaration, and no core check or manifest field is
  added.
- The Student model, assessment independence, and Examiner and Learning Analyst
  authority are unchanged.
- Revisit if prepared Lessons repeatedly fail the evidence-delta check at
  delivery, which would mean the material was prepared for a route that is not
  stable enough.

## Scope boundary

This decision changes who may author Themes and Lessons and when. It does not
change Student state, placement authority, independent assessment, Worker
appointment, or the content of any Course.
