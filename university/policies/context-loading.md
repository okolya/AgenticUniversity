# Workspace and repository context

This policy binds CLI hosts. Other hosts supply their own start-up under
`policies/runtime-portability.md`.

The standalone agent starts in the public core repository root. It contains
AGENTS.md, the public academic source under `university/`, and public runtime
adapters. A composed workspace may expose a separate workspace adapter and
private `students/` repository; those are not core dependencies.

## Bootstrap

1. Run `pwd` and confirm the parent repository contains AGENTS.md.
2. Confirm the expected `university/` directory exists.
3. Read the core AGENTS.md through its repository-relative path.
4. Route the task to its owner before reading or changing files:
   - `university/` for public University knowledge, policies, workflows,
     Skills, professions, workers, and runtime adapters;
5. Verify the core repository with `git rev-parse --show-toplevel`.
6. Use paths relative to the core repository or selected ownership boundary. Never put
   a machine-specific absolute path in a Skill, policy, workflow, or adapter.

The workspace-root `.agents`, `.claude`, `.codex`, and `.cursor` entries are
runtime aliases. They may be inspected as infrastructure when needed, but are
not editing targets. Changes belong in the owning repository and are exposed
through the normal workspace initialization/linking flow.
