# ADR 0009: Session role inference from the first message

- Status: accepted
- Date: 2026-10-01

## Context

`host-prompt-assembly.md` step 1 required resolving Student identity "from
the host authentication context... do not infer it from the current
message." A composed CLI workspace has no separate host authentication layer
— the only identity signal available at session start is the user's own
first message. Under the old rule, a CLI runtime had exactly one entry
branch (Student) and no way to start a Worker (academic staff) or Developer
(University maintenance) session without first bootstrapping as a Student
and then re-routing mid-session.

Observed failure: a session opened with "ти ректор bob" (intending Worker
Bob, Dean of Language Faculty, not Rector). The runtime had no branch to
resolve this from the message and fell back to a full blocking
multi-option question instead of a short inline correction. A later request
in the same session ("хочу розробляти матеріали як працівник") also had no
dedicated entry — the runtime had already committed to the Student branch.

ADR 0006 already defines four Skill/workflow classes — `learning`,
`administrative`, `development`, `technical` — and the manifest already
classifies `session-bootstrap` as `development`. The classification existed
before this decision; the problem was that `session-bootstrap`'s documented
procedure was written as a universal entry point, not scoped to the class it
was already given.

## Options considered

- **Keep requiring external host authentication, add nothing for CLI** —
  leaves CLI hosts permanently unable to start a Worker or Developer session
  without a manual workaround; rejected as the status quo that caused the
  observed failure.
- **Add a mandatory "Student or Worker?" question at the start of every
  session** — removes the ambiguity risk but forces a ritual question even
  when the first message already states the role unambiguously; rejected,
  the user explicitly asked against this shape.
- **Infer role and identity from the first substantive message, resolved
  against the existing public registries, with a single clarifying question
  only on genuine ambiguity** — chosen.
- **Invent a new Skill class for "session kind"** — rejected; the three
  session kinds (Student, Worker, Developer) already map onto three of
  ADR 0006's four classes (`learning`, `administrative`, `development`); a
  new class would duplicate that model instead of reusing it.

## Decision

A CLI/composed-workspace runtime resolves session identity and kind from the
user's first substantive message instead of requiring a separate host
authentication context. Three branches, each reusing an already-existing
mechanism:

1. **Student** — name/role resolves against `students/registry/REGISTRY.md`
   → `inspect-student-state` (`learning` class, unchanged).
2. **University Worker** — name/Profession/Faculty resolves against
   `university/staff/REGISTRY.md` → `profession-routing.md` +
   `worker-activation.md` (`administrative` class, unchanged mechanism, new
   entry path only).
3. **University Developer** — intent targets the University's own
   protocols/Skills/workflows/plans with no Student or Worker identity claim
   → `session-bootstrap` (`development` class — this is its existing
   manifest classification, not a new one).

A message that fails to resolve against either registry and carries no clear
Developer intent produces exactly one `AskUserQuestion`; this is the only
case that blocks on a question. An unregistered name with Student intent
routes to a registration sub-branch rather than a silent `missing` stop.

Message-derived identity is **impersonation-bound by the registries**: a
name is only treated as "this session is now that person" when it resolves
to exactly one entry in the matching public registry. Mentioning a third
party's name without claiming to be them must not be read as that party
authenticating. This decision applies to the CLI/composed-workspace path
only; a host with a real external authentication context keeps using that
context and ignores message inference.

## Consequences

- `host-prompt-assembly.md` step 1 names three resolution branches plus the
  single-ambiguity fallback, replacing the old Student-only branch.
- `session-bootstrap`'s documented scope narrows to match its existing
  `development` manifest class; it stops reading as a universal startup
  path.
- No new Skill class is introduced; `make check-manifest` continues to
  validate against the existing four-class model from ADR 0006.
- Branches 2 and 3 must never read Student state (`students/<id>/STUDENT.md`)
  unless a task explicitly names that Student — `student-state-authority.md`
  is unchanged and still governs that boundary.
- Revisit if a future host introduces a real external authentication
  context for the CLI path, or if message inference produces a
  misidentification incident the registry cross-check did not catch.
