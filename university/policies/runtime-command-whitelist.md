# Runtime command whitelist

CLI hosts only; see `policies/runtime-portability.md` for other hosts.

This is the University-owned allowlist for the read-only bootstrap surface.
It describes the commands a runtime may use to initialize a session without
asking the Student to approve each individual file read.

The list is deliberately narrow and applies only after the runtime has started
in the host's active repository and confirmed the core boundary.

## Core bootstrap

- `pwd`
- `test -f AGENTS.md`
- `test -d university`
- `test -d students` (only when the selected workflow uses private Student state)
- `git rev-parse --show-toplevel`

For a composed workspace, the host resolves the core boundary first and then
uses the same core-relative `students/` path. A top-level workspace `students/`
path is not a fallback for core runtime instructions.

## University read-only context

In standalone mode, the generated Codex Skill path is
`.codex/skills/university-rector-startup`; the canonical source is
`university/skills/rector-startup`. A composed workspace may expose the same
generated path at its host root while sourcing it from
`university-core/university/skills/rector-startup`.
After routing to the core repository, the runtime may read the
canonical contract, constitution, activation protocol, active Profession and
Worker records, startup Skill, and public Faculty/Staff files required by it.

The runtime should load this bootstrap set in one bounded read operation where
the host supports command allowlisting. It must not scan the whole repository,
follow workspace runtime aliases as editing targets, or read private Student
state during startup unless the workflow explicitly permits it.

## Authority

This file is a project policy, not a host-level Codex permission database.
Provider-specific approval settings remain outside the repository. Adapters
must use these paths and commands as their portable project contract.

The bootstrap allowlist grants no Student or Worker capability by itself.
Technical operations require a separately declared host capability, an active
authorized Worker workflow, bounded targets, and post-operation verification.
