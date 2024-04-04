"""Logger for GARNET"""

from mantid.kernel import Logger as MantidLogger


class Logger(MantidLogger):
    """Logger class for GARNET

    This is a thin wrapper for the Mantid logger class. It adds the ability to
    get the garnet logger in a simple way.
    """

    def get(self: MantidLogger, name: str = "garnet"):
        """Get the logger with the given name."""
        super().get(name)
