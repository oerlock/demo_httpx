# Project Structure

This document defines the target project structure. Directories are created as needed.

## Directory Overview

```text
/
├── AGENTS.md
├── README.md
├── pyproject.toml
├── uv.lock
├── pytest.ini
├── .coveragerc
├── .gitattributes
├── manage.py
│
├── docs/
│   ├── standards/
│   ├── designs/
│   └── todo-list.md
│
├── src/                    # Examples organized by feature
├── tests/                  # Tests
├── requirements/           # Dependency snapshots (optional)
│
├── .example.env.d/         # Example environment configuration
├── .example.support/       # Example runtime support files (optional)
├── .env.d/                 # Local environment configuration (ignored)
├── .support/               # Local runtime support files (ignored)
├── experiments/            # Ongoing experiments (optional, ignored)
└── tmp/                    # Temporary files (ignored)
```

## Examples

Organize `src/` by HTTPX features and use cases. No fixed internal structure is required.

```text
src/
├── event_hooks/
├── auth/
├── timeouts/
└── ...
```

## Tests

Organize tests by example feature. Test files should use the `test_` prefix, and subdirectories can be added as needed.

```text
tests/
├── test_event_hooks.py
├── test_auth.py
└── ...
```
