# AGENTS.md

## Rules

- Keep global conventions here, development standards in `docs/standards/`, and consult them as needed.
- Keep directory-specific rules in the nearest `AGENTS.md`.
- Before modifying files, check and load applicable `AGENTS.md` files along the directory hierarchy. For example, read `docs/designs/AGENTS.md` before modifying files under `docs/designs/`.

## Tooling

- Use [uv](https://docs.astral.sh/uv/) for Python package and project management.
- Use `pytest-asyncio` with `asyncio_mode = auto`; do not explicitly add `@pytest.mark.asyncio`.
- Store temporary files in `tmp/<YYYYMMDD>/`.

## Markdown

- Keep it simple and structured. Avoid long blocks of text.
- Prefer: diagrams > tables > short lists.

| Format | Use for |
| --- | --- |
| Mermaid | Flows, sequences, states, architecture, responsibilities, transactions |
| Tables | Fields, rules, mappings, comparisons |
| Short lists | Simple facts, notes |

- Do not repeat information already conveyed clearly by diagrams or tables.