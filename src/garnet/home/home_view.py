"""PyQt widget for the home tab"""
from qtpy.QtWidgets import QWidget, QHBoxLayout, QErrorMessage, QMessageBox


class Home(QWidget):  # pylint: disable=too-many-public-methods
    """Home widget"""

    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QHBoxLayout()
        self.setLayout(layout)
