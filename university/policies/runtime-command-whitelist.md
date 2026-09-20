# Runtime command whitelist

This is the University-owned allowlist for the read-only bootstrap surface.
It describes the commands a runtime may use to initialize a session without
asking the Student to approve each individual file read.

The list is deliberately narrow and applies only after the runtime has started
in the workspace root and confirmed the repository boundary.

## Workspace bootstrap

- `pwd`
- `test -f AGENTS.md`
- `test -d university`
- `test -d students`
- `git rev-parse --show-toplevel`

## University read-only context

At the workspace root, the generated Codex Skill path is
`.codex/skills/university-rector-startup`; the canonical source is
`university/skills/rector-startup`. Never use `university/.codex/...` as a
workspace-root path.
After routing to the `university/` repository, the runtime may read the
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
