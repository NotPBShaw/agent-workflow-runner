# Agent Workflow Runner

Run AI agent task plans with retries and structured output.

[![CI](https://github.com/NotPBShaw/agent-workflow-runner/actions/workflows/ci.yml/badge.svg)](https://github.com/NotPBShaw/agent-workflow-runner/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Python workflow runner for AI-agent style task execution with retries, dependency ordering, and run reports.

## Quickstart

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
python -m workflow_runner.cli --output run_artifacts/report.json
cat run_artifacts/report.json
```

## Features

- Directed task execution order
- Step retries with max-attempt policy
- JSON run artifacts
- Unit tests and CI workflow

## Usage

Define tasks programmatically or follow `examples/tasks.md`:

```python
from pathlib import Path
from workflow_runner.core import Task
from workflow_runner.runner import execute_plan

tasks = [Task("retrieve"), Task("rank"), Task("answer")]
execute_plan(tasks, lambda _: None, Path("run_artifacts/report.json"))
```

## Development

```bash
make test
```

## License

MIT — see [LICENSE](LICENSE).
