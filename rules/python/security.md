---
paths:
  - "**/*.py"
  - "**/*.pyi"
---
# Python Security

> This file extends [common/security.md](../common/security.md) with Python specific content.

## Secret Management

Secrets are **never stored in environment variables or `.env` files**. They are mounted as plain files from Kubernetes Secrets into `$SECRETS_DIR` (default: `/secrets`):

```
$SECRETS_DIR/database/user    # PostgreSQL username
$SECRETS_DIR/database/pw      # PostgreSQL password
$SECRETS_DIR/hana/user        # HANA username
$SECRETS_DIR/hana/pw          # HANA password
$SECRETS_DIR/s3/key           # AWS access key ID
$SECRETS_DIR/s3/secret        # AWS secret access key
```

For local development use `SECRETS_DIR=local/.secrets`.

Application configuration (non-secret env vars) is handled via **Pydantic `BaseSettings`** — never read `os.environ` directly in application code:

```python
from pydantic_settings import BaseSettings, Field

class Settings(BaseSettings):
    database_host: str = Field(alias="DATABASE_HOST")
    secrets_dir: Path = Field(default=Path("/secrets"), alias="SECRETS_DIR")
```

## Security Scanning

- **ruff** handles security-relevant lint rules — run via `just test` or `ruff check`

## Reference

See command: `python-testing-patterns` for test secret file structure (`tests/static/secrets/`).
