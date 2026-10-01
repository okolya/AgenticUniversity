---
name: create-enrollment
description: Record an enrollment change in the private Student workspace after Student agreement and an authorized Dean decision; it does not choose placement itself.
class: learning
---
# Create enrollment

Bounded Student-state operation after the academic decision already exists.

Required authority: appointed Dean of the relevant Faculty under `faculty-entry`/`module-entry`.

The Skill records the agreed enrollment/entry point and planning references. It does not choose the Module, skip prerequisites, or create curriculum.

## Contract operation

Performs `record-enrollment` from `protocols/student-state-contract.md`: the
Enrollment references the public Course/Module and never copies its definition.
The agreed Plan is written with it. After writing, the caller reads the
Enrollment back per `protocols/artifact-verification.md`.
