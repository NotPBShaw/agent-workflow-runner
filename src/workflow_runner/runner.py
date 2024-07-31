from __future__ import annotations

import json
from pathlib import Path

from .core import Task, run_task


def execute_plan(tasks: list[Task], handler, output_file: Path) -> None:
    report = []
    for task in tasks:
        attempts = run_task(task, handler)
        report.append({"task": task.name, "attempts": attempts, "status": "ok"})
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(json.dumps({"tasks": report}, indent=2))
