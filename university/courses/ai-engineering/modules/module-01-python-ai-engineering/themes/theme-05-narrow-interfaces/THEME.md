# Theme 5 — Narrow library and service interfaces

- **Module:** Python AI Engineering
- **Owner:** assigned Engineering Faculty Lecturer
- **Status:** bounded four-Lesson sequence approved; detailed Lessons are authored just in time

## Boundary

Integrate one external library or service through a narrow Python interface
with explicit inputs, outputs, configuration, and failure handling. Do not
expand into AI model engineering, RAG, agents, or cloud platform design.

## Theme outcome

The Student can isolate an external dependency behind a small interface and
handle both successful and failed calls predictably.

## Success criteria

- dependency assumptions and configuration are explicit;
- adapter input/output behavior is stated;
- dependency failure is handled without hiding the cause;
- the Student can test the boundary with a safe local substitute where needed.

## Complete Lesson sequence

This Theme contains exactly four Lessons:

1. define an external dependency's input/output contract;
2. isolate it behind a narrow adapter function or component;
3. handle success, dependency failure, configuration failure, and a safe
   local substitute;
4. complete a bounded integration component and return the Theme evidence.

## Theme checkpoint and stop condition

The final artifact must integrate one bounded library or service through an
explicit interface, demonstrate success and failure behavior, and explain its
configuration boundary. After Lesson 4 the Lecturer returns evidence to Dean;
no fifth Lesson is created without a new Dean decision. AI model engineering,
RAG, agents, and cloud platforms remain out of scope.

## Lecturer handoff

The Lecturer prepares these four Lessons only, chooses one bounded dependency
appropriate to the current Student context, and returns the final practical
evidence to Dean. A second dependency requires a new Dean decision.
