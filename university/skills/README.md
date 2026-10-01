# Skills

Skills are reusable bounded operations. A Skill never owns an academic decision, learning trajectory, Profession, Worker, or workflow.

Rules:
- Profession defines baseline responsibility and baseline Skills.
- Worker may add only authorized additive or scope-narrowing Skills.
- Workflow defines when and why a Skill is used.
- Policy constrains every invocation.
- Skills return results to the active Worker; they do not inherit the Worker's authority.
- Student-facing questions follow `university/policies/interaction-format.md`:
  bounded decisions use explicit choices, while evidence requests use an
  explicit structured response frame.
- Technical/internal Skills such as `register-worker` may support another Skill without becoming a Profession capability.
- Do not create a new Skill when an existing Skill already expresses the same bounded operation in another context.

Skill classes (recorded per Skill in `MANIFEST.md`):
- `learning` — used by Workers in Student sessions, including Student-state
  operations bounded by `protocols/student-state-contract.md`;
- `administrative` — staffing operations (`appoint-worker`, `register-worker`);
  never offered in a Student session;
- `maintenance` — University workspace bootstrap tooling (`session-bootstrap`);
  CLI/maintainer only. Development planning Skills live in the private
  documentation repository.
A host exposes only `learning` Skills in Student sessions. Classify every new
Skill and update `MANIFEST.md` (`make check-manifest`).

Current separation examples:
- `run-diagnostic` measures a bounded uncertainty; it does not decide placement.
- `check-prerequisites` compares criteria with existing evidence; it does not certify competence.
- `build-assessment` constructs an assessment; `run-quiz` conducts a bounded quiz; `evaluate-*` evaluates responses/results.
- `module-planning` builds the Student-specific Module coverage plan; it does not design the public Module contract.
- `author-material` creates material; `research-materials` curates external material.
- `localize-material` localizes learner-facing material into the selected
  dialogue language; it does not own the material or replace pedagogical review.
- `session-bootstrap` routes a session to the owning repository boundary and
  Profession; it does not choose placement or read private Student state.
- `update-evidence` persists only evidence/results already authorized by the active assessment workflow.
