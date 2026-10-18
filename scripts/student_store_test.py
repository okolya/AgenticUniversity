#!/usr/bin/env python3
"""Self-tests for the SQLite Student state store."""

import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import student_store as store_module  # noqa: E402

DOC = "id: {id}\nstatus: registered\n\n## Active enrollments\n\n## Notes\n{note}\n"


class StudentStoreTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.state = Path(self.tempdir.name) / "students"
        self.store = store_module.StudentStore(self.state)

    def tearDown(self):
        self.tempdir.cleanup()

    def test_read_never_creates_the_store(self):
        with self.assertRaises(store_module.MissingStateError):
            self.store.read_document("mykola")
        self.assertFalse(self.state.exists())

    def test_write_registers_and_reads_back(self):
        revision = self.store.write_document(
            "Mykola", DOC.format(id="mykola", note=""), actor="Rector/student-initialization", label="Mykola"
        )
        self.assertEqual(revision, 1)
        self.assertEqual(self.store.registered(), [("mykola", "Mykola")])
        self.assertIn("id: mykola", self.store.read_document("MYKOLA"))

    def test_history_is_append_only(self):
        self.store.write_document("mykola", DOC.format(id="mykola", note="a"), actor="Dean/x")
        self.store.write_document("mykola", DOC.format(id="mykola", note="b"), actor="Dean/y")
        rows = self.store.revisions("mykola")
        self.assertEqual([row[0] for row in rows], [1, 2])
        self.assertNotEqual(rows[0][1], rows[1][1])
        self.assertTrue(self.store.read_document("mykola").endswith("b\n"))

    def test_unregistered_student_is_missing(self):
        self.store.write_document("mykola", DOC.format(id="mykola", note=""), actor="Dean/x")
        with self.assertRaises(store_module.MissingStateError):
            self.store.read_document("other")

    def test_document_must_describe_its_student(self):
        with self.assertRaises(store_module.UnavailableStateError):
            self.store.write_document("mykola", DOC.format(id="other", note=""), actor="Dean/x")

    def test_write_needs_an_actor(self):
        with self.assertRaises(store_module.UnavailableStateError):
            self.store.write_document("mykola", DOC.format(id="mykola", note=""), actor=" ")

    def test_invalid_student_id_is_rejected(self):
        with self.assertRaises(store_module.UnavailableStateError):
            self.store.read_document("../etc")

    def test_homeworks_dir_only_for_registered_student(self):
        with self.assertRaises(store_module.MissingStateError):
            self.store.homeworks_dir("mykola")
        self.store.write_document("mykola", DOC.format(id="mykola", note=""), actor="Dean/x")
        path = self.store.homeworks_dir("mykola")
        self.assertTrue(path.is_dir())
        self.assertEqual(path, self.state.parent / "homeworks" / "mykola")
        self.assertFalse((self.state / "mykola").exists())

    def test_resolve_returns_only_the_matching_entry(self):
        self.store.write_document("mykola", DOC.format(id="mykola", note=""), actor="Rector/x", label="Mykola")
        self.store.write_document("other", DOC.format(id="other", note=""), actor="Rector/x", label="Olena")
        self.assertEqual(self.store.resolve("MYKOLA"), [("mykola", "Mykola")])
        self.assertEqual(self.store.resolve("olena"), [("other", "Olena")])
        self.assertEqual(self.store.resolve("nobody"), [])

    def test_registered_lists_only_ids_and_labels(self):
        self.store.write_document("mykola", DOC.format(id="mykola", note="private"), actor="Rector/x", label="Mykola")
        self.assertEqual(self.store.registered(), [("mykola", "Mykola")])

    def test_registering_a_student_creates_the_working_directory(self):
        self.store.write_document("mykola", DOC.format(id="mykola", note=""), actor="Rector/x")
        self.assertTrue((self.state.parent / "homeworks" / "mykola").is_dir())

    def test_import_markdown_matches_the_source(self):
        source = Path(self.tempdir.name) / "markdown"
        (source / "registry").mkdir(parents=True)
        (source / "mykola").mkdir()
        (source / "registry" / "REGISTRY.md").write_text(
            "- Mykola — `students/mykola/STUDENT.md`\n", encoding="utf-8"
        )
        text = DOC.format(id="mykola", note="private")
        (source / "mykola" / "STUDENT.md").write_text(text, encoding="utf-8")
        imported = store_module.import_markdown(self.store, source, actor="owner/import")
        self.assertEqual(imported, ["mykola"])
        self.assertEqual(self.store.read_document("mykola"), text)
        self.assertEqual(self.store.registered(), [("mykola", "Mykola")])


class AppendEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.store = store_module.StudentStore(Path(self.tempdir.name) / "students")
        self.doc = "id: mykola\nstatus: registered\n\n## Independent evidence\n\n- 2026-09-21 — old entry\n\n## Notes\n\nkeep\n"
        self.store.write_document("mykola", self.doc, actor="Rector/x")
        self.entry = {"kind": "assessment", "evidence_status": "verified", "observed": "ran", "criteria_refs": ["c1"],
                      "artifact_ref": "homeworks/ai/x.py"}

    def tearDown(self):
        self.tempdir.cleanup()

    def append(self, entry=None, profession="Learning Analyst", workflow="theme-assessment"):
        return self.store.append_evidence("mykola", entry or self.entry, profession=profession, workflow=workflow,
                                          recorded_on="2026-10-18")

    def test_appends_inside_the_section_and_keeps_the_rest(self):
        evidence_id = self.append()
        text = self.store.read_document("mykola")
        self.assertEqual(evidence_id, "ev-2026-10-18-1")
        self.assertLess(text.index("old entry"), text.index(evidence_id))
        self.assertLess(text.index(evidence_id), text.index("## Notes"))
        self.assertIn("recorded: learning-analyst / theme-assessment / 2026-10-18", text)
        self.assertTrue(text.endswith("keep\n"))
        self.assertEqual([r[0] for r in self.store.revisions("mykola")], [1, 2])
        self.assertEqual(self.store.revisions("mykola")[-1][2], "learning-analyst/theme-assessment")

    def test_creates_the_section_when_missing(self):
        self.store.write_document("mykola", "id: mykola\nstatus: registered\n", actor="Rector/x")
        self.append()
        self.assertIn("## Independent evidence", self.store.read_document("mykola"))

    def test_only_assessing_roles_write(self):
        for role in ("Lecturer", "Dean", "Rector", ""):
            with self.assertRaises(store_module.UnavailableStateError):
                self.append(profession=role)

    def test_module_verdict_is_examiner_only(self):
        verdict = dict(self.entry, kind="module_verdict")
        with self.assertRaises(store_module.UnavailableStateError):
            self.append(verdict)
        self.assertTrue(self.append(verdict, profession="Examiner", workflow="module-exit"))

    def test_rejects_local_paths_and_bad_input(self):
        for ref in ("/home/me/x.py", "~/x.py", "../x.py"):
            with self.assertRaises(store_module.UnavailableStateError):
                self.append(dict(self.entry, artifact_ref=ref))
        with self.assertRaises(store_module.UnavailableStateError):
            self.append(dict(self.entry, kind="mastery"))
        with self.assertRaises(store_module.UnavailableStateError):
            self.append({"kind": "assessment"})
        with self.assertRaises(store_module.UnavailableStateError):
            self.append(workflow=" ")

    def test_a_correction_names_an_existing_entry(self):
        first = self.append()
        second = self.append(dict(self.entry, corrects=first))
        self.assertNotEqual(first, second)
        with self.assertRaises(store_module.UnavailableStateError):
            self.append(dict(self.entry, corrects="ev-nope"))
        self.assertIn(f"corrects: `{first}`", self.store.read_document("mykola"))


COURSE = "german-between-b1-and-b2"
LESSON = (
    "german-between-b1-and-b2/01-a2-recovery/"
    "theme-02-articles-cases-pronouns/lesson-01-articles-gender-accusative"
)


class LexiconTrackTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.store = store_module.StudentStore(Path(self.tempdir.name) / "students")
        self.store.write_document(
            "mykola", DOC.format(id="mykola", note=""), actor="Rector/x", label="Mykola"
        )
        self.base = {
            "lemma": "Artikel",
            "article": "der",
            "collocation": "der bestimmte Artikel",
            "status": "new",
            "introduced_lesson_ref": LESSON,
            "course_id": COURSE,
            "mnemonic": "der=blau",
            "streak_ok": 0,
        }

    def tearDown(self):
        self.tempdir.cleanup()

    def upsert(self, item=None, profession="Lecturer", workflow="lesson-preparation"):
        return self.store.upsert_lexicon(
            "mykola", item or self.base, profession=profession, workflow=workflow, recorded_on="2026-10-18"
        )

    def check(self, result, lemma="Artikel", profession="Lecturer", workflow="lesson-preparation", on="2026-10-18"):
        return self.store.record_lexicon_check(
            "mykola",
            lemma=lemma,
            course_id=COURSE,
            result=result,
            profession=profession,
            workflow=workflow,
            recorded_on=on,
        )

    def test_upsert_and_list(self):
        item = self.upsert()
        self.assertEqual(item["lemma"], "Artikel")
        self.assertEqual(item["article"], "der")
        self.assertEqual(item["status"], "new")
        self.assertEqual(item["recorded"]["profession"], "lecturer")
        listed = self.store.list_lexicon("mykola", course_id=COURSE)
        self.assertEqual(len(listed), 1)
        self.assertEqual(listed[0]["collocation"], "der bestimmte Artikel")

    def test_no_lexicon_without_registered_student(self):
        with self.assertRaises(store_module.MissingStateError):
            self.store.upsert_lexicon(
                "other", self.base, profession="Lecturer", workflow="lesson-preparation"
            )

    def test_only_lecturer_and_teacher_write(self):
        for role in ("Dean", "Learning Analyst", "Examiner", ""):
            with self.assertRaises(store_module.UnavailableStateError):
                self.upsert(profession=role)

    def test_fail_becomes_weak_and_is_due(self):
        self.upsert()
        item = self.check("fail")
        self.assertEqual(item["status"], "weak")
        self.assertEqual(item["streak_ok"], 0)
        self.assertEqual(item["next_due"], "2026-10-18")
        due = self.store.list_lexicon_due(
            "mykola", course_id=COURSE, on=date.fromisoformat("2026-10-18")
        )
        self.assertEqual([row["lemma"] for row in due], ["Artikel"])

    def test_spiel_ok_then_double_recycle_to_stable(self):
        self.upsert()
        first = self.check("ok", on="2026-10-18")
        self.assertEqual(first["status"], "recycling")
        self.assertEqual(first["streak_ok"], 1)
        self.assertEqual(first["next_due"], "2026-10-19")
        second = self.check("ok", on="2026-10-19")
        self.assertEqual(second["status"], "stable")
        self.assertEqual(second["streak_ok"], 2)
        self.assertEqual(second["next_due"], "2026-10-22")

    def test_fail_from_stable_returns_to_weak(self):
        self.upsert(dict(self.base, status="stable", streak_ok=2, next_due="2026-10-18"))
        item = self.check("fail")
        self.assertEqual(item["status"], "weak")
        self.assertEqual(item["streak_ok"], 0)

    def test_teacher_may_record_gym_check(self):
        self.upsert()
        item = self.check("fail", profession="Teacher", workflow="teacher-reinforcement")
        self.assertEqual(item["recorded"]["profession"], "teacher")
        recovered = self.check("ok", profession="Teacher", workflow="teacher-reinforcement", on="2026-10-19")
        self.assertEqual(recovered["status"], "recycling")
        self.assertEqual(recovered["streak_ok"], 1)


if __name__ == "__main__":
    unittest.main()
