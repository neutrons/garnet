"""Main Qt application"""

import argparse
import sys
from typing import Any

from mantid.kernel import Logger
from mantidqt.gui_helper import set_matplotlib_backend
from qtpy.QtWidgets import QApplication, QMainWindow

# make sure matplotlib is correctly set before we import shiver
set_matplotlib_backend()

# make sure the algorithms have been loaded so they are available to the AlgorithmManager
import mantid.simpleapi  # noqa: F401, E402

from garnet.helpers.settings import init_debug, update_debug_enabled  # noqa: E402
from garnet.mainwindow import MainWindow  # noqa: E402
from garnet.version import __version__  # noqa: E402

logger = Logger("PACKAGENAME")


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
    parser = argparse.ArgumentParser(prog="GARNET", description="Single Crystal Diffraction")
    parser.add_argument("-v", "--version", action="version", version=__version__)
    parser.add_argument("--debug", action="store_true", help="enable debug logging for GARNET ONLY")
    options, _ = parser.parse_known_args(sys.argv)
    init_debug()
    if options.debug:
        update_debug_enabled(True)

    app = QApplication(sys.argv)
    window = Garnet()
    window.show()
    sys.exit(app.exec_())
