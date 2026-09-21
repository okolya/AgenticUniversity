---
name: review-learning-material
description: Review prepared learning material for pedagogical coherence, gradual vocabulary introduction, and learner-facing clarity before publication; do not use it as a fact, code, or academic-scope correctness review.
---

# Review learning material

Use this Skill inside the `Instructional Assistant` Profession when a Worker
requests a complete pre-publication pedagogical review of a Lesson, exercise,
lab, diagnostic, assessment brief, explanation, or other learner-facing
material.

## Inputs

- material path or bounded draft;
- intended learner/context and declared outcome;
- relevant Theme/Module scope and success criteria;
- workflow stage and the responsible Worker;
- for an assessment artifact: assessed criteria, authorized assessment Worker,
  learner-facing versus assessor-only sections, and applicable AI-use mode;
- optionally, the Student's response to the material, including comments or
  criticism, with only the permitted context.

Read only the material and minimum surrounding context needed to judge
coherence. Do not read private Student state unless the caller explicitly
provides permitted context relevant to learner level or prior evidence.

## Review procedure

1. State the intended learner outcome in plain language.
2. If a Student response is provided, separate it into: explicit material
   criticism, statements of confusion, preferences/requests, observed learning
   evidence, and unrelated content. Return the first three as feedback signals;
   do not evaluate the learning evidence.
3. Trace the material from prerequisite knowledge through explanation, example,
   practice, and requested evidence.
4. List domain terms, abbreviations, foreign-language terms, symbols, and code
   vocabulary introduced by the material. Mark each as explained before use,
   explained at first use, inferable with sufficient context, or unexplained.
5. Check that new terms are introduced in a manageable order and reused with
   stable meaning. Pay special attention to words used in tasks or evidence
   instructions that were not prepared in the teaching section.
6. Check the selected dialogue language. In a localized Lesson, report
   unnecessary anglicisms and mixed-language prose as findings. Do not remove,
   rewrite, or enforce a language change. Identify exact code/API names,
   commands, file paths, source titles, URLs, and required identifiers that may
   remain, and recommend an explanation in the selected language before use.
7. Check that each practical task states the action, exact target, expected
   result, comparison/failure case, and evidence format without requiring the
   learner to infer a hidden task contract.
8. Check alignment between outcome, examples, practice, and evidence request.
9. For a diagnostic or assessment artifact, check that purpose, target
   capability, task, inputs, outputs, failure cases, evidence requirements,
   bounded scope, allowed tools, and learner/assessor boundaries are explicit.
   Check that the document does not coach the learner or accidentally assess a
   different capability.
10. For an executable practical task, check that the accepting Worker is
    instructed to inspect and run the submitted code, and that the requested
    evidence is minimal: artifact, command, compact required-case results, and
    only a short understanding check. Flag long reports, repeated traces,
    program maps, or descriptions that do not expose a declared criterion.
11. Report strengths and findings from the entire artifact with exact
   headings/locations and concrete revision suggestions. Do not create, edit,
   remove, or publish the source material.

## Explicit non-goals

This Skill does not evaluate Student knowledge, mastery, or assessment
evidence. It also does not verify factual correctness, code execution, source
provenance, copyright, security, assessment validity, scoring validity,
independence, or Course/Module/Theme authority. Flag a concern for the
responsible owner instead of resolving it as fact. It does not publish,
approve, or create a final readiness verdict.

## Output frame

```text
Instructional Assistant review

Material:
Learner/outcome:
Workflow stage:

Student feedback signals:
- Explicit criticism:
- Confusion signals:
- Preferences/requests:
- Learning evidence: not evaluated by this Skill; passed to Lecturer

Strengths to preserve:
- ...

Vocabulary and progression:
- term / location / status / learner risk / suggested explanation

Other coherence findings:
- location / observed gap / learner risk / suggested improvement

Questions for responsible Worker:
- ...

Pedagogical readiness: ready | ready_with_changes | not_ready
Technical/factual review: not performed by this Skill
```
