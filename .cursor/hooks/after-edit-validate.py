#!/usr/bin/env python3
"""If a task.md was edited, run the acceptance gate and return the report."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))


def _path_from_payload(payload: dict) -> Path | None:
    for key in ("file_path", "path", "file", "uri"):
        val = payload.get(key)
        if isinstance(val, str) and val:
            return Path(val)
    file = payload.get("file")
    if isinstance(file, dict):
        for key in ("path", "file_path"):
            val = file.get(key)
            if isinstance(val, str) and val:
                return Path(val)
    return None


def main() -> None:
    raw = sys.stdin.read()
    try:
        payload = json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError:
        json.dump({}, sys.stdout)
        return

    path = _path_from_payload(payload)
    if path is None or path.name != "task.md":
        json.dump({}, sys.stdout)
        sys.stdout.write("\n")
        return

    try:
        from riga_lib import parse_task
        from validate_submission import check_acceptance, format_report

        task = parse_task(path)
        errors = check_acceptance(task)
        report = format_report(task, errors)
    except Exception as exc:  # noqa: BLE001
        report = f"Riga gate could not parse {path}: {exc}"

    json.dump({"additional_context": report}, sys.stdout)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
