"""Logger for GARNET"""
from typing import Any

from mantid.kernel import Logger as MantidLogger

from garnet.helpers.settings import get_debug_enabled, init_debug, set_log_level


class Logger(MantidLogger):
    """Logger class for GARNET

    This is a thin wrapper for the Mantid logger class. It adds the ability to
    log debug and information messages
    """

    def __init__(self: Any, name: str = "GARNET") -> None:
        """Initialize the logger"""
        super().__init__(name)
        init_debug()

    def debug(self: Any, message: str) -> None:
        """Log a debug message if the debug flag is enabled else default to mantid logger"""
        if get_debug_enabled():
            with set_log_level("debug"):
                super().debug(message)
        else:
            super().debug(message)

    def information(self: Any, message: str) -> None:
        """Log an information message if the debug flag is enabled else default to mantid logger"""
        if get_debug_enabled():
            with set_log_level("information"):
                super().information(message)
        else:
            super().information(message)
