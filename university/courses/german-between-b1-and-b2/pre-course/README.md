# Між B1 та B2 — Pre-course

## Purpose

The pre-course is the public entry layer before the Student enters the Course.
It measures the Course and Module Entry Contracts and gives the Dean the
independent evidence needed for the Course Entry decision and first Module
placement.

The entry diagnostic is a placement tool, not an admission barrier: its result
decides where the Student begins in the Course route, not whether the Student
may study.

The pre-course is not a Module and does not count as Course delivery. It does
not change the Course's Module architecture. Its artifacts are public
University material; the Student's responses, evidence, and decisions remain in
the private Student workspace.

## Lifecycle

```text
independent entry diagnostic → Dean Course Entry decision → first Module route
```

A bounded bridge may be added only for a known entry gap and only through a
Dean-issued sequence (see `course-entry.md`). No bridge exists yet.

## Entry diagnostic: Dean frame (Assessment Request, Contract 1)

This section is the Dean's request to the appointed Learning Analyst. It states
what must be measured. It does not prescribe the tasks, the assessment
implementation, or the teaching path.

### Purpose and uncertainty

- Purpose: Course Entry and first Module placement.
- Missing evidence: the Student's current German performance relative to the
  A2 foundations and the B1 Recovery criteria is unknown after a period of
  interruption.

### Criteria to measure

1. **A2 foundations** — the four Entry criteria of Module 2 (B1 Recovery):
   controlled basic statements and questions; essential articles, cases,
   pronouns, prepositions, and verb forms preserving meaning; present, past,
   and future reference; high-frequency vocabulary and functional phrases.
2. **B1 performance** — the Exit criteria 1–7 of Module 2, across Lesen, Hören,
   Schreiben, and Sprechen, including noticing uncertainty and requesting
   clarification or repair.

Results are reported per criterion as `demonstrated`, `not demonstrated`, or
`uncertain`. A criterion that cannot be measured in the available channel
(for example Sprechen when no spoken exchange is possible) is reported as
`uncertain`, never as `demonstrated`.

### Scope and limits

- Two parts: Part A measures the A2 foundations; Part B measures B1
  performance. Part B is administered only when Part A does not show A2 gaps
  that materially block B1 work (see stop condition).
- One attempt per part. The Student may take the parts in separate sessions.
  Each part is bounded to a single sitting; the Analyst proposes the exact
  length within that limit.
- The diagnostic does not teach, does not assess B2 competencies, and is not an
  exam-format simulation.

### Stop condition

The Analyst stops when every criterion in scope has a result, or when Part A
shows that A2 gaps materially block B1 work. In the second case the Analyst
returns the evidence without administering Part B, and states which criteria
were not measured.

### Language of the artifact

All learner-facing text is in German. Task instructions use simple German at
A2 level or lower, so that misunderstanding an instruction is not mistaken for
a gap in the measured criterion. Assessor-only criteria are kept separate from
learner-facing text.

### AI and tool mode

The mode differs by step and is recorded with the evidence because it affects
what the evidence proves (`policies/ai-usage.md`):

- measured attempts for Parts A and B (comprehension, form, vocabulary,
  Schreiben, Sprechen): `NO_AI`, no dictionary;
- an optional, clearly separated revision step after a measured Schreiben or
  Sprechen attempt: `AI_ASSISTED` with the use disclosed, to give evidence for
  noticing and repairing an error. Its result is recorded separately and does
  not replace the unassisted measurement.

The Analyst may refine task design within this mode but may not weaken the
`NO_AI` rule for the measured attempts.

### Permitted Student context

The artifact is public and Student-independent. It must contain no private
Student information. Student-specific results are recorded by the Analyst in the
private Student workspace through `update-evidence` after the diagnostic is
administered.

### Handoff stage

Before publication the Analyst invokes the Instructional Assistant for review
(Contract 3), applies the report, and returns the artifact path and review
record to the Dean. Placement and trajectory remain with the Dean.

## Dean Course Entry decision map

After independent evidence (Contract 4) the Dean decides by criterion-level
results, not by a numeric score. The decision is the Dean's and is made with the
Student.

| Evidence | Dean decision |
|---|---|
| A2 criteria `demonstrated`; B1 criteria mixed or not yet shown | Skip Module 1; enter Module 2 narrowed to the B1 criteria not yet demonstrated |
| One or more A2 criteria `not demonstrated` | Confirm Course Entry; enter Module 1 narrowed to those criteria only |
| A2 and B1 criteria `demonstrated` in all four skills | Consider Module 3 entry; verify with a Module 3 Entry check if evidence is stale or uncertain |
| Criteria `uncertain` or contradictory | Request a bounded further measurement for those criteria; defer entry |
| Student does not meet the Course Entry Contract | Another route or Faculty/Course choice (`course-entry.md`) |

No threshold or percentage is fixed here. Narrowing never removes a criterion
from the Course Success Criteria; it only decides which criteria are taught and
examined for that Student.

## Current status

The diagnostic artifact (`entry-diagnostic-part-a.md`,
`entry-diagnostic-part-b.md`, and the assessor-only
`entry-diagnostic-assessor-record.md`) is created by the Learning Analyst under
Contract 2. It was reviewed once by the Instructional Assistant; the revised
version has not been re-reviewed and is not yet delivered to any Student. No
bridge, Theme, or Lesson exists.

### Provisional parameters (Dean decision, until a pilot)

These values were proposed by the Analyst and accepted by the Dean as
provisional. They are unpiloted and may change after the first administration:

- stop rule: Part B is withheld if E1 is not demonstrated, or if two or more of
  E1–E4 are not demonstrated;
- criterion X6 is read as forms that were correct in Part A reappearing
  correctly in free production in Part B;
- the revision step (Z) applies to Schreiben only;
- time limits of 45 minutes (Part A) and 75 minutes (Part B), and the A2/B1
  level calibration of the tasks.

### Decided

- assessor-only material (keys, audio scripts) stays public in this repository,
  as in the AI Engineering pre-course. The University model has no restricted
  location for it, and a Student can read the keys, so an administration
  without an observer is weaker evidence.

### Open decisions

- who administers and observes the sitting, and the typed or handwritten
  channel.
