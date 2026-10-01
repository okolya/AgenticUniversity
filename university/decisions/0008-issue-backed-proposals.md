# ADR 0008: Issue-backed correction proposals

- Status: accepted
- Date: 2026-10-01

## Decision

The future shared correction queue is the University repository's issue
metadata. An issue is created only after the Assistant, Lecturer, and
required Dean decisions finish. Duplicates and rejected proposals create no
new issue. Accepted and deferred proposals use stable academic scope labels
and the outcomes `ready-to-apply`, `deferred`, or `blocked`.

Issue, pull-request, and commit content contains Profession resolutions and
source/version references, but no Student names, identifiers, private
dialogue, or named Worker identities.

## Consequences

Hosts may later implement issue/Git execution without inventing a second queue
database or Student proposal entity. The core contract does not create live
issues, credentials, branches, pull requests, or merges.
