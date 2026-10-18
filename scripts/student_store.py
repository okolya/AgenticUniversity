#!/usr/bin/env python3
"""SQLite implementation of the Student state contract (ADR 0012, ADR 0013).

Standard library only. The store is one SQLite file in a plain data directory:
`AGENTIC_UNIVERSITY_STATE_DIR`, otherwise the core-relative `students/`. Student
working files (homeworks) live in a sibling `homeworks/<id>/` directory
(`AGENTIC_UNIVERSITY_HOMEWORKS_DIR` overrides it). Each
Student keeps one document (the `STUDENT.md` shape of the CLI store mapping)
plus an append-only revision history, and optional formative `lexicon_items`
(ADR 0013). Reads never create the store; missing state is reported as missing,
never invented.
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
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

STATE_DIR_ENV = "AGENTIC_UNIVERSITY_STATE_DIR"
HOMEWORKS_DIR_ENV = "AGENTIC_UNIVERSITY_HOMEWORKS_DIR"
DB_NAME = "university.sqlite3"
EVIDENCE_KINDS = ("assessment", "finding", "gap", "retention", "competency_verification", "module_verdict")
EVIDENCE_WRITERS = {"learning-analyst", "examiner"}
LEXICON_WRITERS = {"lecturer", "teacher"}
LEXICON_STATUSES = ("new", "recycling", "weak", "stable")
LEXICON_ARTICLES = ("der", "die", "das", "none")
LEXICON_CHECKS = ("ok", "fail")
LESSON_REF = re.compile(
    r"^[a-z0-9][a-z0-9-]*/[a-z0-9][a-z0-9-]*/[a-z0-9][a-z0-9-]*/[a-z0-9][a-z0-9-]*$"
)
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
CREATE TABLE IF NOT EXISTS lexicon_items (
    student_id TEXT NOT NULL REFERENCES students(student_id),
    course_id TEXT NOT NULL,
    lemma TEXT NOT NULL,
    article TEXT NOT NULL,
    collocation TEXT,
    status TEXT NOT NULL,
    introduced_lesson_ref TEXT NOT NULL,
    last_check TEXT,
    next_due TEXT,
    streak_ok INTEGER NOT NULL DEFAULT 0,
    mnemonic TEXT,
    image_ref TEXT,
    audio_ref TEXT,
    profession TEXT NOT NULL,
    workflow TEXT NOT NULL,
    recorded_on TEXT NOT NULL,
    PRIMARY KEY(student_id, course_id, lemma)
);
"""

LEXICON_COLUMNS = (
    "lemma",
    "article",
    "collocation",
    "status",
    "introduced_lesson_ref",
    "last_check",
    "next_due",
    "streak_ok",
    "mnemonic",
    "course_id",
    "image_ref",
    "audio_ref",
    "profession",
    "workflow",
    "recorded_on",
)


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


def _today() -> date:
    return datetime.now(timezone.utc).date()


def _normalize_profession(profession: str) -> str:
    return profession.strip().lower().replace(" ", "-")


