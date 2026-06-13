# Contributing

Thanks for helping improve `oc-opsdevnz`! This document mirrors the workflow we use for `op-opsdevnz`, with staging-safe defaults and tests for every change.

## Development Environment

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

We keep tooling in `pyproject.toml`, so editable installs are enough for tests and packaging.

## Common Tasks

| Task      | Command                                     |
|-----------|---------------------------------------------|
| Lint      | `ruff check src tests`                      |
| Tests     | `pytest --color=yes --durations=10`         |
| Build     | `python -m build`                           |

## Commit Signing

All commits must be signed. We accept SSH (`gpg.format = ssh`) or GPG
signatures. The signing key should be associated with an email address that
identifies a human contributor — not an anonymous or unattributable key.

This requirement exists because:

- It establishes a chain of human accountability for every change.
- It protects against supply-chain attacks where an unattributed actor
  introduces code.
- It allows us to welcome AI-assisted contributions while maintaining a
  clear line of human responsibility.

**AI-assisted contributions are welcome.** Code drafted, reviewed, or
refined with the help of an LLM or AI coding assistant is fine. But the
commit itself must be signed by a human who has reviewed the change and
stands behind it.

To configure commit signing:

```bash
git config commit.gpgsign true
git config gpg.format ssh           # or "openpgp" for GPG
git config user.signingkey "ssh-ed25519 AAAA..."
```

GitHub verifies signed commits with a "Verified" badge. Unsigned commits
will be asked to be re-submitted with a signature before merge.

## Pull Requests

1. Create a feature branch.
2. Make your changes — AI assistance is welcome; human review is required.
3. Update/add tests for behavioural changes (HTTP error handling, CLI flows, etc.).
4. Run `ruff` and `pytest` locally (CI will enforce the same).
5. Update documentation (`README.md`, `CHANGELOG.md`, `RELEASING.md`) when behaviour or release steps change.
6. Sign your commits (see above).
7. Open a PR and keep CI green.

## Cutting a Release

See [RELEASING.md](RELEASING.md) for the checklist, including TestPyPI → PyPI steps and staging/prod guardrails.
