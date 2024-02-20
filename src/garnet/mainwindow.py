"""
Main Qt window
"""

from qtpy.QtWidgets import QVBoxLayout, QWidget, QTabWidget

from garnet.home.view import Home
from garnet.home.model import HomeModel
from garnet.home.presenter import HomePresenter


class MainWindow(QWidget):
    """Main widget"""

    def __init__(self, parent=None):
        super().__init__(parent)

        ### Create tabs here ###

        ### Home tab
        self.tabs = QTabWidget()
        home = Home(self)
        home_model = HomeModel()
        self.home_presenter = HomePresenter(home, home_model)
        self.tabs.addTab(home, "Home")

        ### Set tab layout
        layout = QVBoxLayout()
        layout.addWidget(self.tabs)

        self.setLayout(layout)

        # register child widgets to make testing easier
        self.home = home