def _lexicon_row(row: sqlite3.Row) -> dict:
    item = {key: row[key] for key in LEXICON_COLUMNS}
    item["recorded"] = {
        "profession": item.pop("profession"),
        "workflow": item.pop("workflow"),
        "date": item.pop("recorded_on"),
    }
    return item


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
            connection = sqlite3.connect(f"file:{self.path}?mode=ro", uri=True)
            connection.row_factory = sqlite3.Row
            return connection
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
            connection.row_factory = sqlite3.Row
        except sqlite3.Error as exc:
            raise UnavailableStateError(f"Student state store cannot be written: {exc}") from exc
        return connection

    def _require_registered(self, connection: sqlite3.Connection, student_id: str) -> None:
        if connection.execute(
            "SELECT 1 FROM students WHERE student_id = ?", (student_id,)
        ).fetchone() is None:
            raise MissingStateError(f"Student ID is not registered: {student_id}")

    def _lexicon_table_ready(self, connection: sqlite3.Connection) -> bool:
        return (
            connection.execute(
                "SELECT 1 FROM sqlite_master WHERE type = 'table' AND name = 'lexicon_items'"
            ).fetchone()
            is not None
        )

    def registered(self) -> list[tuple[str, str]]:
        """Registry: `(student_id, label)` of every registered Student."""
        with closing(self._read_connection()) as connection:
            return [
                (row[0], row[1])
                for row in connection.execute(
                    "SELECT student_id, label FROM students ORDER BY student_id"
                ).fetchall()
            ]

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
            return [
                (row[0], row[1], row[2], row[3])
                for row in connection.execute(
                    "SELECT revision, sha256, actor, recorded_at FROM student_document_revisions"
                    " WHERE student_id = ? ORDER BY revision",
                    (student_id,),
                ).fetchall()
            ]

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

    def upsert_lexicon(
        self,
        student_id: str,
        item: dict,
        *,
        profession: str,
        workflow: str,
        recorded_on: str | None = None,
    ) -> dict:
        """Create or update one formative lexicon item (ADR 0013)."""
        student_id = normalize_student_id(student_id)
        profession = _normalize_profession(profession)
        if profession not in LEXICON_WRITERS:
            raise UnavailableStateError(f"{profession or 'this role'} may not write lexicon items")
        if not workflow.strip():
            raise UnavailableStateError("a lexicon write needs the active workflow")
        lemma = str(item.get("lemma", "")).strip()
        course_id = str(item.get("course_id", "")).strip()
        article = str(item.get("article", "")).strip()
        status = str(item.get("status", "new")).strip()
        introduced = str(item.get("introduced_lesson_ref", "")).strip()
        if not lemma or not course_id:
            raise UnavailableStateError("lexicon item needs lemma and course_id")
        if article not in LEXICON_ARTICLES:
            raise UnavailableStateError(f"article must be one of {', '.join(LEXICON_ARTICLES)}")
        if status not in LEXICON_STATUSES:
            raise UnavailableStateError(f"status must be one of {', '.join(LEXICON_STATUSES)}")
        if not LESSON_REF.fullmatch(introduced):
            raise UnavailableStateError("introduced_lesson_ref must be course/module/theme/lesson")
        try:
            streak_ok = int(item.get("streak_ok", 0))
        except (TypeError, ValueError) as exc:
            raise UnavailableStateError("streak_ok must be an integer") from exc
        if streak_ok < 0:
            raise UnavailableStateError("streak_ok must be >= 0")
        day = recorded_on or _today().isoformat()
        next_due = item.get("next_due")
        if next_due is None or str(next_due).strip() == "":
            next_due = day
        collocation = item.get("collocation")
        mnemonic = item.get("mnemonic")
        image_ref = item.get("image_ref")
        audio_ref = item.get("audio_ref")
        last_check = item.get("last_check")
        with closing(self._write_connection()) as connection:
            with connection:
                self._require_registered(connection, student_id)
                connection.execute(
                    """
                    INSERT INTO lexicon_items(
                        student_id, course_id, lemma, article, collocation, status,
                        introduced_lesson_ref, last_check, next_due, streak_ok, mnemonic,
                        image_ref, audio_ref, profession, workflow, recorded_on
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ON CONFLICT(student_id, course_id, lemma) DO UPDATE SET
                        article = excluded.article,
                        collocation = excluded.collocation,
                        status = excluded.status,
                        introduced_lesson_ref = excluded.introduced_lesson_ref,
                        last_check = COALESCE(excluded.last_check, lexicon_items.last_check),
                        next_due = excluded.next_due,
                        streak_ok = excluded.streak_ok,
                        mnemonic = excluded.mnemonic,
                        image_ref = excluded.image_ref,
                        audio_ref = excluded.audio_ref,
                        profession = excluded.profession,
                        workflow = excluded.workflow,
                        recorded_on = excluded.recorded_on
                    """,
                    (
                        student_id,
                        course_id,
                        lemma,
                        article,
                        None if collocation in (None, "") else str(collocation),
                        status,
                        introduced,
                        None if last_check in (None, "") else str(last_check),
                        str(next_due),
                        streak_ok,
                        None if mnemonic in (None, "") else str(mnemonic),
                        None if image_ref in (None, "") else str(image_ref),
                        None if audio_ref in (None, "") else str(audio_ref),
                        profession,
                        workflow.strip(),
                        day,
                    ),
                )
                row = connection.execute(
                    "SELECT * FROM lexicon_items WHERE student_id = ? AND course_id = ? AND lemma = ?",
                    (student_id, course_id, lemma),
                ).fetchone()
        return _lexicon_row(row)

    def list_lexicon(self, student_id: str, *, course_id: str | None = None) -> list[dict]:
        """Return lexicon items for one registered Student."""
        student_id = normalize_student_id(student_id)
        with closing(self._read_connection()) as connection:
            self._require_registered(connection, student_id)
            if not self._lexicon_table_ready(connection):
                return []
            if course_id:
                rows = connection.execute(
                    "SELECT * FROM lexicon_items WHERE student_id = ? AND course_id = ?"
                    " ORDER BY lemma",
                    (student_id, course_id.strip()),
                ).fetchall()
            else:
                rows = connection.execute(
                    "SELECT * FROM lexicon_items WHERE student_id = ? ORDER BY course_id, lemma",
                    (student_id,),
                ).fetchall()
        return [_lexicon_row(row) for row in rows]

    def list_lexicon_due(
        self, student_id: str, *, course_id: str | None = None, on: date | None = None
    ) -> list[dict]:
        """Return lexicon items due on or before `on` (UTC today by default)."""
        student_id = normalize_student_id(student_id)
        due_on = (on or _today()).isoformat()
        with closing(self._read_connection()) as connection:
            self._require_registered(connection, student_id)
            if not self._lexicon_table_ready(connection):
                return []
            if course_id:
                rows = connection.execute(
                    "SELECT * FROM lexicon_items WHERE student_id = ? AND course_id = ?"
                    " AND next_due IS NOT NULL AND next_due <= ?"
                    " ORDER BY next_due, lemma",
                    (student_id, course_id.strip(), due_on),
                ).fetchall()
            else:
                rows = connection.execute(
                    "SELECT * FROM lexicon_items WHERE student_id = ?"
                    " AND next_due IS NOT NULL AND next_due <= ?"
                    " ORDER BY next_due, course_id, lemma",
                    (student_id, due_on),
                ).fetchall()
        return [_lexicon_row(row) for row in rows]

    def record_lexicon_check(
        self,
        student_id: str,
        *,
        lemma: str,
        course_id: str,
        result: str,
        profession: str,
        workflow: str,
        recorded_on: str | None = None,
    ) -> dict:
        """Apply spacing v1 for one Spiel/Recycle/gym check (ADR 0013)."""
        student_id = normalize_student_id(student_id)
        profession = _normalize_profession(profession)
        if profession not in LEXICON_WRITERS:
            raise UnavailableStateError(f"{profession or 'this role'} may not record lexicon checks")
        if not workflow.strip():
            raise UnavailableStateError("a lexicon check needs the active workflow")
        lemma = lemma.strip()
        course_id = course_id.strip()
        result = result.strip().lower()
        if result not in LEXICON_CHECKS:
            raise UnavailableStateError("lexicon check result must be ok or fail")
        if not lemma or not course_id:
            raise UnavailableStateError("lexicon check needs lemma and course_id")
        day = date.fromisoformat(recorded_on) if recorded_on else _today()
        day_s = day.isoformat()
        with closing(self._write_connection()) as connection:
            with connection:
                self._require_registered(connection, student_id)
                row = connection.execute(
                    "SELECT * FROM lexicon_items WHERE student_id = ? AND course_id = ? AND lemma = ?",
                    (student_id, course_id, lemma),
                ).fetchone()
                if row is None:
                    raise MissingStateError(
                        f"lexicon item is missing: {student_id}/{course_id}/{lemma}"
                    )
                status = row["status"]
                streak = int(row["streak_ok"] or 0)
                if result == "fail":
                    status = "weak"
                    streak = 0
                    next_due = day_s
                elif status == "new":
                    status = "recycling"
                    streak = 1
                    next_due = (day + timedelta(days=1)).isoformat()
                elif status in ("recycling", "weak"):
                    streak = streak + 1 if status == "recycling" else 1
                    if streak >= 2:
                        status = "stable"
                        next_due = (day + timedelta(days=3)).isoformat()
                    else:
                        status = "recycling"
                        next_due = (day + timedelta(days=1)).isoformat()
                else:  # stable
                    status = "stable"
                    streak = max(streak, 2)
                    next_due = (day + timedelta(days=3)).isoformat()
                connection.execute(
                    """
                    UPDATE lexicon_items SET
                        status = ?, streak_ok = ?, last_check = ?, next_due = ?,
                        profession = ?, workflow = ?, recorded_on = ?
                    WHERE student_id = ? AND course_id = ? AND lemma = ?
                    """,
                    (
                        status,
                        streak,
                        day_s,
                        next_due,
                        profession,
                        workflow.strip(),
                        day_s,
                        student_id,
                        course_id,
                        lemma,
                    ),
                )
                updated = connection.execute(
                    "SELECT * FROM lexicon_items WHERE student_id = ? AND course_id = ? AND lemma = ?",
                    (student_id, course_id, lemma),
                ).fetchone()
        return _lexicon_row(updated)


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
    upsert_lex = commands.add_parser("upsert-lexicon", help="create or update one formative lexicon item (JSON on stdin)")
    upsert_lex.add_argument("student_id")
    upsert_lex.add_argument("--profession", required=True)
    upsert_lex.add_argument("--workflow", required=True)
    list_lex = commands.add_parser("list-lexicon", help="list formative lexicon items for one Student")
    list_lex.add_argument("student_id")
    list_lex.add_argument("--course", dest="course_id", default=None)
    due_lex = commands.add_parser("list-lexicon-due", help="list lexicon items due on or before today")
    due_lex.add_argument("student_id")
    due_lex.add_argument("--course", dest="course_id", default=None)
    check_lex = commands.add_parser("record-lexicon-check", help="record ok|fail for one lexicon lemma (spacing v1)")
    check_lex.add_argument("student_id")
    check_lex.add_argument("lemma")
    check_lex.add_argument("result", choices=LEXICON_CHECKS)
    check_lex.add_argument("--course", dest="course_id", required=True)
    check_lex.add_argument("--profession", required=True)
    check_lex.add_argument("--workflow", required=True)
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
        elif args.command == "upsert-lexicon":
            print(json.dumps(
                store.upsert_lexicon(
                    args.student_id,
                    json.loads(sys.stdin.read()),
                    profession=args.profession,
                    workflow=args.workflow,
                ),
                ensure_ascii=False,
                indent=2,
            ))
        elif args.command == "list-lexicon":
            print(json.dumps(
                store.list_lexicon(args.student_id, course_id=args.course_id),
                ensure_ascii=False,
                indent=2,
            ))
        elif args.command == "list-lexicon-due":
            print(json.dumps(
                store.list_lexicon_due(args.student_id, course_id=args.course_id),
                ensure_ascii=False,
                indent=2,
            ))
        elif args.command == "record-lexicon-check":
            print(json.dumps(
                store.record_lexicon_check(
                    args.student_id,
                    lemma=args.lemma,
                    course_id=args.course_id,
                    result=args.result,
                    profession=args.profession,
                    workflow=args.workflow,
                ),
                ensure_ascii=False,
                indent=2,
            ))
        else:
            for student_id in import_markdown(store, args.markdown_root.resolve(), actor=args.actor):
                print(f"✓ imported {student_id} (revision {store.revisions(student_id)[-1][0]})")
    except MissingStateError as exc:
        print(json.dumps({"status": "missing", "error": str(exc)}, ensure_ascii=False))
        return 1
    except (StoreError, OSError, json.JSONDecodeError, ValueError) as exc:
        print(json.dumps({"status": "unavailable", "error": str(exc)}, ensure_ascii=False))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
