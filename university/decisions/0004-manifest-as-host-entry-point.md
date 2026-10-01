# 0004. Manifest as the single host entry point

Status: Superseded by 0006
Date: 2026-09-30 (recorded retroactively for plan v0.0.1)

## Context

Workers were discoverable only by reading `staff/REGISTRY.md` and Faculty
`STAFF.md`; other entities only by scanning the tree. A host needs one stable
entry point that lists what exists.

## Options considered

- **Hosts scan the tree** — no new file, but fragile and unbounded in context.
- **Extend `staff/REGISTRY.md`** — covers Workers only.
- **Dedicated `MANIFEST.md`** with a constrained front matter, checked against
  the directory contents.

## Decision

`university/MANIFEST.md` lists Professions, Workers, Skills (with class),
workflows, policies, protocols, Faculties, Courses, and the startup entry
points. `make check-manifest` fails when it differs from disk; the pre-commit
hook and `make init` run it. Worker records stay canonical; the registries are
equivalent CLI discovery indexes. There is no separate core version: hosts pin
by Git tag or commit. ADR 0006 supersedes the manifest format and class
details with manifest v2 and structured dependencies.

## Consequences

- Adding or removing a listed entity requires a manifest update in the same
  commit.
- Appointment workflows must remind about `make check-manifest` (plan v0.0.2).
- Revisit when a real release needs an explicit core version number.
