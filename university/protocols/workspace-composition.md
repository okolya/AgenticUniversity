# Workspace Composition Protocol

Expected layout:

```text
workspace/
├── university/   # public Git repository
├── students/     # private Git repository
├── AGENTS.md     -> university/AGENTS.md
├── CLAUDE.md     -> university/CLAUDE.md
├── CODEX.md      -> university/CODEX.md
├── CURSOR.md     -> university/CURSOR.md
├── .agents/      # University-managed runtime links
├── .claude/      # University-managed runtime links
├── .codex/       # University-managed runtime links
└── .cursor/      # University-managed runtime links
```

The workspace root is a composition directory, not the authoritative Git repository. Runtime agents execute from the workspace root so they can read public University knowledge and the explicitly selected private Student state.

The Students repository has no AI/runtime files of its own. All runtime behavior is supplied by University templates/adapters through workspace-root links.

A worker operating for one student receives only that student's permitted private context. Physical proximity of other students in the same private repository does not grant contextual access.
