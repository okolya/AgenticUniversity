# Artifact Verification Protocol

Reports from Workers, Skills, and delegated runtime agents are operational
claims, not authoritative proof that a file, state, or result has the
reported contents.

Before presenting a result or relying on it for an academic decision, the
calling runtime must independently verify material claims against the
canonical artifact or an appropriate read-only tool result.

## Required verification

Verify the smallest relevant surface for the claim:

- file contents — read the canonical file;
- file creation or modification — inspect the file and Git status/diff;
- repository or boundary — verify the relevant Git root;
- generated output — inspect the output using the applicable parser/renderer;
- test or validation result — run or inspect the named focused check;
- Student state — read the permitted private state after the operation;
- public academic state — read the canonical `university/` artifact after edits.

Do not infer a fact from a filename, a Worker report, a previous summary, or
the mere presence of a repository path. Do not claim that a check passed when
only the delegated report says so and no permitted verification was performed.

If verification is unavailable, state the claim as unverified and stop short
of presenting it as fact. Verification confirms the artifact or result; it
does not grant the Worker authority to make a decision outside its scope.
