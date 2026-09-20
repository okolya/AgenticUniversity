# Worker Appointment Workflow

Use this workflow whenever an authorized Rector or Dean creates a concrete Worker from an existing Profession.

1. Identify the staffing need and owning scope/faculty.
2. Select an existing Profession; do not create a specialized Profession merely for a Faculty.
3. Read the Faculty/scope specification to determine domain context.
4. Choose the concrete Worker identity and appointment.
5. Determine only genuine Worker additions: specialization, extra responsibilities, extra skills, extra policies.
6. Use `appoint-worker`.
7. `appoint-worker` creates the thin `WORKER.md` and invokes `register-worker`.
8. Verify University and Faculty staff registries.
9. The Worker becomes usable through the existing Profession runtime agent and `worker-activation` protocol.

Example:

`Dean Profession + Engineering Faculty + Luke appointment + additions -> Luke`

Luke still uses the Dean Profession agent. Engineering specialization comes primarily from Faculty/scope context; Luke contains only appointment-specific additions.
