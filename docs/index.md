# <module-name>

<one-line description>

- **Status:** Development
- **License:** Apache 2.0
- **Python:** 3.12+

## Overview

<2-3 paragraph overview of the module's purpose and capabilities>

## Quick Start

```bash
# Install
uv pip install <module-name>

# Run the CLI
<cli-command> --help
```

## Documentation

- **[Specifications](specs/)** — Functional and non-functional requirements
- **[Design Decisions](design/README.md)** — Architecture choices and rationale
- **[User Stories](stories/README.md)** — Persona-driven narratives

## Development

```bash
# Install with dev dependencies
uv sync --extra dev

# Run tests
uv run python -m pytest tests/ -v

# Lint
uv run ruff check src tests

# Serve documentation (human only)
uv run zensical serve

# Build docs (verify render)
uv run zensical build
```

## Related

- [OpsDev.nz Collective](https://opsdev.nz) — Parent project
- [Module template](https://github.com/startmeup-nz/practice-template-opsdevnz)
