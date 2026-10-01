# Controlled material-correction protocol

This protocol defines the public contract for a future host correction chain.
It does not create a live issue queue or grant a host GitHub permissions.

## Route

1. The Instructional Assistant searches existing issues before accepting a new
   proposal. A duplicate returns the existing link and a suggestion for a
   Student comment; it does not restart review.
2. The Assistant rejects only a proposal unrelated to every approved Course
   competency and unnecessary for the current Course Lessons. An uncertain case
   goes to the Lecturer.
3. The Assistant records the criticism, pedagogical findings, scope, source
   revision, affected material, measurements, and proposed correction.
4. The Lecturer decides subject correctness, scope, and learning impact.
5. The Dean resolves every escalated case, may narrow the proposal, and issues
   binding execution instructions.
6. Only after the decision chain does the Assistant create a future issue or
   invoke the bounded technical execution Skills.

## Impact route

Text impact is `abs(after - before) / before * 100`, covering both growth and
reduction. Learning impact includes replaced knowledge, code, formulas, tasks,
complexity, and proportion of knowledge changed. The larger value governs.

- Below 15%, within approved scope, and confidently assessed: Lecturer may
  authorize execution.
- Exactly 15%, at least 15%, at least 15% knowledge replacement, an
  out-of-Lesson change within the Course, or uncertainty: Lecturer resolution
  followed by mandatory Dean resolution.
- Zero baseline or unreliable assessment: uncertain, never automatically below
  threshold.

The Lecturer implements or checks compliance with a Dean resolution; no
approval ping-pong is created. A technical blocker is recorded.

## Future issue contract

The issue body contains the proposal, rationale, impact assessment, applicable
resolutions, source version, material target, and execution instructions.
Stable academic labels may include `faculty:<id>`, `course:<id>`,
`module:<id>`, `theme:<id>`, and `lesson:<id>`. Outcome labels are
`ready-to-apply`, `deferred`, and `blocked`.

Issue, PR, and commit content signs only by Profession:
`Instructional Assistant`, `Lecturer`, and `Dean`. It contains no Student
names/identifiers, private dialogue, or named Worker identities.

Rejected cases and duplicates create no new issue. Accepted or deferred cases
create an issue after resolutions. A successful future merge closes its linked
issue; a failed check or unavailable capability labels it `blocked`.

## Technical boundary

The future Assistant execution input must contain the approved resolution,
source reference, material targets, and authorized scope. Technical Skills may
search/read/create/label issues, patch approved MATERIALS, create branches and
PRs, run required checks, resolve technical conflicts, and merge only when the
authorization and repository protections permit it.

Policies, Skills, workflows, Course/Module framework, configuration, service
files, and other non-material files are forbidden targets. The correction
chain cannot approve itself, change the threshold, broaden scope, or bypass
host authorization.

This core contract does not implement GitHub, credentials, live issue creation,
PRs, merges, deferred scheduling, or a Worker bot.
