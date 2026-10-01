# Theme 2 — Preparation record

- **Course:** AI Engineering
- **Module:** Python AI Engineering
- **Theme:** Structured data and validation
- **Sequence:** bounded four-Lesson sequence
- **Dialogue language:** Ukrainian
- **Responsible Profession:** Lecturer
- **Resolved appointment:** active Engineering Faculty Lecturer appointment;
  corrected Theme-specific Contract 1 handoff recorded
- **Review cycle:** Student-specific correction pass, final readiness review

## Explicit profession handoffs

### Dean → Lecturer (Contract 1)

- **Target Profession:** Lecturer
- **Resolved appointment context:** active Engineering Faculty Lecturer
  appointment; no separate named-worker runtime is created
- **Purpose:** prepare and refine the finite Theme 2 Lesson sequence
- **Scope:** AI Engineering → Python AI Engineering → Theme 2; Lessons 1–4 only
- **Input:** approved outcome, Success Criteria, exclusions, checkpoint, stop
  condition, four Lesson slots, Module Exit criteria 4/6, prior Theme 1
  boundary evidence, and the cumulative sequence map
- **Output:** learner-facing Lesson materials, formative evidence contracts,
  specialist-contribution requests where justified, and Contract 6 Dean handoff
- **Boundary:** no fifth Lesson, no database/model-training expansion, no
  Module/Course or placement decision

### Lecturer → Instructional Assistant (Contract 5)

- **Target Profession:** Instructional Assistant
- **Resolved appointment context:** active University-wide pedagogical-review
  appointment; no separate named-worker runtime is created
- **Purpose:** complete pedagogical review before delivery
- **Input:** all four corrected Lesson materials, Theme outcome/criteria,
  cumulative sequence map, Ukrainian dialogue language, practical
  run-and-inspect contract, and evidence burden
- **Output:** bounded review report with strengths, vocabulary/progression
  findings, coherence findings, unresolved questions, and readiness signal
- **Boundary:** no editing, technical correctness verdict, Student assessment,
  publication approval, or Theme scope change

### Lecturer → Translator (post-final-review localization handoff)

- **Target Profession:** Translator
- **Resolved appointment context:** active University-wide Translator
  appointment; no named-worker runtime is created
- **Purpose:** after Assistant findings and Lecturer final source control,
  audit and localize learner-facing Theme 2 material into natural Ukrainian
  without unnecessary anglicisms
- **Input:** four Lessons, selected dialogue language Ukrainian, exact JSON/API
  names, commands, paths, output strings, and Theme criteria
- **Output:** localized wording and terminology decisions returned to Lecturer
- **Second review trigger:** only if the localized wording materially changes
  the learner path, instructions, evidence burden, or creates a clarity risk
- **Boundary:** no change to code identifiers, criteria, scope, evidence burden,
  or publication status

## Approved frame

- **Outcome:** Student defines a small data shape, validates it, transforms it,
  and reports invalid data without silently changing its meaning.
- **Criteria:** explicit fields/types; valid and invalid paths tested;
  serialization preserves structure; limits of validation explained.
- **Exclusions:** databases, model training, and new data domains.
- **Lessons:** read structured data; validate shape/types; transform and
  serialize; final Theme checkpoint. The dependency chain is explicitly
  `read → validate → transform → serialize`.
- **Stop condition:** after Lesson 4, return evidence to Dean; no fifth Lesson
  without a new Dean decision.

## Cumulative traceability map

| Module criterion | Theme criterion | Lesson delta | Next result |
|---|---|---|---|
| Exit 6 | define and preserve structured data shape | Lesson 1 reads `service.json` and preserves Python types | Lesson 2 schema validation |
| Exit 4 and 6 | validate fields, types, and invariants | Lesson 2 distinguishes valid and invalid service objects | Lesson 3 safe transformation |
| Exit 4 and 6 | transform and serialize without semantic loss | Lesson 3 runs `read → validate → transform → serialize` | Lesson 4 integrated component |
| Exit 4 and 6 | demonstrate complete bounded behavior and limits | Lesson 4 integrates prior artifacts and returns checkpoint evidence | Contract 6 Dean handoff |

## Lecturer teaching-intent plan

The sequence moves from observing JSON/Python type mapping to explicit
validation, then to a non-mutating transformation and serialization, and ends
with one bounded component that integrates all four operations. Each practical
task requests only the artifact path, run command, compact required-case
results, and a short explanation exposing the declared criterion.

The prepared material is original University content. The research gate found
no need to replace it with an external source; exact external provenance is
therefore not applicable. Student-provided materials have not been supplied.

## Specialist contributions

- **Teacher Profession:** optional and trigger-based; request only for a
  concrete reinforcement gap in reading, type checks, or error explanation.
- **Laboratory Specialist Profession:** optional; the final Lesson already
  contains the bounded implementation task, so a separate Lab is not required
  unless the Lecturer identifies a practical gap.
- **Learning Analyst Profession:** not requested; no independent measurement
  request is present.
- **Examiner Profession:** not requested; this is not a Module examination.
- **Instructional Assistant Profession:** complete review recorded in
  `material-review.md`; findings were incorporated by the material owner.
- **Translator Profession:** completed the post-final-review
  Ukrainian native-language and anglicism audit; exact technical identifiers
  were preserved and no material learner-path change was reported.

## Lecturer final control review

After the material-review changes, the complete package was reread against the
Theme outcome, criteria, exclusions, vocabulary progression, practical
run-and-inspect contract, AI-use wording, and stop condition. No new Lesson,
Theme criterion, or Module scope was added.

## Handoff to Dean

- **Completed slots:** Lessons 1–4 prepared.
- **Evidence status:** learner-facing evidence contracts are defined; no
  Student evidence exists in this operation.
- **Student delivery gate:** existing Student Module 1 entry and coverage plan
  remain governed by the private Student workspace; this public record carries
  only the reusable Theme sequence and its criteria.
- **Staffing handoff:** the Contract 1 Dean → Lecturer assignment context is
  recorded above and resolves to the active Engineering Faculty Lecturer
  appointment.
- **Decision required:** Dean confirmation that the cumulative Theme map is
  aligned to Module Exit criteria 4 and 6.
- **Recommendation within Lecturer authority:** proceed with the corrected
  four-Lesson sequence after Dean confirmation; no additional worker is
  required unless a concrete gap, Lab need, independent measurement, or exam
  trigger appears.

## Dean readiness decision

`ready` — the corrected four-Lesson sequence is aligned with Module 1 Exit
criteria 4 and 6, has explicit cumulative dependencies, and has passed the
Instructional Assistant pedagogical review and Translator language audit.
Delivery remains subject to the accepting Lecturer's run-and-inspect duty and
the normal Contract 6 handoff after Lesson 4.
