# Theme 1 — Instructional Assistant material review

**Reviewer:** Instructional Assistant Profession, resolved University-wide Worker context

**Localization pass:** Translator Profession completed the Ukrainian
native-language and anglicism audit after Lecturer source finalization. The
existing pedagogical review preceded this localization pass.

**Materials reviewed:** `THEME.md` and the four learner-facing Lessons in this
directory, plus the optional Teacher/Lab evidence instructions.

**Review stage/version:** final Student-specific correction pass after the
forward-motion redesign; four-Lesson package revision 2.

**Student feedback signals:** The Student identified repetition of Course Entry
material and excessive written evidence. Those signals were reviewed
separately from learning evidence; no Student mastery verdict is issued here.

## Intended learner outcome

The Student can build and explain a small Python component with explicit
function, data, and entry-point boundaries, then verify ordinary, boundary,
and failure behavior with a controlled change.

## Strengths to preserve

- the Theme has exactly four Lessons and a visible stop condition;
- vocabulary is introduced before it is required in tasks;
- the sequence moves from function responsibility to file separation and then
  integration;
- practical tasks request compact evidence and require the accepting Worker to
  inspect and run code;
- the localized Lessons explain necessary code names, commands, and output
  labels in Ukrainian.

## Findings and dispositions

1. The first Lesson used technical output labels in English without initially
   identifying them as exact strings. **Accepted:** the Lecturer marked them as
   exact output strings and explained their role.
2. The first Lesson introduced “контрольована зміна” only in the task.
   **Accepted:** the Lecturer added a plain-language definition before the
   task.
3. The sequence needed an explicit final boundary to prevent indefinite
   Lesson creation. **Accepted:** the Theme now defines four Lessons, a final
   checkpoint, and a stop condition.
4. Lesson 1 used the code identifier `label` before explaining its meaning in
   the selected language. **Accepted:** the Lecturer added the term to the
   vocabulary section and explained its role before the example and task.

## Evidence burden

The requested evidence is limited to artifact paths, commands, compact run
results, a short explanation, and one controlled change. Full terminal logs,
program maps, and long reports are not required.

## Pedagogical readiness

`ready` after the Lecturer applied the listed findings and completed the final
control review, including the post-routing Worker-context audit.

## Correction pass

The material-owner → Instructional Assistant review was rerun for the current
correction pass. The following findings were confirmed and resolved by the
Lecturer:

1. **Lessons 2–3 — practical input/output contract.** The required inputs,
   expected result, failure cases, command, and accepting Worker's run-and-
   inspect duty are now explicit.
2. **Lesson 4 — failure acceptance boundary.** The checkpoint now states that
   invalid cases must remain visible failures and that a textual claim cannot
   replace inspection and execution of the artifact.
3. **Lessons 1–4 — provenance consistency.** Each Lesson now has an explicit
   original-material statement and separates provenance from AI-use disclosure.
4. **Theme frame — handoff clarity.** The Theme now states the required
   Contract 1 and Contract 5 inputs/outputs and preserves the four-Lesson stop
   condition.

The correction pass did not add a Lesson, alter Theme criteria, or change the
Module boundary.

## Localization disposition

`localized`: learner-facing prose is Ukrainian. English remains only in exact
code/API names, commands, file paths, required output strings, and identifiers
that the Student must see or type. Unnecessary English prose introduced during
the prior correction was replaced with Ukrainian wording.

Technical correctness, code execution, assessment validity, and academic
placement were not reviewed by this report.

## Student-specific review correction

The earlier `ready` signal is valid only for generic pedagogical clarity. It
is not a Student-specific delivery approval because the review did not receive
the Student's prior diagnostic evidence or an explicit new-evidence delta. The
Lesson 1 task substantially repeats the Course Entry Python diagnostic and is
therefore `not_ready` for this Student until the Lecturer redesigns or skips
the repeated work, then reruns Contract 5 with the permitted prior evidence.

## Final Student-specific correction review

**Review stage:** corrected Theme package before delivery

**Permitted prior context:** Course Entry evidence already demonstrates basic
function decomposition, parameters/returns, input conversion, range/error
handling, command execution, and reading runtime errors.

**Forward-motion findings:**

1. **Lesson 1 — accepted correction.** The score/temperature diagnostic is no
   longer reused. The new task isolates pure calculation and formatting with
   prepared data and no terminal I/O.
2. **Lesson 2 — accepted correction.** Parsing is limited to the CLI boundary;
   the new evidence is direct reuse of the same component from code and CLI.
3. **Lesson 3 — accepted correction.** The prior diagnostic is not rewritten;
   the new evidence is import isolation and a separate entry-point module.
4. **Lesson 4 — accepted correction.** The checkpoint uses an unfamiliar
   meeting component and tests transfer, failure behavior, and one controlled
   change rather than repeating score/temperature cases.

**Sequence traceability:** accepted. Lesson 1 establishes the pure component;
Lesson 2 isolates the input boundary; Lesson 3 makes the module/entry-point
boundary explicit; Lesson 4 transfers the cumulative result to a new context
and returns the Theme checkpoint evidence. The sequence advances Module 1 Exit
criteria 1 and 2 without claiming the later Themes' criteria.

