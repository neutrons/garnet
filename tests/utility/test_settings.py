"""Test for the settings module."""
import unittest
from typing import Any

from garnet.helpers.settings import get_debug_enabled, init_debug, set_log_level, update_debug_enabled
from mantid.kernel import ConfigService


class TestDebugSettings(unittest.TestCase):
    """Test for the debug settings."""

    def setUp(self: Any):
        """Set up the test."""
        init_debug()

    def test_init_debug(self: Any):
        """Test that the debug flag is initialized to False."""
        assert get_debug_enabled() is False

    def test_update_debug_enabled(self: Any):
        """Test that the debug flag is updated."""
        update_debug_enabled(True)
        assert get_debug_enabled() is True

    def test_set_log_level(self: Any):
        """Test that the log level is set correctly with the context manager."""
        config = ConfigService.Instance()
        current_level = config["logging.loggers.root.level"]

        with set_log_level("debug"):
            assert config["logging.loggers.root.level"] == "debug"

        assert config["logging.loggers.root.level"] == current_level
