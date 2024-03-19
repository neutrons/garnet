"""Unit tests for garnet.helpers.ui_elements.base_statusbar.py BaseStatusBar"""

from garnet.helpers.ui_elements.base_statusbar import BaseStatusBar


def test_update_status_label():
    """Test updating the status label."""
    base_status_bar = BaseStatusBar()
    assert base_status_bar.status_label.text() == ""

    error_text = {1: "Error: Invalid input", 2: "Warning: Incomplete data"}
    base_status_bar.update_status_label(error_text)

    expected_text = "Error: Invalid input\nWarning: Incomplete data"
    assert base_status_bar.status_label.text() == expected_text

    base_status_bar.update_status_label({1: "", 2: ""})
    assert base_status_bar.status_label.text() == ""


def test_update_cwe_label():
    """Test updating the CWE label."""
    base_status_bar = BaseStatusBar()
    assert base_status_bar.cwe_label.text() == ""

    base_status_bar.update_cwe_label("Caution: Invalid input")
    assert base_status_bar.cwe_label.text() == "Caution: Invalid input"
