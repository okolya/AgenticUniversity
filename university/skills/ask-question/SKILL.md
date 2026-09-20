---
name: ask-question
description: Ask a focused learning question. Use during teaching, tutoring, diagnostics, or assessment when the active Worker needs evidence or reflection.
---
# Ask question

Ask a learning question appropriate to the current goal, context, and practice/assessment mode.

Student-facing output must follow `university/policies/interaction-format.md`.
Use choices whenever the target can be tested with a bounded set of answers.
When the learning goal requires explanation, code, reasoning, or another
artifact, use `structured_evidence` and specify the smallest acceptable
response format instead of emitting an unbounded conversational question.

## Contract

Input must include the active Worker, purpose, applicable success criteria where relevant, policy/mode, and only the Student context required for the operation. Output is returned to the calling Worker; the Skill does not assume the Worker's academic authority.

For every Student-facing question, output:

- `question` — one focused prompt;
- `response_mode` — `single_choice`, `multiple_choice`, `ordered_choice`, or
  `structured_evidence`;
- `options` — stable labeled options for choice modes, otherwise `[]`;
- `selection_rule` — how the Student responds;
- `fallback` — the allowed `Other / not listed` behavior, if any.
