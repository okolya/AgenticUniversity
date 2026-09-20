# Agentic University

This is the public Agentic University root repository and runtime workspace.

- `university/` — public University: behavior, agents, reusable knowledge, courses and learning materials.
- `students/` — private repository: only student registry and private learning-process state.
- Root AI files are runtime-managed symlinks to the canonical `university/` content.

Start:

```bash
make init
make workspace-check
```

The root repository owns orchestration and public University content under
`university/`. Students owns only private educational state and is ignored by
the root repository.
