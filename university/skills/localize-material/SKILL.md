---
name: localize-material
description: Localize bounded learner-facing material into the selected dialogue language with native phrasing and controlled technical terminology.
class: learning
---
# Localize material

Localize a prepared learner-facing artifact into the selected dialogue language
without changing its academic meaning, technical behavior, scope, criteria, or
evidence burden.

## Contract

Input must include the active Translator Profession and Worker appointment,
exact source path or bounded draft, parent Course/Module/Theme/Lesson scope,
selected dialogue language, intended learner context, outcome, criteria,
terminology that must remain exact, and applicable AI/tool-use policy.

The source must already have passed the normal Instructional Assistant review
and the Lecturer's disposition/final source control. Return the localized
artifact or bounded patch, terminology decisions, retained-English
justifications, unresolved semantic questions, and one signal:
`localized`, `localized_with_questions`, or `not_localized`.

Also state whether the localization materially changes explanations,
instructions, evidence burden, or learner path. This signal determines whether
a targeted second Instructional Assistant review is needed.

Preserve code/API names, commands, file paths, URLs, source titles, required
identifiers, outcomes, criteria, scope, and evidence burden. Do not add or
remove Lessons, rewrite technical facts, assess the Student, approve
publication, or replace Instructional Assistant review.
