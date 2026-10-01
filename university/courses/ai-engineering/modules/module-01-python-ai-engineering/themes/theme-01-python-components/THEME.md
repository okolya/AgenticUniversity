# Theme 1 — Python components and maintainable boundaries

- **Module:** Python AI Engineering
- **Owner:** assigned Engineering Faculty Lecturer
- **Status:** approved frame and prepared materials; Dean readiness recorded

## Boundary

Build small readable Python components with explicit function, data, and
entry-point boundaries. Do not expand into frameworks, AI libraries, or
deployment.

All four Lessons use the same practical evidence boundary: the accepting
Worker inspects and runs the submitted artifact, checks the declared ordinary,
boundary, and failure cases, and requests only compact evidence plus the short
explanation needed to expose understanding. A claim or pasted output without
the runnable artifact is insufficient.

## Theme outcome

The Student can decompose a small requirement, implement the component, and
explain how input, transformation, and output responsibilities are separated.

## Success criteria

- named functions have one clear primary responsibility and a visible data
  flow;
- reusable functions receive required data through parameters and return their
  result instead of reading input or printing unexpectedly;
- the executable entry point is distinguishable from reusable logic and can be
  placed in a separate file;
- ordinary, boundary, and invalid behavior is stated and checked before the
  final submission;
- the Student can make and explain one controlled change and describe the
  limits of the checks performed.

## Dean-goal alignment

Theme 1 serves the Dean-approved Module 1 goals without expanding them:

| Dean / Module goal | Theme 1 result | Evidence source |
|---|---|---|
| Implement a readable Python component with clear functions and data boundaries | Student separates input, transformation, output, and entry-point responsibilities | Lessons 1–3 and Lesson 4 component |
| Organize executable and reusable code into maintainable boundaries | Student places reusable logic separately from the executable entry point | Lesson 3 and Lesson 4 component |
| State and handle ordinary, boundary, and invalid behavior | Student runs the declared cases and preserves deliberate failure behavior | Lessons 1 and 4 |
| Validate behavior and explain limits of validation | Student performs focused checks, one controlled change, and states what was not checked | Lesson 4 checkpoint |

The Theme does not claim to complete the full Module Exit Contract. Structured
data, runtime/dependency reproducibility, external interfaces, and broader
production review remain in later Themes.

## Sequence traceability

The Lesson sequence is cumulative. Each Lesson consumes the previous result and
adds the next bounded capability:

| Lesson | Parent Theme criterion | Consumes | Adds | Enables |
|---|---|---|---|---|
| 1 | named functions have clear responsibilities | Course Entry evidence for basic functions and flow | pure component calculation/formatting without terminal I/O | explicit separation of input boundary from logic |
| 2 | reusable functions receive data explicitly | Lesson 1 pure component | CLI boundary isolated from reusable logic; direct reuse | file/module separation without hidden state |
| 3 | executable entry point is distinguishable from reusable logic | Lesson 2 explicit boundary | imported reusable module and separate entry point | transfer to an unfamiliar component |
| 4 | all Theme criteria and controlled validation | Lessons 1–3 | unfamiliar meeting component with failure path and controlled change | Theme checkpoint and Dean Contract 6 handoff |

The cumulative Theme result advances Module 1 Exit Contract criteria 1 and 2:
readable Python components with clear boundaries and maintainable separation of
reusable code from the executable entry point. Later Themes own the remaining
Module Exit criteria.

## Complete Lesson sequence

This Theme contains exactly four Lessons. The sequence is complete when Lesson
4 checkpoint evidence is received; no additional Lesson is created by the
Lecturer without a new Dean decision.

1. `lesson-01-separate-function-responsibilities.md` — identify and separate
   function responsibilities in a new pure component without repeating Course
   Entry parsing/error work.
2. `lesson-02-explicit-data-boundaries.md` — connect CLI input to the component
   while keeping reusable functions independent of the input source.
3. `lesson-03-separate-entry-point-and-component.md` — separate reusable
   module code from the executable entry point and verify import behavior.
4. `lesson-04-theme-checkpoint-small-python-component.md` — transfer all Theme
   boundaries to an unfamiliar meeting component and provide final evidence.

## Theme checkpoint and stop condition

The final submission must contain one runnable component, its entry point,
ordinary/boundary/failure checks, a short responsibility/data-flow
explanation, and one controlled change. The accepting Worker inspects and runs
the code. The Lecturer returns the evidence and any unresolved gap to the
Dean. The Theme stops after this checkpoint: demonstrated criteria move to
the next Dean-approved Theme, while a real gap returns to Dean for a bounded
decision rather than an automatically generated Lesson.

