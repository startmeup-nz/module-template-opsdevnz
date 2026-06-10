# AGENTS.md — <module-name>

**Audience:** Contributors and AI assistants working on the <module-name> module.

## IMPORTANT: No Autonomous Commits

AI assistants must NOT commit changes to this repository. Always stage changes
and describe what was done, then wait for human review and confirmation before
committing. This ensures all changes have human oversight.

## Module Scope

<brief description of what this module does — 2-3 sentences>

## Zensical Documentation Server

**AI assistants should NOT start the Zensical dev server.** The human developer
controls when and where `zensical serve` runs — it binds a port and stays
running, which is a human-level decision.

AI assistants MAY:
- Run `uv run zensical build` to verify docs render without errors
- Edit `zensical.toml` configuration
- Edit markdown files under `docs/`

## Development Workflow

```bash
# Install dev dependencies
uv sync --extra dev

# Run tests
uv run python -m pytest tests/ -v

# Lint
uv run ruff check src tests

# Build docs (verify render, no errors)
uv run zensical build
```

## Testing

```bash
# Run all tests
uv run python -m pytest tests/ -v

# Run a specific test file
uv run python -m pytest tests/test_<name>.py -v
```

## Versioning

- **0.0.x** — Incubation phase, rapid iteration, breaking changes expected
- **0.1.0** — First public release, API stabilises
- **1.0.0** — Stable release, semantic versioning enforced

## Current Focus

- <current development priorities — 3-4 bullet points>

## Related

- [OpsDev.nz Collective](https://opsdev.nz) — Parent project
- [Module template](https://github.com/startmeup-nz/practice-template-opsdevnz)
