# Theme Record Contracts

Theme preparation and material review records are Theme-local execution
artifacts. Their canonical structure is shared across the University, but
their contents remain specific to one Theme, Lesson sequence, learner context,
and review cycle.

## Placement rule

- `theme-preparation-record.md` belongs beside the Theme it describes.
- `material-review.md` belongs beside the learner-facing materials it reviews.
- reusable rules belong in University policies, workflows, protocols, and
  Skills; they must not be copied into every Theme record as competing rules.
- a Module may contain an aggregate readiness index with links to Theme-local
  records, but must not duplicate their full handoff or review reports.

## `theme-preparation-record.md` contract

Each record must identify:

1. Course, Module, Theme, dialogue language, responsible Profession, and
   resolved appointment scope;
2. Dean → Lecturer Contract 1 input, output, boundary, and readiness decision;
3. the approved Theme outcome, criteria, exclusions, finite Lesson sequence,
   checkpoint, and stop condition;
4. the cumulative traceability map:
   `Module criterion → Theme criterion → Lesson delta → next result`;
5. omitted/already-demonstrated criteria and the permitted Student context,
   without copying private Student state into public material;
6. material-owner → Instructional Assistant Contract 5 input, output,
   findings disposition, and readiness signal;
7. Translator handoff and semantic-equivalence result when localization is
   required;
8. Teacher, Laboratory Specialist, Learning Analyst, and Examiner status,
   including the concrete trigger when any is invoked;
9. the research decision: sources retained, rejected, or not needed, with
   bounded reasons;
10. the multimedia decision: curation report or an explicit no-multimedia
    decision, including fallback when a proposed source is not required;
11. Lecturer final control review and the Dean's readiness decision;
12. the Contract 6 evidence handoff and Theme stop/next-decision boundary.

## Complete preparation gate

The record is the Theme-local evidence bundle for the complete
material-preparation gate in ADR 0011. It must not claim `ready` merely because
Lesson files exist or repository checks pass. Before the claim, the record must
connect, in order, the approved scope handoff, research/curation decision,
bounded authoring, complete Instructional Assistant review, finding
dispositions, required specialist/language handoffs, Lecturer final control,
and Dean readiness decision.

For ahead-of-student preparation, the record must also state `unpiloted` and
list the Student-specific checks that remain open at delivery. For a package
still in progress, use an explicit non-ready status rather than omitting the
missing stage.

## `material-review.md` contract

Each review must identify:

1. the exact Theme materials and version/review stage;
2. learner/context permitted for the review and the declared Theme outcome;
3. Student feedback signals, if any, separated from learning evidence;
4. strengths to preserve;
5. vocabulary, sequence, coherence, evidence-burden, and forward-motion
   findings;
6. the Module → Theme → Lesson traceability result;
7. each finding's disposition: `accepted`, `deferred`, or `rejected`, with a
   reason and owner;
8. localization disposition, if applicable;
9. pedagogical readiness: `ready`, `ready_with_changes`, or `not_ready`;
10. explicit boundaries: no technical execution verdict, mastery verdict,
    placement decision, publication authority, or Theme-scope mutation.

## Readiness rule

A Theme-local record may say `ready` only when the complete Lesson sequence is
traceable to the Theme outcome, the Theme is traceable to Module criteria,
required Profession reviews are complete, and the Lecturer and Dean have
completed their respective final-control and readiness decisions.
