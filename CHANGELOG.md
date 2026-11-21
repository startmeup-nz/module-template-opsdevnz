# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

> **Instantiating a new module from this template?** This changelog
> documents the template's own history. To start your module's changelog
> fresh, run: `mv CHANGELOG.md.template CHANGELOG.md`

## [Unreleased]

### Added

- `tests/test_version.py` — version consistency test ensuring `__version__`
  matches pyproject.toml.
- Pre-push `uv.lock` freshness gate in `.githooks/` (see CONTRIBUTING.md).
- `CHANGELOG.md.template` plus a self-terminating reset note in this
  changelog — instantiated modules start fresh with
  `mv CHANGELOG.md.template CHANGELOG.md`.
- Release-tag guard note in RELEASING.md: no tags until the
  `YOUR-MODULE-opsdevnz` placeholder is replaced.

### Fixed

- Version now read from package metadata via `importlib.metadata` instead of
  hardcoded string, matching pattern used by oc-opsdevnz and worklog-opsdevnz.
- `zensical.toml`: removed duplicate `language = "en"` under `[project]`
  (unrecognised by Zensical 0.1.x; theme settings belong under
  `[project.theme]`).

## [0.0.5]

### Changed

- Minimum Python version set to 3.12.

## [0.0.4]

### Changed

- Switched to uv-based workflow and added `py.typed` marker file.

## [0.0.3]

### Added

- Commit signing guidance in AGENTS.md.
- RELEASING.md with release checklist.

### Changed

- Updated AGENTS.md with Python-specific development workflow.

## [0.0.2]

### Changed

- Updated module template structure, README, and GitHub Actions dependencies.

## [0.0.1]

### Added

- Initial module scaffold from template-opsdevnz.
