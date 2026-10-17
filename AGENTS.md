# AGENTS.md

## Rules

- Before starting a task, check the applicable development standards in `docs/standards/`.
- Before modifying files, check applicable `AGENTS.md` files along the directory hierarchy. Keep directory-specific
  rules in the nearest `AGENTS.md`.

| Standard       | When to read                |
|----------------|-----------------------------|
| `branching.md`         | Creating or naming branches        |
| `project_structure.md` | Creating, moving, or removing files |

## Tooling

- Use [uv](https://docs.astral.sh/uv/) for Python package and project management.
- Use `pytest-asyncio` with `asyncio_mode = auto`; do not explicitly add `@pytest.mark.asyncio`.
- Store temporary files in `tmp/<YYYYMMDD>/`.

## Markdown

- Keep it simple and structured. Avoid long blocks of text.
- Prefer: diagrams > tables > short lists.

| Format      | Use for                                                                |
|-------------|------------------------------------------------------------------------|
| Mermaid     | Flows, sequences, states, architecture, responsibilities, transactions |
| Tables      | Fields, rules, mappings, comparisons                                   |
| Short lists | Simple facts, notes                                                    |

- Do not repeat information already conveyed clearly by diagrams or tables.