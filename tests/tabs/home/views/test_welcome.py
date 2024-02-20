from garnet.garnet import Garnet
from qtpy.QtWidgets import QApplication


def test_welcome_label():
    """Test starting the app"""

    # initialization
    _ = QApplication([])

    garnet = Garnet()
    garnet.show()

    # check there is a landing tab
    tabs = garnet.main_window.tabs
    assert tabs.currentWidget().__class__.__name__ == "HomeView"
    assert tabs.currentWidget().label_welcome.text() == "Welcome to GARNET"
