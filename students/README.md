# Student state

Private Student state of this University instance. Everything here except this
file is ignored by Git and never published.

- `university.sqlite3` is the Student state store (ADR 0012), created on the
  first write; a short-lived `-journal` file appears next to it during a write.
- The store is managed through `scripts/student_store.py` and the host
  adapters; do not edit the database by hand.
- `AGENTIC_UNIVERSITY_STATE_DIR` points the core at another directory.

Back up this directory (and `../homeworks/`) as one unit; they are the only
copy of a Student's progress.
