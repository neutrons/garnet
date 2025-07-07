"""Contains the entry point for the application"""

try:
    from ._version import __version__  # noqa: F401
except ImportError:
    __version__ = "unknown"

from garnet.garnet import Garnet

__all__ = ["Garnet"]
