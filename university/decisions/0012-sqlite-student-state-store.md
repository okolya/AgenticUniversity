# 0012. SQLite Student state store in the core

Status: Accepted
Date: 2026-10-18

## Context

ADR 0002 made Student state a host-neutral contract and allowed any store, but
the only store the core ships is the nested `students/` Git repository of
Markdown files. That store has three costs:

- Private Student data sits inside the public core's working tree. The
  directory is ignored, yet every clone carries the habit and the risk of a
  private repository next to public knowledge.
- A developer who only has an AI provider console must still create and track a
  second Git repository before the first Student session.
- Free-form Markdown makes reads, append-only Evidence, and verify-after-write
  depend on text parsing; the contract already names typed entities and
  operations.

A host with a service shell (`server-api`) keeps its own runtime database. The
core needs one store that works the same with and without that shell.

## Options considered

- **Keep the Markdown Git repository** — no work, but keeps the costs above.
- **A server database as the core store** — needs a service, so a console-only
  developer cannot run the core.
- **A SQLite store shipped with the core** — one file, Python standard library
  only, no service; the same operations run in both modes.

## Decision

The core ships a SQLite implementation of the Student state contract. Skills and
workflows keep naming contract operations, never store paths or SQL.

- Default location is the core-relative `students/` directory. It is a plain
  directory, not a Git repository, and stays ignored by the core. It holds the
  database file and the artifact files that Evidence references. An
  `AGENTIC_UNIVERSITY_STATE_DIR` override may point elsewhere.
- The store is created on first use. Missing state is still reported as
  missing; nothing is invented.
- The entities, operations, authority, and invariants of
  `protocols/student-state-contract.md` do not change. Evidence stays
  append-only and every write carries the acting Profession, Workflow, and
  date.
- A host with its own runtime database may implement the same contract; the
  core makes no database server a requirement.
- The Markdown `students/` repository is retired after a one-time import with a
  verified read-back.

## Consequences

- Private Student data no longer needs a Git repository next to public
  knowledge; history of Student state is the database's own append-only
  records.
- A console-only developer and a developer with the service shell run the same
  operations.
- Concurrent writers are limited to what SQLite allows (one writer at a time;
  a rollback journal, so a read-only mount can open the file). If several service processes or background workers write
  Student state, this decision is revisited; the contract lets the store change
  without changing Workflows.
- The CLI store mapping in the contract, the bootstrap and state-inspection
  scripts, the templates and the checks that name `students/` are rewritten in
  the implementation plan.
- Supersedes only the "private core-relative `students/` Git repository" part
  of ADR 0002; its contract decision stands.

## Scope boundary

This decision covers the core's shipped store. It does not change the academic
content, the authority policies, host-side databases, or how a host presents
Student sessions.
