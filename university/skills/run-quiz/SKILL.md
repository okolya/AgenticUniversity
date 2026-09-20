---
name: run-quiz
description: Conduct a quiz under the active practice or assessment policy. Use when the active Worker needs a bounded question sequence.
---
# Run quiz

Conduct a quiz under the active mode and policy. Practice mode may allow hints; assessment mode follows independent assessment restrictions.

Every quiz item must be presented with an explicit response mode. Use a
bounded, labeled choice list when it can measure the criterion. Use
`structured_evidence` only when the criterion requires reasoning, code, or
another artifact, and state the required format and limits. Do not emit a bare
question with no response structure.

## Contract

Input must include the active Worker, purpose, applicable success criteria where relevant, policy/mode, and only the Student context required for the operation. Output is returned to the calling Worker; the Skill does not assume the Worker's academic authority.

Each item includes `question`, `response_mode`, `options` (or `[]` for
structured evidence), `selection_rule`, and `fallback` according to
`university/policies/interaction-format.md`.
