# ADR 0006: Manifest classes and version 2

- Status: accepted
- Date: 2026-10-01

## Context

Hosts need to distinguish Student learning entry points, staffing operations,
University development, and bounded technical capabilities. A scalar workflow
list and the former `maintenance` class cannot express those boundaries or
validate transitive calls.

## Decision

The public manifest uses `manifest_version: 2`. Every Skill and workflow has
one class: `learning`, `administrative`, `development`, or `technical`.
`maintenance` is retired and its University-development uses are classified as
`development`.

Workflows declare calls in a machine-readable `dependencies` block. Each call
names a target and target kind (`skill` or `workflow`). Hosts may expose only
the classes permitted by the active profile. A learning chain may reach a
bounded technical capability only when the active Worker and target contract
authorize it; it may not reach administrative or development operations.

The manifest remains a constrained YAML-like document parsed by the standard
library. Inline maps are used for manifest entries, and dependency declarations
use a stable list of inline maps:

```yaml
dependencies:
  - {kind: skill, name: example-skill}
```

The declarations are authoritative for static reachability checks. They do not
replace runtime authorization, Profession ownership, Worker activation, or
host enforcement.

## Consequences

Hosts can build a deterministic capability graph and reject forbidden
transitive paths before execution. Existing readers must understand manifest
v2 and workflow maps. Runtime isolation and Git/provider enforcement remain
host responsibilities and require separate acceptance tests.

## Scope boundary

This ADR defines the public contract only. It does not create a bot, issue
queue, GitHub integration, MCP transport, credentials, or automatic merge
execution.
