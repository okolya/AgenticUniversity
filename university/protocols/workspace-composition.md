# Workspace Composition Protocol

Describes the CLI host composition. Other hosts compose the same core through
`MANIFEST.md` and keep Student state per `protocols/student-state-contract.md`.

Standalone core layout:

```text
university-core/
├── university/   # public academic source tree
├── students/     # ignored private Git repository
├── AGENTS.md     # core contract
├── CLAUDE.md     # core adapter
├── CODEX.md      # core adapter
└── CURSOR.md     # core adapter
```

The core is the agent's starting directory in standalone mode. Runtime agents
route public academic work to `university/` and private state to the
core-relative `students/`, and verify the relevant Git boundary before changes.
A larger workspace may add `.agents`, `.claude`, `.codex`, and `.cursor` runtime
roots and compose this core without changing these ownership boundaries.

The Students repository has no AI/runtime files of its own. All runtime behavior is supplied by University templates/adapters through workspace-root links.

A worker operating for one student receives only that student's permitted private context. Physical proximity of other students in the same private repository does not grant contextual access.
