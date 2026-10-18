# 0013. Formative lexicon track in Student state

Status: Accepted
Date: 2026-10-18

## Context

The German bridge course (`german-between-b1-and-b2`) uses short
`Lektionslexik` games and recycle (plan v0.0.13). Delivery still relied on
session memory or free-form Notes for lemma status (`new` / `recycling` /
`weak` / `stable`). Notes and Evidence are the wrong surfaces: Notes are
Dean/Rector metadata; Evidence is append-only independent assessment and
must not become a micro-vocab ledger. Recycle and Teacher vocab gym need a
durable per-Student item track with `status` and `next_due` that is not a
mastery verdict and not a Module Exit criterion.

## Options considered

- **Keep status in Notes** — misuses Note authority; hard to query due items.
- **Record Spiel outcomes as Evidence** — pollutes assessment Evidence;
  Lecturer/Teacher must not invent mastery through Evidence.
- **Host-only or client flashcard DB** — breaks CLI/agent-only delivery and
  duplicates the core Student store (ADR 0012).
- **Typed `lexicon_item` entity in the core Student state store** — formative
  only; Lecturer/Teacher write; queryable due list; no Exit coupling.

## Decision

The Student state contract gains a formative **`lexicon_item`** entity,
implemented in the core SQLite store (ADR 0012).

- Fields (v1): `lemma`, `article` (`der` | `die` | `das` | `none`), optional
  `collocation`, `status` (`new` | `recycling` | `weak` | `stable`),
  `introduced_lesson_ref`, `last_check`, `next_due`, `streak_ok`, optional
  text `mnemonic`, `course_id`. Nullable `image_ref` / `audio_ref` stubs may
  exist for forward compatibility but are unused in v1.
- Writers: **Lecturer** and **Teacher** for the appointed Language Faculty
  course delivery and vocab gym. They write formative lexicon status only;
  they do not mark verified mastery. Learning Analyst and Examiner do not
  own routine lexicon writes. Lexicon rows never satisfy Module Exit
  criteria by themselves.
- Operations: `upsert-lexicon`, `list-lexicon`, `list-lexicon-due`,
  `record-lexicon-check` (`ok` | `fail`) on the CLI store. Every write
  carries acting Profession, Workflow, and date. No lexicon row exists
  without a registered Student.
- Spacing v1 (items only): Spiel pass → `recycling` / due next Lesson slot;
  fail → `weak` (gym); two clean Recycle oks → `stable` (Theme-Pack or
  +3 slots); fail while `stable` → `weak`. `Lexik-Schreiben` stays
  in-lesson Festigung and is **not** stored or spaced.
- Scope: course-local convention for Language Faculty delivery that uses
  this track; not a University-wide vocabulary protocol for other Faculties.

## Consequences

- Recycle and Teacher gym can call `list-lexicon-due` / `record-lexicon-check`
  instead of inventing status from chat memory.
- Contract, JSON Schema, authority policy, and store tests must name the
  entity and writers explicitly.
- Rich media practice (images, audio, client shell) stays out of scope; see
  documentation `planning/future-ideas/language-lexicon-rich-practice.md`.

## Scope boundary

This decision adds one formative entity and its store operations. It does
not change Module Exit Contracts, Examiner instruments, Evidence append
rules, Note authority, or host-side databases beyond implementing the same
contract operations if a host mirrors the store.
