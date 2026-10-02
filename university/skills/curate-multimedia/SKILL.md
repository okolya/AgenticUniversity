---
name: curate-multimedia
description: Find and propose suitable audio, images, and video for a bounded Lesson or Theme outcome, with provenance, learner fit, accessibility, and fallback details.
class: development
---
# Curate multimedia

Find and curate external multimedia that materially supports an approved
Course/Module/Theme/Lesson goal. Return proposals to the responsible academic
Worker; this Skill does not insert, publish, approve, or replace material in a
Lesson.

## Contract

Input must include:

- active Worker and Profession;
- exact Course/Module/Theme/Lesson scope and approved slot;
- learner-facing outcome and applicable Success Criteria;
- selected dialogue/learning language and target level;
- intended classroom use and any known accessibility or delivery constraints;
- the minimum permitted Student context when the material is being prepared
  for a specific Student.

## Search and selection

1. Search public sources appropriate to the requested language and medium:
   audio, image, video, or a justified combination. Use the available search
   or browsing capability; if a source cannot be checked, mark it unverified.
2. Prefer sources that are stable, clearly attributable, accessible to the
   learner, and proportionate to the Lesson outcome. Search in Ukrainian,
   German, or Russian when that improves the learning fit; do not treat the
   search language as permission to change the learner-facing dialogue
   language.
3. Select only the smallest useful fragment. For video/audio, record exact
   timestamps, duration, transcript or caption availability, and the learner
   action. For images, record the exact asset and the intended observation or
   language task.
4. Check the source's visible access, attribution, reuse, and embedding
   conditions. Do not download, reproduce, or embed copyrighted or
   access-controlled material into University material beyond applicable
   rights. A precise link or permitted embed may be proposed instead.
5. Check foreseeable failure modes: broken or region-locked source, missing
   captions/transcript, unsuitable speed or language level, distracting
   content, tracking/login requirements, and dependency on a live platform.
   Propose a bounded fallback for any material needed by the Lesson.
6. Reject sources that add no meaningful evidence delta, require the learner
   to infer an unstated task, or expand the approved Theme/Lesson scope.

## Output

Return a bounded curation report containing one or more proposals. Each
proposal must state:

- `status`: `recommended`, `optional`, or `rejected`;
- `type`: `audio`, `image`, or `video`;
- exact URL or repository/file path and source title/creator;
- source role: `primary`, `supplementary`, or `reference-only`;
- language and approximate learner level;
- exact fragment: timestamp, page/section, or asset identifier;
- the Lesson outcome/criterion it supports;
- the learner action and expected observable result;
- accessibility details: captions, transcript, alt-text, or limitation;
- access/licensing/attribution notes;
- risks and a fallback source or original non-media alternative.

The report must distinguish facts verified from the source, reasonable
inferences, and unresolved checks. It must not present a source as approved
teaching material merely because it was found.

## Handoff boundary

The Lecturer decides whether and how to use a proposal, records exact
provenance in the Lesson, and remains responsible for the teaching design.
After insertion or adaptation, the complete learner-facing material follows
the normal `Instructional Assistant` review workflow. The Assistant checks
pedagogical coherence and clarity; it does not validate copyright, technical
source correctness, or publish the material. The Lecturer performs the final
source review and returns any parent-scope question to the Dean.
