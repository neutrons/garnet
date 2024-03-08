"""Global settings for Garnet."""
from contextlib import contextmanager

from mantid.kernel import ConfigService

debug_init = False


def init_debug() -> None:
    """Initialize the debug flag."""
    global debug_init  # noqa
    if not debug_init:
        debug_init = True
        global debug_garnet  # noqa
        debug_garnet = False


def update_debug_enabled(update_value: bool) -> None:
    """Update the debug flag."""
    global debug_garnet  # noqa
    debug_garnet = update_value


def get_debug_enabled() -> bool:
    """Get the debug flag."""
    return debug_garnet


@contextmanager
def set_log_level(level: str):
    """Small context manager to temporarily set the log level"""
    config = ConfigService.Instance()
    current_level = config["logging.loggers.root.level"]
    config.setLogLevel(level, True)

    try:
        yield
    finally:
        config.setLogLevel(current_level, True)
