# Workspace Composition Protocol

Expected layout:

```text
AgenticUniversity/
├── university/   # public academic source tree in the root Git repository
├── students/     # nested private Git repository
├── AGENTS.md     -> university/AGENTS.md
├── CLAUDE.md     -> university/CLAUDE.md
├── CODEX.md      -> university/CODEX.md
├── CURSOR.md     -> university/CURSOR.md
├── .agents/      # University-managed runtime links
├── .claude/      # University-managed runtime links
├── .codex/       # University-managed runtime links
└── .cursor/      # University-managed runtime links
```

The root is both the agent's starting directory and the authoritative public
Git repository. Runtime agents execute from the root, route public academic
work to `university/` and private state to `students/`, and verify the relevant
Git boundary before changes. The workspace runtime roots (`.agents`,
`.claude`, `.codex`, `.cursor`) are real directories populated with
namespace-scoped University links; they are not symlinks to whole repository
directories, because sandboxed runtimes may reject that boundary.

The Students repository has no AI/runtime files of its own. All runtime behavior is supplied by University templates/adapters through workspace-root links.

A worker operating for one student receives only that student's permitted private context. Physical proximity of other students in the same private repository does not grant contextual access.
