---
name: inspect-student-state
description: Read only permitted private Student state and return facts relevant to the active academic decision. Never modify mastery state.
class: learning
---
# Inspect permitted Student state

Read only the Student context permitted by policy and return facts relevant to the active academic decision. Do not modify mastery state.

## Contract

Input must include the active Worker, purpose, applicable success criteria where relevant, policy/mode, and only the Student context required for the operation. Output is returned to the calling Worker; the Skill does not assume the Worker's academic authority.

## Contract operation

Performs `read` from `protocols/student-state-contract.md`, scoped to one
authenticated Student and to the requested entities only. It works against any
state store that implements the contract; in CLI hosts that is the SQLite
Student state store in the core-relative `students/` directory. Never search a parent workspace for an
alternative Student store or infer state availability from a generic filesystem
search (the state directory is ignored by Git tooling). Return exactly
one explicit state result: `available/no-active-workflow`,
`available/active-workflow`, `missing`, or `unavailable`, with only the
requested facts and any access/initialization blocker. Missing state is never
interpreted as an available empty state and never invented.

CLI hosts must obtain the Student ID from host authentication and read through
`python3 scripts/inspect-student-state.py --student-id <id> --select <selector>`
(core-relative), which resolves the registry entry and returns only the
selected facts as JSON. A name claim is resolved with
`python3 scripts/student_store.py resolve <claim>`, which returns the single
matching registry entry. A CLI host without a login may show the registry
(`python3 scripts/student_store.py list`: ids and labels only) so the user can
choose. Do not print or parse a whole Student document or read the database. The host-side selector adapter may expose only these bootstrap
selectors: `identity`, `active-enrollments`, `plans`, `current-lesson`,
`next-actions`, `checkpoints`, `stop-conditions`, and `handoffs`.

For session bootstrap, the first read is limited to Student identity/status,
active enrollments, active plans, current Lesson references, next actions,
checkpoints, stop conditions, and explicit handoffs. Do not read independent
evidence, artifacts, goals, notes, or public scope files until the selected
workflow and its responsible Profession require them. A later read may request
only the additional selectors needed for that workflow.
