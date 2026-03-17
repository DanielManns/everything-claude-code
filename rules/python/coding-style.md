---
paths:
  - "**/*.py"
  - "**/*.pyi"
---
# Python Coding Style

> This file extends [common/coding-style.md](../common/coding-style.md) with Python specific content.

## Standards

- Follow **PEP 8** conventions
- Use **type annotations** on all function signatures

## Immutability

Prefer immutable data structures:

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    name: str
    email: str

from typing import NamedTuple

class Point(NamedTuple):
    x: float
    y: float
```

## Package Manager & Task Runner

- Use **uv** for dependency management and virtual environments (`uv sync`, `uv run`)
- Use **just** as the task runner (`just test`, `just main`, `just setup`)
- Never use `pip install` directly — always go through `uv`

## Formatting & Linting

- **ruff** for both formatting and linting (replaces black + isort + flake8)
  - Format: `ruff format`
  - Lint: `ruff check`
- Do **not** use `black` or `isort` — `ruff` handles both

## Reference

See skill: `python-patterns` for comprehensive Python idioms and patterns.
