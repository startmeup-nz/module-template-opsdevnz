# Releasing `<module-name>`

All releases are automated through GitHub Actions and [Trusted Publishing
(OIDC)](https://docs.pypi.org/trusted-publishers/). No API tokens are stored
or managed — pushing a version tag triggers the pipeline.

## Conventions

| What | Rule |
|------|------|
| Versioning | [Semantic Versioning](https://semver.org) |
| Tag format | `v<version>` (e.g. `v0.1.0`) — must be signed (`git tag -s`) |
| Branch | `main` only — tags must point at a commit on `main` |
| Auth | Trusted Publishing (OIDC) — no API tokens |

## Prerequisites

- `uv` installed
- Clean `main` branch, CI green
- PyPI Trusted Publisher configured on Test PyPI and PyPI (see
  `docs/release-process.md`)

## Release Workflow

### 1. Prepare

On a branch off `main`:

```bash
# Bump version in pyproject.toml
version = "0.1.0"

# Move changelog entries from [Unreleased] to [0.1.0]
```

### 2. Merge and tag

```bash
git checkout main
git pull origin main
git tag -s v0.1.0 -m "v0.1.0"
git push origin v0.1.0
```

### 3. Watch CI

Pushing the tag fires `.github/workflows/publish.yml`:

| Job | What it does |
|-----|-------------|
| `test-pypi` | Builds wheel, publishes to Test PyPI, smoke-tests |
| `pypi` | Runs only if test-pypi passes, publishes to real PyPI |

If the Test PyPI publish or smoke test fails, fix the issue, bump the patch
version, and tag again.

### 4. Verify

```bash
pip install <module-name>==0.1.0
<module-cli> --version
```

## Dry-run releases

To validate the pipeline without publishing to real PyPI, temporarily comment
out the `pypi` job in `.github/workflows/publish.yml`, tag and push, then
restore it after confirming Test PyPI succeeds.
