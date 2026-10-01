---
name: university-start
class: learning
---
# University start

Purpose: start a personal University without inventing academic content.

Entry gate: this workflow applies only when `session-bootstrap` has successfully
inspected the selected Student state and confirmed that it is available and
contains no active enrollment, plan, current Lesson, or explicit academic
handoff. Missing or unavailable Student state blocks startup; it must not be
treated as an empty state. If an active workflow exists, resume that workflow
instead; do not present University orientation or Faculty selection.

1. The private Student state is created (`initialize-student` in
   `protocols/student-state-contract.md`). In the CLI host a human creates the
   private Student repository from the public Student template/instructions; in
   another host the Student's own sign-up request creates the Student record.
2. Rector is activated through the Rector Profession agent; the routing layer
   resolves and attaches the active Rector Worker context.
3. Rector verifies only the minimum Student state needed to begin.
4. Rector presents a focused, numbered choice of verified learning routes. If
   an unlisted goal must be accepted, expose it as an explicit `Other / not
   listed` option with a short structured description request.
5. Rector presents existing Faculties; Rector does not invent a Faculty merely to satisfy a request.
6. Student chooses a Faculty.
7. Rector hands the Student to that Faculty's appointed Dean.
8. Faculty Entry workflow begins.

The Rector owns University entry. The Dean owns Faculty entry.
