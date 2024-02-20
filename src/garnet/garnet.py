"""
Main Qt application
"""

import sys
from qtpy.QtWidgets import QApplication, QMainWindow

from mantid.kernel import Logger
from mantidqt.gui_helper import set_matplotlib_backend

# make sure matplotlib is correctly set before we import shiver
set_matplotlib_backend()

# make sure the algorithms have been loaded so they are available to the AlgorithmManager
import mantid.simpleapi  # noqa: F401, E402 pylint: disable=unused-import, wrong-import-position

from garnet.version import __version__  # noqa: E402 pylint: disable=wrong-import-position
from garnet.mainwindow import MainWindow  # noqa: E402 pylint: disable=wrong-import-position

logger = Logger("PACKAGENAME")


class Garnet(QMainWindow):
    """Main GARNET window"""

    __instance = None

    def __new__(cls):
        if Garnet.__instance is None:
            Garnet.__instance = QMainWindow.__new__(cls)  # pylint: disable=no-value-for-parameter
        return Garnet.__instance

    def __init__(self, parent=None):
        super().__init__(parent)
        logger.information(f"GARNET version: {__version__}")

        self.setWindowTitle(f"GARNET - {__version__}")
        self.main_window = MainWindow(self)
        self.setCentralWidget(self.main_window)


def gui():
    """
    Main entry point for Qt application
    """
    input_flags = sys.argv[1::]
    if "--v" in input_flags or "--version" in input_flags:
        print(__version__)
        sys.exit()
    else:
        app = QApplication(sys.argv)
        window = Garnet()
        window.show()
        sys.exit(app.exec_())
