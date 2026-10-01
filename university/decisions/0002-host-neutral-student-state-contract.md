# 0002. Host-neutral Student state contract

Status: Accepted
Date: 2026-09-30 (recorded retroactively for plan v0.0.1)

## Context

Private Student state is one free-form Markdown file per Student in the nested
`students/` Git repository. Skills and workflows referred to that workspace
implicitly. A host without that repository has no defined state shape or
operations.

## Options considered

- **Keep the repository as the only store** — no change, but blocks any other
  host.
- **Define a database schema in the core** — concrete, but ties the core to one
  technology.
- **Define entities, operations, authority, and invariants; allow any store** —
  the `students/` repository becomes one implementation.

## Decision

Describe Student state as entities, operations, and invariants in
`protocols/student-state-contract.md`, with write authority exactly as in
`policies/student-state-authority.md`. There is no separate Mastery entity:
verified mastery is what verified Evidence supports. Skills name contract
operations, not paths.

## Consequences

- State Skills reference contract operations; the CLI store mapping is kept.
- Evidence is append-only; state refers to public entities, never copies them.
- The machine-readable schema is maintained alongside the public state
  contract in `schemas/`.
- Revisit if the free-form Markdown state proves too ambiguous for hosts.
