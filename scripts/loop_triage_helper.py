#!/usr/bin/env python3
"""
MacBook Loop Analysis — Triage Helper
Updates STATE.md from shell scripts or cron. L1 report-only.

Usage:
  python3 loop_triage_helper.py <state_file> <gate_name> <PASS|FAIL|PENDING> [<notes>]

Environment:
  LOOP_PROJECT_ROOT — absolute path to the purchase analysis directory

Example:
  LOOP_PROJECT_ROOT=/home/sak/macbook-loop-analysis \
    python3 ~/.hermes/skills/data-science/macbook-loop-analysis/scripts/loop_triage_helper.py \
    STATE.md ram_verified PASS "64GB confirmed via System Report"
"""

import sys
import os
import re
import datetime
from pathlib import Path


def load_state(state_path: str) -> str:
    p = Path(state_path)
    if not p.exists():
        return p.read_text() if p.exists() else ""
    return p.read_text()


def save_state(state_path: str, content: str) -> None:
    p = Path(state_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content)


def update_gate(content: str, gate: str, status: str, notes: str = "") -> str:
    status = status.upper()
    if status not in ("PASS", "FAIL", "PENDING"):
        raise ValueError(f"Invalid status: {status}. Use PASS, FAIL, or PENDING")

    pattern = re.compile(
        rf"(^|(?<=\n))\| *{re.escape(gate)} *\| *[^|]* \| *[^|\n]*",
        re.IGNORECASE,
    )
    replacement = f"| {gate} | {status} | {notes} |"

    if pattern.search(content):
        new_content = pattern.sub(replacement, content)
    else:
        # Append to gate results section
        insert_marker = "## Gate Results"
        if insert_marker in content:
            new_content = content.replace(
                insert_marker,
                f"{insert_marker}\n| {gate} | {status} | {notes} |",
            )
        else:
            new_content = content + f"\n| {gate} | {status} | {notes} |\n"

    return new_content


def derive_verdict(content: str) -> str:
    gate_lines = re.findall(r"\| (\w+) \| (PASS|FAIL|PENDING) \|", content)

    hard_fail_gates = {"ram_verified", "warranty_verified"}

    fails = [g for g, s in gate_lines if s == "FAIL"]
    hard_fails = [g for g in fails if g in hard_fail_gates]
    passes = [g for g, s in gate_lines if s == "PASS"]

    if hard_fails:
        return "HOLD"
    if len(fails) >= 3:
        return "HOLD"
    if len(fails) >= 1:
        return "HOLD"

    if len(passes) >= 7:
        return "STRONG BUY"
    if len(passes) >= 5:
        return "BUY"
    return "PENDING"


def update_last_run(content: str) -> str:
    now = datetime.datetime.now().isoformat()
    return re.sub(r"last_run: .*", f"last_run: {now}", content)


def append_run_log(log_path: str, gate_lines: list, verdict: str) -> None:
    log = Path(log_path)
    log.parent.mkdir(parents=True, exist_ok=True)

    now = datetime.datetime.now().isoformat()
    gate_summary = ", ".join(gate_lines) if gate_lines else "no gates recorded"
    entry = f"\n--- Run: {now} ---\nOutcome: {verdict}\nGates: {gate_summary}\n"

    if log.exists():
        existing = log.read_text()
        if f"Run: {now}" not in existing:
            log.write_text(existing + entry)
    else:
        log.write_text(entry.lstrip("\n"))


def main():
    if len(sys.argv) < 4:
        print(__doc__)
        sys.exit(1)

    state_file = sys.argv[1]
    gate_name = sys.argv[2]
    status = sys.argv[3]
    notes = " ".join(sys.argv[4:]) if len(sys.argv) > 4 else ""

    # Resolve LOOP_PROJECT_ROOT if state_file is relative
    project_root = os.environ.get("LOOP_PROJECT_ROOT", "")
    if project_root and not os.path.isabs(state_file):
        state_file = os.path.join(project_root, state_file)

    content = load_state(state_file)
    new_content = update_gate(content, gate_name, status, notes)
    new_content = update_last_run(new_content)

    verdict = derive_verdict(new_content)
    new_content = re.sub(
        r"## Verdict: .*",
        f"## Verdict: {verdict}",
        new_content,
    )

    save_state(state_file, new_content)

    # Append to run log
    log_file = os.path.join(
        os.path.dirname(state_file), "loop-run-log.md"
    )
    append_run_log(log_file, [f"{gate_name}={status}"], verdict)

    print(f"{gate_name}: {status} → verdict: {verdict}")
    print(f"STATE written to {state_file}")


if __name__ == "__main__":
    main()
