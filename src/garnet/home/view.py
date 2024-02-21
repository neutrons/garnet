"""PyQt widget for the home tab"""
from typing import Any

from qtpy.QtWidgets import QHBoxLayout, QLabel, QWidget


class HomeView(QWidget):
    """Home widget"""

    def __init__(self: Any, parent: QWidget = None) -> None:
        """Initialize the home widget"""
        super().__init__(parent)

        self.label_welcome = QLabel(self)
        self.label_welcome.setText("Welcome to GARNET")

        layout = QHBoxLayout()
        layout.addWidget(self.label_welcome)

        self.setLayout(layout)
