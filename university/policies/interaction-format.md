# Student interaction format

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
