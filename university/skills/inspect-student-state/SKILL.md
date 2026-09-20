---
name: inspect-student-state
description: Read only permitted private Student state and return facts relevant to the active academic decision. Never modify mastery state.
---
# Inspect permitted Student state

Read only the Student context permitted by policy and return facts relevant to the active academic decision. Do not modify mastery state.

## Contract

Input must include the active Worker, purpose, applicable success criteria where relevant, policy/mode, and only the Student context required for the operation. Output is returned to the calling Worker; the Skill does not assume the Worker's academic authority.
