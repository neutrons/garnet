"""Tests for the Logger class in garnet/logger.py."""

from mantid.kernel import Logger as mantid_logger  # noqa: N813

from garnet.helpers.logger import Logger


def test_get_logger():
    """Test getting the logger."""
    logger_name = "custom_logger"
    logger = Logger(logger_name)
    logger.get(logger_name)

    # Assert that the returned logger instance is correct
    assert isinstance(logger, mantid_logger)
