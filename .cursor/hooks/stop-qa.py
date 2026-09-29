#!/usr/bin/env python3
"""If draft/ready tasks still fail the gate, ask the agent to finish QA."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))


def main() -> None:
    sys.stdin.read()
    try:
        from riga_lib import find_task_files, parse_task
        from validate_submission import check_acceptance
    except Exception:
        json.dump({}, sys.stdout)
        sys.stdout.write("\n")
        return

    failing = []
    roots = [ROOT / "submissions" / "drafts", ROOT / "submissions" / "ready"]
    for root in roots:
        if not root.exists():
            continue
        for path in find_task_files(root):
            try:
                errors = check_acceptance(parse_task(path))
            except Exception as exc:  # noqa: BLE001
                failing.append(f"{path}: parse error ({exc})")
                continue
            if errors:
                failing.append(f"{path} ({len(errors)} issues)")

    if not failing:
        json.dump({}, sys.stdout)
        sys.stdout.write("\n")
        return

    msg = (
        "Riga QA is not clean. Run python3 scripts/qa_gate.py on these tasks "
        "and fix them before telling the user the item is paste-ready:\n- "
        + "\n- ".join(failing[:8])
    )
    json.dump({"followup_message": msg}, sys.stdout)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
