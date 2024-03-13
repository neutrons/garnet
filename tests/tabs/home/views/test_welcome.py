"""Test the welcome tab"""

import pytest
from garnet import Garnet, __version__


def test_welcome_label(qtbot: pytest.fixture):
    """Test starting the app"""
    # initialization
    garnet = Garnet()
    garnet.show()
    qtbot.addWidget(garnet)
    qtbot.waitUntil(garnet.show, timeout=5000)

    # check there is a landing tab
    tabs = garnet.main_window.tabs
    assert tabs.currentWidget().__class__.__name__ == "HomeView"
    assert tabs.currentWidget().label_welcome.text().startswith("Welcome to GARNET")


def test_mainwindow(qtbot: pytest.fixture):
    """Test that the application starts successfully"""
    garnet = Garnet()
    qtbot.addWidget(garnet)
    garnet.show()
    assert garnet.isVisible()
    assert garnet.windowTitle() == f"GARNET - {__version__}"
