---
paths:
  - "**/*.py"
  - "**/*.pyi"
---
# Python Hooks

> This file extends [common/hooks.md](../common/hooks.md) with Python specific content.

## PostToolUse Hooks

Configure in `~/.claude/settings.json`:

- **ruff format**: Auto-format `.py` files after edit (`ruff format <file>`)
- **ruff check**: Auto-lint `.py` files after edit (`ruff check --fix <file>`)
- Do **not** configure black, isort, mypy, or pyright — project uses ruff only

## Warnings

- Warn about `print()` statements in edited files (use `logging` module instead)
