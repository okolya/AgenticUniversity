---
name: inspect-student-state
description: Read only permitted private Student state and return facts relevant to the active academic decision. Never modify mastery state.
---
# Inspect permitted Student state

Read only the Student context permitted by policy and return facts relevant to the active academic decision. Do not modify mastery state.

## Contract

Input must include the active Worker, purpose, applicable success criteria where relevant, policy/mode, and only the Student context required for the operation. Output is returned to the calling Worker; the Skill does not assume the Worker's academic authority.

## Contract operation

Performs `read` from `protocols/student-state-contract.md`, scoped to one
Student and to the requested entities only. It works against any state store
that implements the contract; in CLI hosts that is the private core-relative
`students/` repository. Never search a parent workspace for an alternative
Student store. Missing state is reported as missing, never invented.
