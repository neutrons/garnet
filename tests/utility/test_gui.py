"""Test the garnet.garnet.gui function

This is the entry point for the GUI application.
"""

import sys
from unittest import mock
from unittest.mock import patch

import pytest
from garnet.garnet import gui


def test_gui_version():
    """Test the version flag."""
    t_argv = sys.argv.copy()
    sys.argv.append("--version")
    with pytest.raises(SystemExit) as excinfo:
        gui()
    assert excinfo.value.code is None
    sys.argv = t_argv


@patch("garnet.garnet.QApplication")
@patch("garnet.garnet.Garnet")
def test_gui(mock_garnet: mock, mock_qtapp: mock):
    """Test the GUI entry point."""
    with pytest.raises(SystemExit) as excinfo:
        gui()

    assert excinfo.type == SystemExit
    assert mock_garnet.called
    assert mock_qtapp.called
