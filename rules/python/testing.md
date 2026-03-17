---
paths:
  - "**/*.py"
  - "**/*.pyi"
---
# Python Testing

> This file extends [common/testing.md](../common/testing.md) with Python specific content.

## Framework

Use **pytest** as the testing framework.

## Running Tests

Always use the `just` entrypoint — it loads the required environment variables before pytest:

```bash
just test
```

Direct invocation (env vars must already be set):

```bash
uv run pytest -m "not e2e" --no-cov -q
```

## Test Markers

```python
import pytest

# Tests requiring a real Postgres container (Jenkins sidecar or local Docker)
@pytest.mark.testAgainstPostgres
def test_postgres_integration():
    ...

# End-to-end tests with side effects — excluded from default runs
@pytest.mark.e2e
def test_full_flow():
    ...
```

Default run excludes `e2e`. Tests not marked `testAgainstPostgres` must mock all database connections.

## Reference

See skill: `python-testing-patterns` for detailed pytest patterns, fixtures, mocking strategy, and project-specific conventions.
