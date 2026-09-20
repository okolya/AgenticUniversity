# Agentic University

This is the runtime workspace.

- `university/` — public University: behavior, agents, reusable knowledge, courses and learning materials.
- `students/` — private repository: only student registry and private learning-process state.
- Root AI files and runtime directories are symlinks owned by `university/`.

Start:

```bash
cd university
make init
make workspace-check
```

University owns behavior and reusable knowledge. Students owns only private educational state. The workspace composes both.
