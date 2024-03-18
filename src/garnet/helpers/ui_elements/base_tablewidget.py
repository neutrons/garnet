"""BaseTableWidget
-----------------

This module defines the BaseTableWidget class, a customized QTableWidget with setup and helper functions for
QTableWidgets used in Garnet.
"""  # noqa D205

from typing import Any, Optional

from qtpy.QtWidgets import QTableWidget, QWidget

INVALID_QTABLEWIDGET = """
QTableWidget {
    border-color: red;
    border-style: outset;
    border-width: 2px;
    border-radius: 4px;
    padding-left: -1px;
    padding-right: -1px;
    padding-top: 1px;
    padding-bottom: 1px;
}
"""

REQUIRED_QTABLEWIDGET = """
QTableWidget {
    background-color: lightyellow;
}
"""


class BaseTableWidget(QTableWidget):
    """BaseTableWidget that inherits the QTableWidget.

    This class includes setup and helper functions for QTableWidgets used in Garnet.

    :param required: Indicate whether the field is required. Defaults to False.
    :type required: bool, optional
    :param parent: The parent object that holds the QTableWidget. Defaults to None.
    :type parent: Any, optional
    :param args: Additional positional arguments that will be passed to the parent class constructor.
    :param kwargs: Additional keyword arguments that will be passed to the parent class constructor.

    """

    def __init__(
        self: Any,
        *args: tuple[Any],
        required: Optional[bool] = False,
        parent: Optional[QWidget] = None,
        **kwargs: dict[str, Any],
    ) -> None:
        """Initialize the BaseTableWidget."""
        super().__init__(*args, parent=parent, **kwargs)
        self.required = required
        self.reset_style()

    def set_invalid_style(self: Any) -> None:
        """Set field style as invalid.

        If a validator determines the field is invalid, this function will be called
        and the field will be marked with a red border.
        """
        self.setStyleSheet(INVALID_QTABLEWIDGET)

    def set_required_style(self: Any) -> None:
        """If a field is required, the background will be set to light-yellow."""
        self.setStyleSheet(REQUIRED_QTABLEWIDGET)

    def set_empty_style(self: Any) -> None:
        """Once the field has been validated, the style will be cleared."""
        self.setStyleSheet("")

    def reset_style(self: Any) -> None:
        """Reset the style to its default."""
        if self.required:
            self.set_required_style()
        else:
            self.set_empty_style()
