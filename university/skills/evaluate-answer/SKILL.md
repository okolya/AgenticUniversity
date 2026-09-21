---
name: evaluate-answer
description: Evaluate a Student answer against explicit criteria. Use for formative feedback, diagnostics, or authorized assessment without exceeding caller authority.
---
# Evaluate answer

Evaluate a Student answer against explicit criteria and return evidence/feedback without exceeding the caller Worker academic authority.

Evaluate the demonstrated understanding, not compliance with a template. A
structured response frame is a communication aid and a minimum evidence guide,
not a grading form. If the Student uses another order or wording but clearly
demonstrates the relevant understanding, accept and interpret the evidence
semantically. Ask for clarification only where a required concept remains
unclear or contradictory; do not penalize harmless omissions of headings,
formatting, terminology, or exact example values.

## Contract

Input must include the active Worker, purpose, applicable success criteria where relevant, policy/mode, and only the Student context required for the operation. Output is returned to the calling Worker; the Skill does not assume the Worker's academic authority.

When the answer accompanies executable work, this Skill does not replace the
run-and-inspect requirement in `practical-work.md`. The accepting Worker must
inspect and run the submitted code, then use the answer only as compact
evidence of understanding against the observed behavior.