## Worker–Student interaction points

| Stage | Worker / Profession | Interaction with Student | Required input/output | Boundary |
|---|---|---|---|---|
| Before delivery | Lecturer Profession / Engineering Faculty scope | Presents one Lesson and its bounded task | Outcome, prerequisites, artifact, command, required cases, minimum evidence | May not add a Lesson or change Theme criteria |
| After Lecturer final source review | Translator Profession / University-wide scope | Does not teach Student; localizes or audits learner-facing language | Selected dialogue language, final source, terminology decisions, localized artifact | Does not change technical identifiers, criteria, scope, or publication status |
| Before delivery | Instructional Assistant Profession / University-wide scope | Does not teach Student; reviews the complete material with the Lecturer | Pedagogical review of language, vocabulary, task clarity, and evidence burden | Does not assess code or issue a verdict |
| Lesson submission | Lecturer Profession / assigned Theme scope | Receives Student artifact, observations, explanation, and criticism | Contract 3 response; resolved Lecturer Worker inspects and runs executable work | Owns Lesson feedback, not independent mastery verdict |
| Remediation need | Teacher Profession / assigned Theme scope | Works with Student on one identified understanding gap | Lecturer's bounded gap handoff and one focused correction | Cannot add Theme scope or issue independent verdict |
| Practical gap | Laboratory Specialist Profession / Engineering Faculty scope | Supervises the optional Lesson 4 Lab | Practical outcome, run contract, artifact, minimal evidence | Cannot add a Lesson or issue mastery verdict |
| Independent evidence need | Learning Analyst Profession / assigned assessment scope | Works with Student only after Dean's Assessment Request | Exact criteria, bounded assessment, permitted context, evidence handoff | Does not teach or choose trajectory |
| Module examination | Examiner Profession / approved Module scope | Does not work with Student during Theme delivery | Dean's approved Module Exit criteria and examination request | No Theme verdict or remediation |
| Theme checkpoint | Lecturer Profession → Dean Profession | Student receives the bounded result/next action from the responsible Worker | Contract 6 evidence: completed Lessons, observations, gaps, recommendation | Dean decides next Theme, correction, or measurement |

The normal path is the assigned Lecturer Profession ↔ Student for Lessons. Other Workers enter only at the
listed trigger; their mere appointment does not create an automatic handoff.

## Lecturer handoff

The assigned Engineering Faculty Lecturer Profession owns preparation and delivery
of these four Lessons. Before each Lesson is delivered, it invokes the
Instructional Assistant Profession for a complete pedagogical review. After
Lesson 4 it returns the accumulated Theme evidence to the Dean; the Lecturer
may not extend the sequence or declare the next Theme.

The Dean → Lecturer handoff must provide the approved Theme frame, four Lesson
slots, criteria, exclusions, checkpoint, stop condition, permitted Student
context, and required Contract 6 output. The Lecturer → Instructional
Assistant review request must include all four learner-facing materials, the
Ukrainian dialogue language, vocabulary/progression concerns, practical
run-and-inspect contract, and evidence burden. The Assistant reports findings
but does not edit, assess code, approve publication, or change Theme scope.

## Profession handoff status

- **Dean Profession:** approved the Theme boundary, finite sequence, criteria, and
  stop condition.
- **Lecturer Profession:** prepared the four Lessons and owns their delivery and
  Lesson-level learning feedback.
- **Translator Profession:** completed the Ukrainian native-language and
  anglicism audit after Lecturer source finalization. Exact code/API names,
  commands, paths, and required output strings were retained; unnecessary
  English prose was localized. No material learner-path change was reported.
- **Instructional Assistant Profession / resolved University-wide appointment:** completed the
  pedagogical review; the reported clarity and vocabulary findings were
  applied by the Lecturer before delivery.
- **Learning Analyst Profession:** not invoked for Lesson delivery. No independent
  measurement is required before the formative Theme sequence; Dean may issue
  a separate bounded request if the final evidence is insufficient for a
  placement or assessment decision.
- **Teacher Profession:** prepared a bounded reinforcement plan; no reinforcement
  handoff is currently required.
- **Laboratory Specialist Profession:** prepared the optional Lesson 4 Lab; it is
  not an additional Lesson and is used only if the Lecturer requests it for a concrete
  practical need.
- **Examiner Profession:** completed the examinability contribution; no Module-exit
  examination is due at this Theme checkpoint and no verdict was issued.

The next real handoff is Student response to the assigned Lecturer under
Contract 3. After Lesson 4, the Lecturer returns Contract 6 evidence to the
Dean. Worker appointments are
explicit staffing boundaries, not implicit authority.
