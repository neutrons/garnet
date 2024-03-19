"""BaseListWidget
-----------------

This module defines the BaseListWidget class, a customized QListWidget with setup and helper functions for
QListWidgets used in Garnet.
"""  # noqa D205

from typing import Any, Optional

from qtpy.QtWidgets import QListWidget

INVALID_QLISTWIDGET = """
QListWidget {
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

REQUIRED_QLISTWIDGET = """
QListWidget {
    background-color: lightyellow;
}
"""


class BaseListWidget(QListWidget):
    """BaseListWidget that inherits the QListWidget.

    This class includes setup and helper functions for QListWidgets used in Garnet.

    :param required: Indicate whether the field is required. Defaults to False.
    :type required: bool, optional
    :param parent: The parent object that holds the QListWidget. Defaults to None.
    :type parent: Any, optional
    :param args: Additional positional arguments that will be passed to the parent class constructor.
    :param kwargs: Additional keyword arguments that will be passed to the parent class constructor.

    When creating a BaseListWidget, also pay attention to the selection mode.
    The selection mode will change the behavior of the list widget when selecting items.
    The selection mode can be set using the setSelectionMode method.

        :param mode: Selection mode to be set.
                     0: NoSelection
                     1: SingleSelection
                     2: MultiSelection
                     3: ExtendedSelection
                     4: ContiguousSelection
        :type mode: int

        more info about the selection mode can be found in the
        `Qt documentation <https://doc.qt.io/archives/qt-4.8/qabstractitemview.html#SelectionMode-enum>`_

    """

    def __init__(
        self: Any,
        *args: tuple[Any],
        required: Optional[bool] = False,
        **kwargs: dict[str, Any],
    ) -> None:
        """Initialize the BaseListWidget."""
        super().__init__(*args, **kwargs)
        self.required = required
        self.reset_style()

    def set_invalid_style(self: Any) -> None:
        """Set field style as invalid.

        If a validator determines the field is invalid, this function will be called
        and the field will be marked with a red border.
        """
        self.setStyleSheet(INVALID_QLISTWIDGET)

    def set_required_style(self: Any) -> None:
        """If a field is required, the background will be set to light-yellow."""
        self.setStyleSheet(REQUIRED_QLISTWIDGET)

    def set_empty_style(self: Any) -> None:
        """Once the field has been validated, the style will be cleared."""
        self.setStyleSheet("")

    def reset_style(self: Any) -> None:
        """Reset the style to its default."""
        if self.required:
            self.set_required_style()
        else:
            self.set_empty_style()
