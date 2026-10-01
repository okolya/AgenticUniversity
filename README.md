# Agentic University Core

This repository is the public, standalone University knowledge core.

- `university/` — canonical academic knowledge, policies, workflows, Skills,
  Professions, Workers, Courses, and public checks.
- `agent-runtime/` — provider-neutral runtime adapters for the public core.
- `scripts/` — core integrity, manifest, and documentation-link checks.
- `students/` — ignored private Student repository when this core is used as a
  standalone learning workspace.

The core does not depend on private planning, workspace orchestration, or
component repositories. Student state, when used, lives at the core-relative
`students/` boundary and is never committed to the public repository. A larger
workspace may compose this core through relative links and namespaced runtime
resources.
