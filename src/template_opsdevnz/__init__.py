"""YOUR-MODULE-opsdevnz — short description."""

from importlib import metadata

try:
    __version__ = metadata.version("YOUR-MODULE-opsdevnz")
except metadata.PackageNotFoundError:
    __version__ = "0.0.0+local"