**Module → Theme → Lesson result:** Module Exit 1/2 map to the Theme criteria
for function, data, and entry-point boundaries; Lessons 1–4 produce the
cumulative evidence required by the Theme checkpoint and Contract 6 handoff.

**Evidence burden:** accepted. Each Lesson requests only artifact path,
command, compact observed results, and at most one short understanding check.
No long authorship narrative or repeated terminal transcript is required.

**Localization review:** accepted. Learner-facing prose is Ukrainian. English
remains only in code identifiers, commands, paths, and required literals.

**Pedagogical readiness:** `ready`

Technical execution and Student mastery remain the accepting Lecturer's
responsibility; this review does not issue either verdict.

## Current review pass — Lessons 2–4

**Workflow stage:** Lecturer source review → Instructional Assistant
pedagogical review

**Scope:** Lessons 2–4 of this Theme. Lesson 1 was reviewed separately after
the learner-facing/runtime-path correction. This pass does not change the
file-upload implementation.

### Lecturer handoff

The Lecturer supplied the complete learner-facing Lessons 2–4, the Theme
outcome and sequence, Ukrainian as the dialogue language, and the practical
run-and-inspect contract. No private Student state was needed for this generic
material review.

### Instructional Assistant findings

1. **Lesson 2 — `ready_with_changes`.** The phrase `evidence delta` is an
   unnecessary English term in learner-facing prose. `reusable-функція`, `CLI`
   and `REPL` either need native explanations at first use or should be
   replaced with clear Ukrainian wording. The phrase “короткий локальний
   перевірочний фрагмент” does not specify how the learner should perform or
   report that check.

2. **Lesson 3 — `ready_with_changes`.** The phrase `evidence delta` is again
   untranslated. `reusable-логіка`, `entry point` and `CLI-поведінка` mix
   English prose with Ukrainian; use “логіка повторного використання”, “точка
   запуску” and “поведінка командного запуску”, while retaining exact file
   names and commands where the learner must type them. The two-file evidence
   requirement is clear academically, but its delivery mechanism remains an
implementation handoff outside this review.

## Current correction pass — artifact delivery contract

**Lecturer disposition:** accepted within the approved four-Lesson Theme scope.

The learner-facing Lessons now distinguish local execution from submission:
the Student may work in any local directory, but must transmit the named `.py`
files through the client Artifact control. Local `homeworks/...` paths are no
longer requested as evidence. Lessons 1–4 now state exact artifact names,
compact command/results, and that Lecturer inspection runs the transmitted
files.

The Instructional Assistant found no Theme-scope or learner-outcome change.
The technical client/API handoff was expanded to accept multiple `.py` files
so Lessons 3–4 remain executable. The repeat pedagogical review after the
related structured-data material pass found the wording and evidence burden
clear; this correction pass is `ready`.

3. **Lesson 4 — `not_ready`.** `entry point` and `reusable-логіка` require the
   same language correction. More importantly, `format_meeting_report()` is
   required to return a “короткий звіт”, but the material does not define its
   exact learner-facing format or the expected ordinary result for `3`
   participants and `4` questions. The accepting Lecturer cannot compare the
   output consistently until that contract is stated.

4. **Cross-Lesson boundary check.** No private repository path, Student-ID,
   container, volume, database, or internal runtime storage detail was found
   in Lessons 2–4. The paths and commands present are logical learner-facing
   paths or commands the Student must use.

### Lecturer dispositions and correction pass

The Lecturer accepted all applicable findings and corrected the Lessons within
the approved Theme scope:

- Lesson 2 now uses Ukrainian wording for the learning result and function
  reuse, replaces unexplained `REPL` with an understandable Python check, and
  clarifies the direct-call evidence.
- Lesson 3 now uses “логіка повторного використання” and “точка запуску” in
  learner-facing prose while preserving exact file names and commands.
- Lesson 4 now defines the exact report format, the expected ordinary result
  (`27` minutes), the invalid-argument behavior, and the controlled-change
  result (`30` minutes).

The Instructional Assistant reran the complete pedagogical review after these
corrections. The findings are resolved, no internal runtime information was
introduced, and the package is `ready` for delivery. The review does not alter
the Theme criteria, add a Lesson, or decide the deferred file-upload
implementation.

### Final artifact-delivery control review

The Translator audited the Ukrainian learner-facing wording after the artifact
delivery correction. Unexplained `upload` wording was replaced with Ukrainian
wording for file transfer; exact technical identifiers and the client label
`Artifact` were retained. The localization result is `localized` and does not
change the learning path, criteria, or evidence burden.

The Lecturer then completed final source control: Lessons 1–4 name the files
to transmit through the client Artifact control, do not request a local
`homeworks/...` path, and remain within the approved Theme scope. The package
is `ready` for the next real Student artifact-delivery run.

### Rector policy recheck

After the University-wide Artifact evidence boundary was accepted, the
Lecturer rechecked this Theme package. Lessons 1–4 already require the client
Artifact control for executable files and keep dialogue explanations separate
from file evidence; no Lesson criterion or sequence change is needed. The
Translator confirmed that the Ukrainian learner-facing wording remains
equivalent and retains the exact `Artifact` UI label. The package remains
`ready` under the new University-wide boundary.
