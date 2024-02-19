"""PyQt widget for the home tab"""
from qtpy.QtWidgets import QWidget, QHBoxLayout, QLabel


class HomeView(QWidget): 
    """Home widget"""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.label_welcome = QLabel(self)
        self.label_welcome.setText("Welcome to GARNET")
        
        
        layout = QHBoxLayout()
        layout.addWidget(self.label_welcome)

        
        self.setLayout(layout)
