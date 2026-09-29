#!/usr/bin/env python3
"""Inject Riga operating context at session start."""
from __future__ import annotations

import json
import sys

CONTEXT = """Riga STEM (Snorkel) session. Guidelines V1.3, 16 July 2026.

Before drafting: read AGENTS.md and docs/platform/ui-fields.md.
Every problem is one original, self-contained, uniquely answerable STEM question
written in the voice of a working PhD in that field — not chatbot cadence.
After editing any task.md, run: python3 scripts/qa_gate.py <file>
Do not mark ready until independently_verified is true and the gate PASSes.
Paste order: left-pane stump test → Paste from Prompt → domain/subdomain/
justification → steps → answer $...$ → In-App LaTeX → types/concepts →
Automated Checks Only → Quality Review.
User pastes into EK_Riga_Production / Riga Submission. You do not submit.
Biology live dropdown: data/catalogs/platform_domains.json
(Genetics and Genomics is not selectable on this account).
"""


def main() -> None:
    sys.stdin.read()
    json.dump({"additional_context": CONTEXT.strip()}, sys.stdout)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
