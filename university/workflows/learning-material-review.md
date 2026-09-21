# Learning Material Review Workflow

Owner of revision and final readiness: the responsible academic owner. This is
the Lecturer for Lessons and teaching material, and the authorized assessment
Worker for an independent diagnostic or assessment artifact.
Pedagogical reviewer: the `Instructional Assistant` Profession.

The material-owner → Assistant request and the Assistant → owner report are
Contract 5 of `learning-interaction-contracts.md`; independent assessment
artifacts additionally use `assessment-contracts.md`.

## Handoff

The caller hands off:

- target material and exact path or bounded draft;
- artifact type: Lesson, exercise, lab, diagnostic, assessment brief, or other
  learner-facing material;
- intended learner and current learning context permitted for use;
- Lesson/Theme/Module outcome and relevant success criteria;
- workflow stage and responsible Worker;
- any known vocabulary, language, accessibility, or sequencing concern.
- the Student response, when available, as a separate source of feedback and
  learning evidence.

The caller invokes the Profession and supplies the workflow scope through the
Worker Activation Protocol. The routing layer resolves and attaches the
matching Worker context. The caller does not request a Worker by name.

## Complete Assistant review

The Instructional Assistant reads the complete material and the minimum
relevant context needed to review it, then returns the
`review-learning-material` output frame. Findings must distinguish:

- a term or prerequisite not prepared before use;
- an instruction or evidence request that is ambiguous;
- a sequence or cognitive-load issue;
- a scope/technical/factual concern that must be sent to another owner.

The Assistant does not create or edit the material and does not mark it
published.

## Assessment and diagnostic review

When the target is a diagnostic, quiz, assessment brief, or other independent
assessment artifact, the caller also supplies:

- the assessed criteria and purpose;
- the authorized assessment Profession/Worker;
- the permitted AI-use mode and evidence boundary;
- any assessor-only rubric that must not be exposed to the learner.

The Assistant reviews the learner-facing instructions as a complete path from
purpose to evidence. It checks that the task is bounded, self-contained,
unambiguous, language-appropriate, and does not accidentally reveal the
solution or introduce coaching. It separately flags any concern about
technical correctness, criterion validity, independence, or scoring for the
authorized assessment owner. Those concerns are not resolved by the Assistant.

## Dual-track Student response

When the review follows a Student response, process the response on two
separate tracks:

1. Lecturer track: the Lecturer evaluates demonstrated knowledge against the
   Lesson criteria and records the learning observation/evidence under the
   applicable assessment policy.
2. Assistant track: the Instructional Assistant extracts explicit criticism,
   confusion signals, and clarity observations, then reviews the complete
   material. It does not evaluate knowledge or decide whether the Student is
   correct about the curriculum.

The Lecturer receives both outputs. Only the Lecturer decides whether a change
to the Lesson is pedagogically justified and makes the change. Student input
cannot directly change the Lesson or any parent academic object.

For every extracted criticism, the Lecturer records and communicates a
disposition: accepted with the resulting change, deferred with a reason and
revisit point, or rejected with a pedagogical/authority reason. The Lecturer
must answer the criticism explicitly; making a related edit without addressing
the Student's stated concern is incomplete.

## Responsible-owner revision and control review

The responsible academic owner receives the report, decides which findings
apply, and alone makes revisions within the approved scope. The Lecturer does
this for Lessons and teaching material; the authorized assessment Worker does
it for an independent assessment artifact. The owner then rereads the complete
material from the learner's perspective and checks the whole artifact again,
not only lines mentioned in the report. The final check covers:

- outcome and prerequisite continuity;
- vocabulary introduced and explained progressively;
- explanations, examples, tasks, and evidence format;
- source/provenance and applicable safety/AI-use boundaries;
- consistency after edits and absence of accidental omissions.

If the Lecturer discovers a parent-scope or correctness issue outside the
review boundary, they hand it to the authorized owner rather than silently
changing that authority.

## Completion record

The responsible owner records the review outcome, material revision status,
remaining questions, and confirmation that the complete final control review
was performed. The Assistant report is feedback evidence; the owner's final
review is the readiness handoff.
