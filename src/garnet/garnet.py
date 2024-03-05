"""Main Qt application"""

import sys
from typing import Any

from mantidqt.gui_helper import set_matplotlib_backend
from qtpy.QtWidgets import QApplication, QMainWindow

# make sure matplotlib is correctly set before we import shiver
set_matplotlib_backend()

# make sure the algorithms have been loaded so they are available to the AlgorithmManager
import mantid.simpleapi  # noqa: F401, E402

from garnet.mainwindow import MainWindow  # noqa: E402
from garnet.version import __version__  # noqa: E402

from mantid.kernel import logger
from garnet.logging.logging import init_logging


import os


init_logging()


class Garnet(QMainWindow):
    """Main GARNET window

    :param QMainWindow: The main window
    :type QMainWindow: QMainWindow
    """

    __instance = None

    def __new__(cls: Any) -> QMainWindow:
        """Singleton pattern for the main window"""
        if Garnet.__instance is None:
            Garnet.__instance = QMainWindow.__new__(cls)
        return Garnet.__instance

    def __init__(self: Any, parent: QMainWindow = None) -> None:
        """Initialize the main window"""
        super().__init__(parent)

        logger.information(f"GARNET version: {__version__}")
        
        self.setWindowTitle(f"GARNET - {__version__}")
        self.main_window = MainWindow(self)
        self.setCentralWidget(self.main_window)


def gui():
    """Open main entry point for Qt application"""
    input_flags = sys.argv[1::]
    if "--v" in input_flags or "--version" in input_flags:
        print(__version__)  # noqa: T201
        sys.exit()
    else:
        app = QApplication(sys.argv)
        window = Garnet()
        window.show()
        sys.exit(app.exec_())
