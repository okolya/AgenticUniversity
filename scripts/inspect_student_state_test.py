#!/usr/bin/env python3
"""Self-tests for the bounded Student-state reader."""

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))
import student_store  # noqa: E402

SCRIPT = Path(__file__).with_name("inspect-student-state.py")
SPEC = importlib.util.spec_from_file_location("inspect_student_state", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class InspectStudentStateTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        self.store = student_store.StudentStore(self.root)
        for student_id in ("mykola", "other"):
            self.write(student_id, f"id: {student_id}\nstatus: registered\n\n## Active enrollments\n")

    def write(self, student_id, text):
        self.store.write_document(student_id, text, actor="Rector/test")

    def tearDown(self):
        self.tempdir.cleanup()

    def test_returns_only_selected_student(self):
        result = MODULE.inspect_state(self.root, "mykola", ["identity"])
        self.assertEqual(result["status"], "available/no-active-workflow")
        self.assertEqual(result["identity"]["id"], "mykola")
        self.assertNotIn("other", str(result))

    def test_student_id_matching_is_case_insensitive(self):
        result = MODULE.inspect_state(self.root, "Mykola", ["identity"])
        self.assertEqual(result["student_id"], "mykola")
        self.assertEqual(result["identity"]["id"], "mykola")

    def test_rejects_unregistered_student(self):
        with self.assertRaises(MODULE.MissingStateError):
            MODULE.inspect_state(self.root, "missing", ["identity"])

    def test_missing_store_is_distinguished_from_unavailable_state(self):
        with tempfile.TemporaryDirectory() as empty:
            with self.assertRaises(MODULE.MissingStateError):
                MODULE.inspect_state(Path(empty), "mykola", ["identity"])
            self.assertFalse((Path(empty) / student_store.DB_NAME).exists())

    def test_rejects_invalid_student_id(self):
        with self.assertRaises(MODULE.InspectionError):
            MODULE.inspect_state(self.root, "../etc", ["identity"])

    def test_rejects_unknown_selector(self):
        with self.assertRaises(MODULE.InspectionError):
            MODULE.inspect_state(self.root, "mykola", ["private-notes"])

    def test_active_workflow_is_explicit(self):
        self.write(
            "mykola",
            "id: mykola\nstatus: registered\n\n"
            "## Active enrollments\n"
            "- public route: `AI Engineering`\n"
            "- status: active\n",
        )
        result = MODULE.inspect_state(self.root, "mykola", ["active-enrollments"])
        self.assertEqual(result["status"], "available/active-workflow")
        self.assertEqual(result["active_enrollments"][0]["status"], "active")


if __name__ == "__main__":
    unittest.main()
