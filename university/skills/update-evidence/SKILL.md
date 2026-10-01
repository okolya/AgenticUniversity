---
name: update-evidence
description: Record assessment evidence and the caller's authorized assessment verdict in the private Student workspace; never creates academic authority or lets formative roles mark verified mastery.
class: learning
---
# Update evidence

A bounded Student-boundary operation for an already-authorized assessment verdict.

Performs `append-evidence` (and, for the Examiner, the Module verdict) from
`protocols/student-state-contract.md`. Evidence is append-only: a correction is
a new entry referring to the earlier one. Every entry carries the acting
Profession, the workflow, the date, and an artifact reference for executable
work. After writing, the caller reads the entry back per
`protocols/artifact-verification.md`.

## Allowed callers

- Learning Analyst under `theme-assessment`: verified Theme evidence + assessment result/findings.
- Learning Analyst under `course-entry` / `learning-assessment`: verified
  Course Entry or prerequisite evidence + criterion-level findings.
- Examiner under `module-exit`: Module evidence + Module verdict.
- Other callers only if a future explicit Policy/Workflow grants equivalent authority.

## Forbidden

- converting Lecturer/Teacher/Lab formative observations into verified mastery;
- changing another independent assessor's verdict;
- publishing private Student evidence/state;
- inventing missing Success Criteria or evidence.

The Learning Analyst records evidence only for the assigned criteria. Recording
Course Entry evidence does not confirm Course/Module Entry or choose the next
trajectory; those decisions remain with the Dean.
