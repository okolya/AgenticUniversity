#!/usr/bin/env python3
"""Resolve one authenticated Student and return bounded state as JSON.

This is the bounded reader over the core's SQLite Student state store
(`scripts/student_store.py`). It deliberately reads only the
selected Student document; selectors determine which sections are returned.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import student_store  # noqa: E402


SELECTORS = {
    "identity": "identity",
    "active-enrollments": "active_enrollments",
    "plans": "plans",
    "current-lesson": "current_lesson",
    "next-actions": "next_actions",
    "checkpoints": "checkpoints",
    "stop-conditions": "stop_conditions",
    "handoffs": "handoffs",
}


class InspectionError(student_store.StoreError):
    """A fail-closed inspection error."""


MissingStateError = student_store.MissingStateError
UnavailableStateError = student_store.UnavailableStateError


def fail(message: str) -> None:
    print(json.dumps({"status": "unavailable", "error": message}, ensure_ascii=False))
    raise SystemExit(1)


def parse_student(content: str) -> tuple[dict[str, str], dict[str, str]]:
    lines = content.splitlines()
    fields: dict[str, str] = {}
    sections: dict[str, str] = {}
    current: str | None = None
    buffer: list[str] = []
    for line in lines:
        if line.startswith("## "):
            if current is not None:
                sections[current] = "\n".join(buffer).strip()
            current = line[3:].strip()
            buffer = []
        elif current is None:
            match = re.match(r"^([a-z][a-z_ -]+):\s*(.*)$", line)
            if match:
                fields[match.group(1).replace(" ", "_")] = match.group(2).strip()
        else:
            buffer.append(line)
    if current is not None:
        sections[current] = "\n".join(buffer).strip()
    return fields, sections


def workflow_facts(sections: dict[str, str]) -> dict[str, object]:
    enrollment = sections.get("Active enrollments", "")
    plan_names = [
        name for name in sections if name.lower().startswith("active ") and name.lower().endswith(" plan")
    ]
    current_lesson = ""
    next_actions: list[str] = []
    checkpoints: list[str] = []
    stop_conditions: list[str] = []
    handoffs: list[str] = []
    enrollment_summary: dict[str, object] = {}
    for label, key in (
        ("public route", "public_route"),
        ("current mode", "mode"),
        ("status", "status"),
    ):
        match = re.search(rf"(?im)^\s*- {re.escape(label)}:\s*(.+)$", enrollment)
        if match:
            enrollment_summary[key] = match.group(1).strip().strip("`")
    enrollment_actions = [
        re.sub(r"^\s*\d+\.\s+", "", line).strip()
        for line in enrollment.splitlines()
        if re.match(r"^\s*\d+\.\s+", line)
    ]
    if enrollment_actions:
        enrollment_summary["next_actions"] = enrollment_actions
    for name in plan_names:
        body = sections[name]
        lesson = re.search(r"(?im)^- current Lesson:\s*`?([^`\n]+)", body)
        if lesson:
            current_lesson = lesson.group(1).strip()
        for line in body.splitlines():
            stripped = line.strip()
            if re.match(r"^\d+\.\s+", stripped) and "next action" in body.lower():
                next_actions.append(re.sub(r"^\d+\.\s+", "", stripped))
            if stripped.lower().startswith("- checkpoint:"):
                checkpoints.append(stripped.split(":", 1)[1].strip())
            if stripped.lower().startswith("- stop condition:"):
                stop_conditions.append(stripped.split(":", 1)[1].strip())
            if "handoff" in stripped.lower():
                handoffs.append(stripped.lstrip("- ").strip())
    active = bool(enrollment.strip() or plan_names)
    return {
        "active": active,
        "active_enrollments": [enrollment_summary] if enrollment_summary else [],
        "plans": plan_names,
        "current_lesson": current_lesson,
        "next_actions": next_actions,
        "checkpoints": checkpoints,
        "stop_conditions": stop_conditions,
        "handoffs": handoffs,
    }


def inspect_state(state_dir: Path, student_id: str, selectors: list[str]) -> dict[str, object]:
    try:
        student_id = student_store.normalize_student_id(student_id)
    except student_store.UnavailableStateError as exc:
        raise InspectionError(str(exc)) from exc
    store = student_store.StudentStore(state_dir)
    fields, sections = parse_student(store.read_document(student_id))
    facts = workflow_facts(sections)
    active = bool(facts["active"])
    result_status = "available/active-workflow" if active else "available/no-active-workflow"
    requested = selectors or list(SELECTORS)
    unknown = sorted(set(requested) - set(SELECTORS))
    if unknown:
        raise InspectionError(f"unknown selector(s): {', '.join(unknown)}")
    result: dict[str, object] = {
        "status": result_status,
        "student_id": student_id,
    }
    if "identity" in requested:
        result["identity"] = {"id": fields.get("id", ""), "status": fields.get("status", "")}
    for selector in requested:
        if selector == "identity":
            continue
        result[SELECTORS[selector]] = facts[SELECTORS[selector]]
    return result


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state-dir", type=Path, default=None)
    parser.add_argument("--student-id", default=os.environ.get("AGENTIC_UNIVERSITY_STUDENT_ID"))
    parser.add_argument("--select", action="append", default=[], dest="selectors")
    args = parser.parse_args(argv)
    if not args.student_id:
        fail("authenticated Student ID is required via --student-id or AGENTIC_UNIVERSITY_STUDENT_ID")
    try:
        result = inspect_state(
            (args.state_dir or student_store.default_state_dir()).resolve(), args.student_id, args.selectors
        )
    except MissingStateError as exc:
        print(json.dumps({"status": "missing", "error": str(exc)}, ensure_ascii=False))
        return 1
    except (student_store.StoreError, OSError) as exc:
        fail(str(exc))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
