"""PyQt widget for the home tab"""
from qtpy.QtWidgets import QWidget, QHBoxLayout, QErrorMessage, QMessageBox, QLabel


class Home(QWidget): 
    """Home widget"""

    def __init__(self, parent=None):
        super().__init__(parent)

        label_welcome = QLabel(self)
        label_welcome.setText("Welcome to GARNET")
        
        
        layout = QHBoxLayout()
        layout.addWidget(label_welcome)

        
        self.setLayout(layout)
