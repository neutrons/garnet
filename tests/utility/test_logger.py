"""Test for the logger module."""
import unittest
from typing import Any
from unittest import mock
from unittest.mock import patch

from garnet.helpers.logger import Logger


class TestLogger(unittest.TestCase):
    """Test for the logger class."""

    @patch("garnet.helpers.logger.set_log_level")
    @patch("garnet.helpers.logger.get_debug_enabled")
    @patch("garnet.helpers.logger.lg.debug")
    def test_debug_enabled_debug(
        self: Any, mock_debug: mock.patch, mock_get_debug_enabled: mock.patch, mock_set_log_level: mock.patch
    ):
        """Test that the debug message is logged when the debug flag is enabled."""
        mock_get_debug_enabled.return_value = True
        logger = Logger()
        logger.debug("Test Debug Message")
        mock_set_log_level.assert_called_with("debug")
        mock_debug.assert_called_with("Test Debug Message")

    @patch("garnet.helpers.logger.set_log_level")
    @patch("garnet.helpers.logger.get_debug_enabled")
    @patch("garnet.helpers.logger.lg.debug")
    def test_debug_disabled_debug(
        self: Any, mock_debug: mock.patch, mock_get_debug_enabled: mock.patch, mock_set_log_level: mock.patch
    ):
        """Test that the debug message is not logged when the debug flag is disabled."""
        mock_get_debug_enabled.return_value = False
        logger = Logger()
        logger.debug("Test Debug Message")
        mock_set_log_level.assert_not_called()
        mock_debug.assert_called_with("Test Debug Message")

    @patch("garnet.helpers.logger.set_log_level")
    @patch("garnet.helpers.logger.get_debug_enabled")
    @patch("garnet.helpers.logger.lg.information")
    def test_debug_enabled_information(
        self: Any, mock_information: mock.patch, mock_get_debug_enabled: mock.patch, mock_set_log_level: mock.patch
    ):
        """Test that the information message is logged when the debug flag is enabled."""
        mock_get_debug_enabled.return_value = True
        logger = Logger()
        logger.information("Test Information Message")
        mock_set_log_level.assert_called_with("information")
        mock_information.assert_called_with("Test Information Message")

    @patch("garnet.helpers.logger.set_log_level")
    @patch("garnet.helpers.logger.get_debug_enabled")
    @patch("garnet.helpers.logger.lg.information")
    def test_debug_disabled_information(
        self: Any, mock_information: mock.patch, mock_get_debug_enabled: mock.patch, mock_set_log_level: mock.patch
    ):
        """Test that the information message is not logged when the debug flag is disabled."""
        mock_get_debug_enabled.return_value = False
        logger = Logger()
        logger.information("Test Information Message")
        mock_set_log_level.assert_not_called()
        mock_information.assert_called_with("Test Information Message")
