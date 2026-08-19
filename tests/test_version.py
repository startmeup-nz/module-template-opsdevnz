"""Tests for package metadata consistency."""

from importlib.metadata import version


def test_version_consistency():
    """Ensure __version__ matches what pyproject.toml declares."""
    from template_opsdevnz import __version__

    assert __version__ == version("YOUR-MODULE-opsdevnz")
