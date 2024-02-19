"""
Contains the entry point for the application
and
Short description of the package.

"""
try:
    from ._version import __version__  # noqa: F401
except ImportError:
    __version__ = "unknown"

def Garnet():  # pylint: disable=invalid-name
    """This is needed for backward compatibility because mantid workbench does "from garnet import Garnet" """
    from .garnet import Garnet as garnet  # pylint: disable=import-outside-toplevel

    return garnet()
