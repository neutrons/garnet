"""Test the welcome tab"""

import pytest

from garnet.garnet import Garnet, __version__


class TestGarnetGUI:
    """Test the GARNET GUI"""

    @pytest.fixture(autouse=True, scope="class")
    def setup(self, qtbot: pytest.fixture):
        """Set up the test environment"""
        self.garnet = Garnet()
        qtbot.addWidget(self.garnet)
        self.garnet.show()
        qtbot.waitUntil(self.garnet.show, timeout=5000)
        yield
        self.garnet.close()

    def test_welcome_label(self):
        """Test the welcome label on the home tab"""
        tabs = self.garnet.main_window.tabs
        assert tabs.currentWidget().__class__.__name__ == "HomeView"
        assert tabs.currentWidget().label_welcome.text().startswith("Welcome to GARNET")

    def test_mainwindow(self):
        """Test that the main window is visible and has the correct title"""
        assert self.garnet.isVisible()
        assert self.garnet.windowTitle() == f"GARNET - {__version__}"
