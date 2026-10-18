# Agentic University Core

This repository is the public, standalone University knowledge core.

- `university/` — canonical academic knowledge, policies, workflows, Skills,
  Professions, Workers, Courses, and public checks.
- `agent-runtime/` — provider-neutral runtime adapters for the public core.
- `scripts/` — core integrity, manifest, and documentation-link checks.
- `students/` — private data directory holding the SQLite Student state store
  and `homeworks/` — private Student working files, when this core is used as a
  standalone learning workspace. Both ship empty with a README; their content is
  ignored by Git.

The core does not depend on private planning, workspace orchestration, or
component repositories. Student state, when used, lives in the SQLite store at the
core-relative `students/` data directory and is never committed to the public
repository. A larger
workspace may compose this core through relative links and namespaced runtime
resources.
