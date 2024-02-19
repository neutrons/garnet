"""
Main Qt window
"""

from qtpy.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QTabWidget, QPushButton

from garnet.home.view import HomeView
from garnet.home.model import HomeModel
from garnet.home.presenter import HomePresenter


class MainWindow(QWidget):
    """Main widget"""

    def __init__(self, parent=None):
        super().__init__(parent)

        ### Create tabs here ###

        ### Home tab
        self.tabs = QTabWidget()
        home_view = HomeView(self)
        home_model = HomeModel()
        self.home_presenter = HomePresenter(home_view, home_model)
        self.tabs.addTab(home_view, "Home")
        

        ### Set tab layout
        layout = QVBoxLayout()
        layout.addWidget(self.tabs)

        self.setLayout(layout)

        # register child widgets to make testing easier
        self.home = home_view


