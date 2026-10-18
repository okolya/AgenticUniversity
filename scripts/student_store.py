#!/usr/bin/env python3
"""SQLite implementation of the Student state contract (ADR 0012).

Standard library only. The store is one SQLite file in a plain data directory:
`AGENTIC_UNIVERSITY_STATE_DIR`, otherwise the core-relative `students/`. Student
working files (homeworks) live in a sibling `homeworks/<id>/` directory
(`AGENTIC_UNIVERSITY_HOMEWORKS_DIR` overrides it). Each
Student keeps one document (the `STUDENT.md` shape of the CLI store mapping)
plus an append-only revision history. Reads never create the store; missing
state is reported as missing, never invented.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sqlite3
import sys
from contextlib import closing
from datetime import datetime, timezone
from pathlib import Path

STATE_DIR_ENV = "AGENTIC_UNIVERSITY_STATE_DIR"
HOMEWORKS_DIR_ENV = "AGENTIC_UNIVERSITY_HOMEWORKS_DIR"
DB_NAME = "university.sqlite3"
EVIDENCE_KINDS = ("assessment", "finding", "gap", "retention", "competency_verification", "module_verdict")
EVIDENCE_WRITERS = {"learning-analyst", "examiner"}
EVIDENCE_HEADING = re.compile(r"^## Independent evidence[ \t]*$", re.MULTILINE)
NEXT_HEADING = re.compile(r"^## ", re.MULTILINE)
STUDENT_ID = re.compile(r"^[a-z0-9][a-z0-9_-]*$")
DOCUMENT_ID = re.compile(r"^id:\s*(\S+)\s*$", re.MULTILINE)
DOCUMENT_STATUS = re.compile(r"^status:\s*(\S+)\s*$", re.MULTILINE)
REGISTRY_ENTRY = re.compile(
    r"^\s*[-*]\s+(?P<label>[^—–\n`]+?)\s+[—–-]\s+`(?P<path>students/[^`]+)`\s*$"
)

SCHEMA = """
CREATE TABLE IF NOT EXISTS students (
    student_id TEXT PRIMARY KEY,
    label TEXT NOT NULL,
    status TEXT NOT NULL,
    created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS student_documents (
    student_id TEXT PRIMARY KEY REFERENCES students(student_id),
    content TEXT NOT NULL,
    revision INTEGER NOT NULL,
    updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS student_document_revisions (
    student_id TEXT NOT NULL REFERENCES students(student_id),
    revision INTEGER NOT NULL,
    content TEXT NOT NULL,
    sha256 TEXT NOT NULL,
    actor TEXT NOT NULL,
    recorded_at TEXT NOT NULL,
    PRIMARY KEY(student_id, revision)
);
"""


class StoreError(RuntimeError):
    """A fail-closed store error."""


class MissingStateError(StoreError):
    """The store or the selected Student does not exist."""


class UnavailableStateError(StoreError):
    """The state cannot be read or written safely."""


def core_root() -> Path:
    return Path(__file__).resolve().parent.parent


def default_state_dir() -> Path:
    override = os.environ.get(STATE_DIR_ENV)
    return Path(override).expanduser() if override else core_root() / "students"


def normalize_student_id(student_id: str) -> str:
    student_id = student_id.strip().lower()
    if not STUDENT_ID.fullmatch(student_id):
        raise UnavailableStateError(f"invalid Student ID: {student_id}")
    return student_id


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _sha(content: str) -> str:
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def document_fields(content: str, student_id: str) -> str:
    """Return the document status after checking that it describes `student_id`."""
    identity = DOCUMENT_ID.search(content)
    status = DOCUMENT_STATUS.search(content)
    if identity is None or identity.group(1).lower() != student_id:
        raise UnavailableStateError("Student document id does not match the requested Student")
    if status is None:
        raise UnavailableStateError("Student document has no status")
    return status.group(1)


class StudentStore:
    def __init__(self, state_dir: Path | str | None = None) -> None:
        self.state_dir = Path(state_dir) if state_dir is not None else default_state_dir()
        self.path = self.state_dir / DB_NAME
        override = os.environ.get(HOMEWORKS_DIR_ENV)
        # Student working files sit beside the state directory, never inside it.
        self.homeworks_root = Path(override).expanduser() if override else self.state_dir.parent / "homeworks"

    def exists(self) -> bool:
        return self.path.is_file()

    def _read_connection(self) -> sqlite3.Connection:
        if not self.exists():
            raise MissingStateError(f"Student state store is missing: {self.path}")
        try:
            return sqlite3.connect(f"file:{self.path}?mode=ro", uri=True)
        except sqlite3.Error as exc:
            raise UnavailableStateError(f"Student state store cannot be opened: {exc}") from exc

    def _write_connection(self) -> sqlite3.Connection:
        self.state_dir.mkdir(parents=True, exist_ok=True)
        try:
            connection = sqlite3.connect(self.path)
            # Rollback journal, not WAL: a read-only mount or a second container can open the file without -wal/-shm.
            connection.execute("PRAGMA journal_mode=DELETE")
            connection.execute("PRAGMA foreign_keys=ON")
            connection.executescript(SCHEMA)
        except sqlite3.Error as exc:
            raise UnavailableStateError(f"Student state store cannot be written: {exc}") from exc
        return connection

    def registered(self) -> list[tuple[str, str]]:
        """Registry: `(student_id, label)` of every registered Student."""
        with closing(self._read_connection()) as connection:
            return connection.execute(
                "SELECT student_id, label FROM students ORDER BY student_id"
            ).fetchall()

    def resolve(self, claim: str) -> list[tuple[str, str]]:
        """Registry entries whose id or label equals `claim` (case-insensitive); no other Student is returned."""
        claim = claim.strip().lower()
        return [(i, l) for i, l in self.registered() if i == claim or l.strip().lower() == claim]

    def read_document(self, student_id: str) -> str:
        student_id = normalize_student_id(student_id)
        with closing(self._read_connection()) as connection:
            if connection.execute(
                "SELECT 1 FROM students WHERE student_id = ?", (student_id,)
            ).fetchone() is None:
                raise MissingStateError(f"Student ID is not registered: {student_id}")
            row = connection.execute(
                "SELECT content FROM student_documents WHERE student_id = ?", (student_id,)
            ).fetchone()
        if row is None:
            raise MissingStateError(f"Student state is missing: {student_id}")
        return row[0]

    def write_document(
        self, student_id: str, content: str, *, actor: str, label: str | None = None
    ) -> int:
        """Register the Student if new, store a new document revision, read it back.

        The Student's working-file directory is created together with the registration."""
        student_id = normalize_student_id(student_id)
        if not actor.strip():
            raise UnavailableStateError("a write needs the acting Profession and Workflow")
        status = document_fields(content, student_id)
        now = _now()
        with closing(self._write_connection()) as connection:
            with connection:
                known = connection.execute(
                    "SELECT 1 FROM students WHERE student_id = ?", (student_id,)
                ).fetchone()
                if known is None:
                    connection.execute(
                        "INSERT INTO students(student_id, label, status, created_at) VALUES (?, ?, ?, ?)",
                        (student_id, label or student_id, status, now),
                    )
                else:
                    connection.execute(
                        "UPDATE students SET status = ?, label = COALESCE(?, label) WHERE student_id = ?",
                        (status, label, student_id),
                    )
                last = connection.execute(
                    "SELECT COALESCE(MAX(revision), 0) FROM student_document_revisions WHERE student_id = ?",
                    (student_id,),
                ).fetchone()[0]
                revision = last + 1
                connection.execute(
                    "INSERT INTO student_document_revisions(student_id, revision, content, sha256, actor, recorded_at)"
                    " VALUES (?, ?, ?, ?, ?, ?)",
                    (student_id, revision, content, _sha(content), actor, now),
                )
                connection.execute(
                    "INSERT INTO student_documents(student_id, content, revision, updated_at) VALUES (?, ?, ?, ?)"
                    " ON CONFLICT(student_id) DO UPDATE SET content = excluded.content,"
                    " revision = excluded.revision, updated_at = excluded.updated_at",
                    (student_id, content, revision, now),
                )
        if self.read_document(student_id) != content:
            raise UnavailableStateError(f"read-back after write differs: {student_id}")
        self.homeworks_dir(student_id)
        return revision

    def revisions(self, student_id: str) -> list[tuple[int, str, str, str]]:
        """History: `(revision, sha256, actor, recorded_at)` oldest first."""
        student_id = normalize_student_id(student_id)
        with closing(self._read_connection()) as connection:
            return connection.execute(
                "SELECT revision, sha256, actor, recorded_at FROM student_document_revisions"
                " WHERE student_id = ? ORDER BY revision",
                (student_id,),
            ).fetchall()

    def append_evidence(
        self, student_id: str, entry: dict, *, profession: str, workflow: str, recorded_on: str | None = None
    ) -> str:
        """`append-evidence` of the contract: add one entry to `## Independent evidence`, never rewrite earlier text.

        Only a Learning Analyst or an Examiner writes (a Module verdict: Examiner only). A correction names the
        earlier entry in `corrects`. Returns the new entry id; the new document revision is read back.
        """
        student_id = normalize_student_id(student_id)
        profession = profession.strip().lower().replace(" ", "-")
        if profession not in EVIDENCE_WRITERS:
            raise UnavailableStateError(f"{profession or 'this role'} may not append Evidence")
        if not workflow.strip():
            raise UnavailableStateError("an Evidence entry needs the active workflow")
        kind = entry.get("kind")
        if kind not in EVIDENCE_KINDS:
            raise UnavailableStateError(f"Evidence kind must be one of {', '.join(EVIDENCE_KINDS)}")
        if kind == "module_verdict" and profession != "examiner":
            raise UnavailableStateError("only the Examiner records a Module verdict")
        if not str(entry.get("evidence_status", "")).strip():
            raise UnavailableStateError("an Evidence entry needs evidence_status")
        artifact = entry.get("artifact_ref")
        if artifact is not None:
            ref = str(artifact)
            if not ref or ref.startswith(("/", "~")) or ".." in Path(ref).parts or "\\" in ref:
                raise UnavailableStateError("artifact_ref must be a relative reference, never a local path")
        old = self.read_document(student_id)
        existing = re.findall(r"^\s*- id: (\S+)\s*$", old, re.MULTILINE)
        corrects = entry.get("corrects")
        if corrects is not None and corrects not in existing:
            raise UnavailableStateError(f"corrects names an unknown Evidence entry: {corrects}")
        date = recorded_on or datetime.now(timezone.utc).date().isoformat()
        evidence_id = f"ev-{date}-{len(existing) + 1}"
        lines = [f"- {date} — {kind}", f"  - id: {evidence_id}"]
        for label, key in (("artifact", "artifact_ref"), ("observed", "observed"), ("demonstrated", "demonstrated"),
                           ("evidence status", "evidence_status"), ("limitation", "limitation"),
                           ("handoff", "handoff"), ("corrects", "corrects")):
            if entry.get(key):
                value = f"`{entry[key]}`" if key in ("artifact_ref", "corrects") else str(entry[key]).strip()
                lines.append(f"  - {label}: {value}")
        if entry.get("criteria_refs"):
            lines.append("  - criteria: " + ", ".join(f"`{c}`" for c in entry["criteria_refs"]))
        lines.append(f"  - recorded: {profession} / {workflow.strip()} / {date}")
        block = "\n".join(lines) + "\n"
        heading = EVIDENCE_HEADING.search(old)
        if heading is None:
            new = old.rstrip("\n") + "\n\n## Independent evidence\n\n" + block
        else:
            following = NEXT_HEADING.search(old, heading.end())
            end = following.start() if following else len(old)
            body = old[:end].rstrip("\n") + "\n\n" + block
            new = body + ("\n" + old[end:] if following else "")
        self.write_document(student_id, new, actor=f"{profession}/{workflow.strip()}")
        if block not in self.read_document(student_id):
            raise UnavailableStateError("Evidence entry is missing after the write")
        return evidence_id

    def homeworks_dir(self, student_id: str) -> Path:
        """Working-file directory of a registered Student (created on demand)."""
        student_id = normalize_student_id(student_id)
        self.read_document(student_id)
        path = self.homeworks_root / student_id
        path.mkdir(parents=True, exist_ok=True)
        return path


def import_markdown(store: StudentStore, markdown_root: Path, *, actor: str) -> list[str]:
    """Import every Student in `markdown_root/registry/REGISTRY.md` (the retired Markdown store)."""
    registry = markdown_root / "registry" / "REGISTRY.md"
    if not registry.is_file():
        raise MissingStateError(f"registry is missing: {registry}")
    imported: list[str] = []
    for line in registry.read_text(encoding="utf-8").splitlines():
        match = REGISTRY_ENTRY.match(line)
        if not match:
            continue
        student_id = Path(match.group("path")).parent.name
        document = markdown_root / student_id / "STUDENT.md"
        if not document.is_file():
            raise MissingStateError(f"Student state is missing: {document}")
        store.write_document(
            student_id,
            document.read_text(encoding="utf-8"),
            actor=actor,
            label=match.group("label").strip(),
        )
        imported.append(student_id)
    return imported


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state-dir", type=Path, default=None)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("list", help="print the registry (ids and labels only) for a CLI host without login")
    resolve = commands.add_parser("resolve", help="print the one registry entry matching a claimed id or name")
    resolve.add_argument("claim")
    history = commands.add_parser("history", help="print the revision history of one Student as JSON")
    history.add_argument("student_id")
    evidence = commands.add_parser("append-evidence", help="append one Evidence entry (JSON on stdin) as an authorized role")
    evidence.add_argument("student_id")
    evidence.add_argument("--profession", required=True)
    evidence.add_argument("--workflow", required=True)
    homeworks = commands.add_parser("homeworks", help="create and print the working-file directory of a registered Student")
    homeworks.add_argument("student_id")
    importer = commands.add_parser("import-markdown", help="one-time import of the retired Markdown store")
    importer.add_argument("markdown_root", type=Path)
    importer.add_argument("--actor", default="owner/import-markdown")
    args = parser.parse_args(argv)
    store = StudentStore(args.state_dir)
    try:
        if args.command == "list":
            print(json.dumps([{"id": i, "label": l} for i, l in store.registered()], ensure_ascii=False, indent=2))
        elif args.command == "resolve":
            matches = store.resolve(args.claim)
            if not matches:
                raise MissingStateError(f"Student is not registered: {args.claim}")
            if len(matches) > 1:
                raise UnavailableStateError(f"claim matches several registry entries: {args.claim}")
            print(json.dumps({"id": matches[0][0], "label": matches[0][1]}, ensure_ascii=False))
        elif args.command == "history":
            print(json.dumps(
                [dict(zip(("revision", "sha256", "actor", "recorded_at"), row)) for row in store.revisions(args.student_id)],
                ensure_ascii=False, indent=2,
            ))
        elif args.command == "append-evidence":
            print(store.append_evidence(
                args.student_id, json.loads(sys.stdin.read()), profession=args.profession, workflow=args.workflow
            ))
        elif args.command == "homeworks":
            print(store.homeworks_dir(args.student_id))
        else:
            for student_id in import_markdown(store, args.markdown_root.resolve(), actor=args.actor):
                print(f"✓ imported {student_id} (revision {store.revisions(student_id)[-1][0]})")
    except MissingStateError as exc:
        print(json.dumps({"status": "missing", "error": str(exc)}, ensure_ascii=False))
        return 1
    except (StoreError, OSError) as exc:
        print(json.dumps({"status": "unavailable", "error": str(exc)}, ensure_ascii=False))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
