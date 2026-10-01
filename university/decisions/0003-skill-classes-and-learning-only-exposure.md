# 0003. Skill classes; hosts expose only learning Skills to Students

Status: Superseded by 0006
Date: 2026-09-30 (recorded retroactively for plan v0.0.1)

## Context

Skills mix Student-session capabilities, staffing operations
(`appoint-worker`, `register-worker`), and maintenance tooling
(`session-bootstrap`, `plan-authoring`, `plan-completion`). A public host must
not offer the last two kinds to Students.

## Options considered

- **No classification; host decides per Skill** — every host repeats the
  judgment and can get it wrong.
- **Two classes (learning, administrative)** — leaves development tooling
  unclassified.
- **Three classes: learning, administrative, maintenance**, recorded in the
  manifest.

## Decision

Every Skill has one class in `MANIFEST.md`. Only `learning` Skills are exposed
in Student sessions. `administrative` and `maintenance` Skills were CLI and
maintainer only under this superseded decision. ADR 0006 replaces
`maintenance` with the four-class model and adds explicit development and
technical boundaries.

## Consequences

- Every new Skill must be classified; `make check-manifest` enforces it.
- Skill classes do not change authority: a Skill still never owns a decision.
- See `skills/README.md`.
- Revisit if a class needs finer exposure rules per host.
