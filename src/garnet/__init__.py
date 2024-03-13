"""Contains the entry point for the application"""

try:
    from ._version import __version__  # noqa: F401
except ImportError:
    __version__ = "unknown"


def Garnet():  # noqa: N802
    """Needed for backward compatibility because mantid workbench does "from garnet import Garnet" to import"""
    from .garnet import Garnet as garnet  # noqa: N813

    return garnet()
