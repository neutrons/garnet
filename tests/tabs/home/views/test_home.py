"""Test the home view"""
import pytest
from garnet.home.view import HomeView
from qtpy import QtCore


def test_plan_name(qtbot: pytest.fixture):
    """Test that the plan_name LineEdit is required"""
    window = HomeView()
    qtbot.addWidget(window)
    window.show()

    assert window.plan_name.text() == ""
    assert window.save_button.isEnabled() is False

    qtbot.keyClicks(window.plan_name, "Plan Name")
    assert window.save_button.isEnabled() is True


def test_wavelength(qtbot: pytest.fixture):
    """Test that the wavelength LineEdit is required and has default value"""
    window = HomeView()
    qtbot.addWidget(window)
    window.show()

    assert window.wavelength.text() == str(window.wavelength.default_value)
    assert window.save_button.isEnabled() is False

    qtbot.keyClicks(window.plan_name, "Plan Name")
    assert window.save_button.isEnabled() is True

    for _ in range(10):
        qtbot.keyClick(window.wavelength, QtCore.Qt.Key_Backspace)
    assert window.save_button.isEnabled() is False
