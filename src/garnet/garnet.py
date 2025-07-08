"""Main Qt application"""

import sys

# make sure the algorithms have been loaded so they are available to the AlgorithmManager
import mantid.simpleapi  # noqa: F401, E402
from mantid.kernel import Logger
from qtpy.QtWidgets import QApplication

from garnet import __version__  # noqa: E402
from garnet.mainwindow import MainWindow  # noqa: E402

logger = Logger("GARNET")


def gui():
    """Open main entry point for Qt application"""
    input_flags = sys.argv[1::]
    if "--v" in input_flags or "--version" in input_flags:
        print(__version__)  # noqa: T201
        sys.exit()
    else:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    gui()
