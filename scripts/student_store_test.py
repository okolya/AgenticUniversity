#!/usr/bin/env python3
"""Self-tests for the SQLite Student state store."""

import sys
import tempfile
import unittest
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


if __name__ == "__main__":
    unittest.main()
