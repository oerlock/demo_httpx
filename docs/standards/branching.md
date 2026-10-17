# Branching Guidelines

Use the following format for branch names:

```text
<type>/<scope>-<summary>
```

| Type | Purpose | Example |
| --- | --- | --- |
| `feature` | Add examples or features | `feature/event-hooks` |
| `fix` | Fix issues | `fix/timeout-example` |
| `docs` | Documentation changes | `docs/installation` |
| `refactor` | Code refactoring | `refactor/client-setup` |
| `test` | Tests and test infrastructure | `test/event-hooks` |
| `chore` | Project maintenance | `chore/upgrade-deps` |

## Conventions

- Use lowercase letters, numbers, and hyphens (`-`).
- Keep branch names short, clear, and descriptive.
- Keep each branch focused on a single goal where practical.
- Avoid vague names such as `temp`, `test1`, or `new-branch`.
