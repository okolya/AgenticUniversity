# Student State Directory Template

This template defines the minimal private state directory used by the
University. The real directory is `students/` inside the public core (or the
directory named by `AGENTIC_UNIVERSITY_STATE_DIR`). It is a plain data
directory, not a Git repository: it holds the SQLite Student state store
(`university.sqlite3`). Student working files live in the sibling `homeworks/<student-id>/` directory, also ignored by Git.

The state directory MUST NOT contain agents, professions, skills, policies, workflows, course definitions, module definitions, teaching materials, reusable knowledge, or runtime adapters. Those belong to the public University.

It contains only facts and state specific to real students and their learning process. Reusable, depersonalized knowledge created during learning is promoted back to the public University.

The store is created on the first write and is never committed to the public repository.
