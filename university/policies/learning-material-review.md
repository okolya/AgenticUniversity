# Learning Material Review Policy

Learning material must be understandable as a guided learning experience, not
only correct as a collection of facts or instructions.

## Required review path

Before a new or materially revised learner-facing Lesson, exercise, lab,
diagnostic, quiz, assessment brief, or explanation is published or delivered:

1. The responsible Worker identifies the material, artifact type, learner
   context, intended outcome, scope, assessment/learning criteria, and workflow
   stage.
2. The responsible Worker invokes the `Instructional Assistant` Profession for
   a complete pedagogical integrity review of the entire material. The request
   is made by Profession, never by calling a named Worker.
3. The Instructional Assistant returns a complete feedback report. It does not
   create, edit, remove, approve, publish, or certify the material.
4. For a learning artifact, the responsible Lecturer separately evaluates the
   Student response as learning evidence against the applicable criteria. For
   an independent assessment artifact, the authorized Learning Analyst owns
   assessment validity and conducts the assessment independently. The Assistant
   report must not replace either responsibility.
5. The responsible academic owner reviews the Assistant feedback, decides
   which changes are appropriate, and updates the material within the approved
   scope. The Lecturer remains the owner of Lessons and teaching material;
   the authorized assessment Worker owns an independent assessment artifact.
6. The responsible owner performs a complete final review of the entire
   prepared material, including outcome, prerequisites, vocabulary, sequence,
   tasks, evidence instructions, source notes, AI-use boundaries, and any
   learner-facing failure cases.
7. Only after that final owner review may the material proceed through the
   applicable publication/delivery process.

## Assessment and diagnostic artifacts

The Instructional Assistant must review the learner-facing part of every
diagnostic or assessment document before publication. The review must check
that:

- the assessed capability and purpose are stated in plain language;
- the task is self-contained and does not hide prerequisites, files, commands,
  inputs, outputs, failure cases, or evidence requirements;
- the learner can distinguish what must be implemented, what must be observed,
  and what must be explained;
- expected behavior is specific enough to produce comparable evidence without
  revealing a solution;
- the artifact clearly separates learner instructions from assessor-only
  criteria or verdict rules;
- the number of attempts, bounded scope, allowed tools, and AI-use mode are
  stated where they affect interpretation;
- the document does not accidentally teach, coach, lead, or assess a different
  capability than its declared target.

The Assistant reports clarity and pedagogical risks only. It does not approve
assessment validity, alter criteria, weaken independence, inspect private
evidence, or issue an assessment verdict. Technical correctness and assessment
design remain with the authorized owner.

## Progressive language

Terms must be explained before they are required for action, or introduced at
the point of first use with enough context for the learner's level. A term used
only in a task, code comment, variable name, or evidence template still counts
as learner-facing vocabulary. If a technical English term is retained, give a
plain-language explanation and keep its meaning stable.

## Localized material

When the material is localized, its explanations, headings, instructions,
questions, and evidence prompts use the selected dialogue language. Do not add
English words merely because they are common in technical writing. Keep exact
code/API names, commands, file paths, source titles, URLs, and required
identifiers unchanged only where the learner must see or type them; present
each with an explanation in the selected language. Mixed-language prose is a
review finding, not a teaching style. The Instructional Assistant reports the
finding and suggests a clearer Ukrainian formulation; it does not remove the
words, rewrite the material, or enforce a language change.

## Practical-task clarity

A practical task is complete only when it says what the learner must do, what
exact line/value/file or behavior is in scope, what result is expected, what
must remain unchanged or fail, and what evidence format to return. The
instructions must be readable as one bounded sequence rather than requiring
the learner to reconstruct the task from earlier examples.

The Instructional Assistant must also review evidence burden. For executable
tasks, flag full program maps, repeated terminal traces, duplicated expected
results, long reflection forms, and any other requested description that does
not expose a declared learning criterion. Recommend the smallest evidence set
that lets the accepting Worker inspect, run, and check understanding.

The task must state that the accepting Worker will inspect and run the submitted
code where executable behavior is part of the criterion. The task may request a
short explanation or a focused controlled change for understanding, but must
not make a long written report the proxy for authorship or comprehension.

## Responsibility boundary

The Instructional Assistant reports pedagogical and clarity risks across the
complete material. The responsible academic owner owns creation, revisions,
source selection, technical content decisions within the assigned scope, and
the final completeness check: Lecturer for teaching material, Learning Analyst
or Examiner for their authorized assessment artifact. A
review report is not proof that the material is factually or technically
correct, and it is not an assessment verdict.

Student criticism is a review input only. It may reveal a real clarity problem,
but it may also be a preference, a misunderstanding, or a request outside the
approved scope. The Lecturer must examine it and may reject it with a reason;
the Student cannot compel a material change. The Lecturer must explicitly
respond to every material criticism with one disposition: `accepted` (and what
was changed), `deferred` (and when/why it will be revisited), or `rejected`
(with the pedagogical or authority reason). A silent edit or silent omission
does not complete the review.
