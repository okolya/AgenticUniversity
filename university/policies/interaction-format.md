# Student interaction format

Student-facing interaction is governed together with
`university/protocols/learning-interaction-contracts.md`. That protocol defines
the academic input/output handoff; this policy defines the response shape and
language for the Student-facing message.

Student-facing questions must make the expected response explicit and
structured.

## Navigation and decisions

For routing, setup, planning, preferences, and other decisions with a bounded
set of valid next steps:

1. Ask one focused question at a time.
2. Present the verified choices as a numbered list with stable short labels.
3. State whether the Student may choose one or several options.
4. Include `Other / not listed` only when an unlisted route is genuinely
   possible, and ask for a short description after that selection.
5. Never end with an unstructured prompt such as “What do you want?” when the
   repository already contains the available options.

## Learning evidence

Some learning, diagnostic, and assessment tasks cannot be answered by a menu.
In those cases, provide a structured response frame: the requested artifact or
answer format, its limits, and the criteria that will be checked. If a choice
can test the target criterion adequately, use choices; otherwise ask for the
smallest necessary free-form evidence rather than disguising it as a choice.

The frame is a support for communication, not a formal submission gate. The
responsible Worker evaluates whether the Student demonstrates the intended
understanding. A response written in another order or with different wording
must be accepted when its meaning is sufficiently clear. Request a correction
only for missing, contradictory, or genuinely ambiguous understanding—not for
cosmetic differences from the suggested structure.

For practical code submissions, keep the evidence frame minimal: artifact path,
run command, compact results for required cases, and only the short explanation
needed to expose understanding. Do not request a full program map, copied
tracebacks, or a long narrative when the accepting Worker can inspect and run
the code directly.

## Response contract

Every question returned by a Skill or Worker must include:

- `question`: the focused prompt;
- `response_mode`: `single_choice`, `multiple_choice`, `ordered_choice`, or
  `structured_evidence`;
- `options`: labeled choices for choice modes, or an empty list for evidence;
- `selection_rule`: how the Student should respond;
- `fallback`: whether and how an `Other / not listed` response is accepted.

Workers may add context, but may not remove this response structure from a
Student-facing question.

## Feedback and reporting

When a Worker returns feedback, it must state the observed result, the
demonstrated or missing understanding, one focused correction if needed, and
the next bounded action or handoff. A Worker must not turn feedback into an
unbounded new assignment.
