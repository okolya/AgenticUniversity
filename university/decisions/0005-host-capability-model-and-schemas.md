# 0005. Host capability model and machine-readable schemas

Status: Accepted
Date: 2026-09-30 (recorded retroactively for plan v0.0.2)

## Context

ADR 0001 separates the core from hosts and ADR 0002 defines the Student state
contract in prose. Hosts still differ in what they can do (execute code, store
artifacts, persist public content), and a prose-only contract leaves the state
shape ambiguous. ADR 0002 noted that a machine-readable schema was still needed;
ADR 0004 did not list schemas in the manifest.

## Options considered

- **Assume every host is like the CLI** — simplest, but a bot cannot execute
  code or write to the core, so Workers would overclaim.
- **Per-host forks of the rules** — flexible, but breaks the single core.
- **Declared host capabilities with stated fallbacks, plus a JSON Schema for
  Student state listed in the manifest** — one core, explicit differences.

## Decision

Hosts declare capabilities (code execution, artifact storage, private state
store, public content persistence); Workers do not assume an undeclared one, and
`policies/practical-work.md` and `policies/runtime-portability.md` state the
fallbacks. `schemas/student-state.schema.json` with a synthetic example is the
machine-readable form of the state contract, listed under `schemas` in
`MANIFEST.md`; `make check-manifest` validates the example. Where schema and
contract prose disagree, prose and the authority policies govern. The schema does
not enforce which Profession may write which entry; hosts enforce that
(`protocols/host-conformance.md`). This extends ADR 0002 and ADR 0004.

## Consequences

- Adding an entity or field means updating the contract prose, the schema, and
  the example together.
- Hosts follow `protocols/host-conformance.md` before serving Students.
- Revisit if write authority per Evidence kind should be expressed in the schema.
