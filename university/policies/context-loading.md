# Workspace and repository context

The agent starts in the project workspace root. The workspace root is the
directory containing `AGENTS.md`, `university/`, and `students/`; it composes
the repositories and runtime links but is not itself a Git repository.

## Bootstrap

1. Run `pwd` and confirm `test -f AGENTS.md`.
2. Confirm the expected `university/` and `students/` directories exist.
3. Read the root `AGENTS.md` through its workspace-relative path.
4. Route the task to its owner before reading or changing files:
   - `university/` for public University knowledge, policies, workflows,
     Skills, professions, workers, and runtime adapters;
   - `students/` for private Student state.
5. Change into the selected repository and verify it with
   `git rev-parse --show-toplevel`.
6. Use paths relative to the workspace root or selected repository. Never put
   a machine-specific absolute path in a Skill, policy, workflow, or adapter.

The workspace-root `.agents`, `.claude`, `.codex`, and `.cursor` entries are
runtime aliases. They may be inspected as infrastructure when needed, but are
not editing targets. Changes belong in the owning repository and are exposed
through the normal workspace initialization/linking flow.
