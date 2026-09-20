# Workspace and repository context

The agent starts in the AgenticUniversity root. The root contains `AGENTS.md`,
the public academic source under `university/`, and the nested private
`students/` repository; it is itself the public Git repository and runtime
composition root.

## Bootstrap

1. Run `pwd` and confirm `test -f AGENTS.md`.
2. Confirm the expected `university/` and `students/` directories exist.
3. Read the root `AGENTS.md` through its workspace-relative path.
4. Route the task to its owner before reading or changing files:
   - `university/` for public University knowledge, policies, workflows,
     Skills, professions, workers, and runtime adapters;
   - `students/` for private Student state.
5. Keep the root repository as the execution and Git composition root. Verify
   it with `git rev-parse --show-toplevel`; treat `university/` as its public
   academic source tree and `students/` as the nested private Git boundary.
6. Use paths relative to the root repository or selected ownership boundary. Never put
   a machine-specific absolute path in a Skill, policy, workflow, or adapter.

The workspace-root `.agents`, `.claude`, `.codex`, and `.cursor` entries are
runtime aliases. They may be inspected as infrastructure when needed, but are
not editing targets. Changes belong in the owning repository and are exposed
through the normal workspace initialization/linking flow.
