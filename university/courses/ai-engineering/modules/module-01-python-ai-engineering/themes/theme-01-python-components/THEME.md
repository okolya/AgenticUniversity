# Theme 1 — Python components and maintainable boundaries

- **Module:** Python AI Engineering
- **Owner:** assigned Engineering Faculty Lecturer
- **Status:** preparation complete; ready for Student delivery through four Lessons and one final checkpoint

## Boundary

Build small readable Python components with explicit function, data, and
entry-point boundaries. Do not expand into frameworks, AI libraries, or
deployment.

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

## Complete Lesson sequence

This Theme contains exactly four Lessons. The sequence is complete when Lesson
4 checkpoint evidence is received; no additional Lesson is created by the
Lecturer without a new Dean decision.

1. `lesson-01-separate-function-responsibilities.md` — identify and separate
   function responsibilities and trace data through a small program.
2. `lesson-02-explicit-data-boundaries.md` — pass data through parameters and
   return values instead of hiding input/output inside reusable logic.
3. `lesson-03-separate-entry-point-and-component.md` — separate the executable
   entry point from reusable component code across two files.
4. `lesson-04-theme-checkpoint-small-python-component.md` — integrate the
   Theme skills in one bounded component and provide the final Theme evidence.

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
| Before delivery | Adam / Lecturer | Presents one Lesson and its bounded task | Outcome, prerequisites, artifact, command, required cases, minimum evidence | May not add a Lesson or change Theme criteria |
| Before delivery | Livia / Instructional Assistant Profession | Does not teach Student; reviews the complete material with Adam | Pedagogical review of language, vocabulary, task clarity, and evidence burden | Does not assess code or issue a verdict |
| Lesson submission | Adam / Lecturer | Receives Student artifact, observations, explanation, and criticism | Contract 3 response; Adam inspects and runs executable work | Owns Lesson feedback, not independent mastery verdict |
| Remediation need | Vlad / Teacher | Works with Student on one identified understanding gap | Adam's bounded gap handoff and one focused correction | Cannot add Theme scope or issue independent verdict |
| Practical gap | Sara / Laboratory Specialist | Supervises the optional Lesson 4 Lab | Practical outcome, run contract, artifact, minimal evidence | Cannot add a Lesson or issue mastery verdict |
| Independent evidence need | Tim / Learning Analyst | Works with Student only after Dean's Assessment Request | Exact criteria, bounded assessment, permitted context, evidence handoff | Does not teach or choose trajectory |
| Module examination | Ollie / Examiner | Does not work with Student during Theme delivery | Dean's approved Module Exit criteria and examination request | No Theme verdict or remediation |
| Theme checkpoint | Adam → Luke / Lecturer → Dean | Student receives the bounded result/next action from the responsible Worker | Contract 6 evidence: completed Lessons, observations, gaps, recommendation | Luke decides next Theme, correction, or measurement |

The normal path is Adam ↔ Student for Lessons. Other Workers enter only at the
listed trigger; their mere appointment does not create an automatic handoff.

## Lecturer handoff

Adam, the assigned Engineering Faculty Lecturer, owns preparation and delivery
of these four Lessons. Before each Lesson is delivered, he invokes the
Instructional Assistant Profession for a complete pedagogical review. After
Lesson 4 he returns the accumulated Theme evidence to the Dean; he may not
extend the sequence or declare the next Theme.

## Profession handoff status

- **Dean / Luke:** approved the Theme boundary, finite sequence, criteria, and
  stop condition.
- **Lecturer / Adam:** prepared the four Lessons and owns their delivery and
  Lesson-level learning feedback.
- **Instructional Assistant Profession / Livia appointment:** completed the
  pedagogical review; the reported clarity and vocabulary findings were
  applied before delivery.
- **Learning Analyst / Tim:** not invoked for Lesson delivery. No independent
  measurement is required before the formative Theme sequence; Dean may issue
  a separate bounded request if the final evidence is insufficient for a
  placement or assessment decision.
- **Teacher / Vlad:** prepared a bounded reinforcement plan; no reinforcement
  handoff is currently required.
- **Laboratory Specialist / Sara:** prepared the optional Lesson 4 Lab; it is
  not an additional Lesson and is used only if Adam requests it for a concrete
  practical need.
- **Examiner / Ollie:** completed the examinability contribution; no Module-exit
  examination is due at this Theme checkpoint and no verdict was issued.

The next real handoff is Student response to Adam under Contract 3. After
Lesson 4, Adam returns Contract 6 evidence to Luke. Worker appointments are
explicit staffing boundaries, not implicit authority.
