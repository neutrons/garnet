"""BaseLineEdit
------------

This module defines the BaseLineEdit class, a customized QLineEdit with setup and helper functions for
QLineEdits used in Garnet.
"""  # noqa D205

from typing import Any, Optional

from qtpy.QtWidgets import QLineEdit

INVALID_QLINEEDIT = """
QLineEdit {
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

REQUIRED_QLINEEDIT = """
QLineEdit {
    background-color: lightyellow;
}
"""


class BaseLineEdit(QLineEdit):
    """BaseLineEdit that inherits the QLineEdit.

    This class includes setup and helper functions for QLineEdits used in Garnet.

    :param required: Indicate whether the field is required. Defaults to False.
    :type required: bool, optional
    :param default_value: Set the default value for the field. Defaults to None.
    :type default_value: Any, optional
    :param parent: The parent object that holds the QLineEdit. Defaults to None.
    :type parent: Any, optional
    :param args: Additional positional arguments that will be passed to the parent class constructor.
    :param kwargs: Additional keyword arguments that will be passed to the parent class constructor.

    """

    def __init__(
        self: Any,
        *args: tuple[Any],
        required: Optional[bool] = False,
        default_value: Optional[Any] = None,  # noqa ANN401
        **kwargs: dict[str, Any],
    ) -> None:
        """Initialize the BaseLineEdit."""
        super().__init__(*args, **kwargs)
        self.required = required
        self.default_value = default_value
        if default_value is not None:
            self.setText(str(default_value))
        self.reset_style()

    def set_invalid_style(self: Any) -> None:
        """Set field style as invalid

        If a validator determines the field is invalid, this function will be called
        and the field will be marked with a red border.
        """
        self.setStyleSheet(INVALID_QLINEEDIT)

    def set_required_style(self: Any) -> None:
        """If a field is required, the background will be set to light-yellow."""
        self.setStyleSheet(REQUIRED_QLINEEDIT)

    def set_empty_style(self: Any) -> None:
        """Once the field has been validated, the style will be cleared."""
        self.setStyleSheet("")

    def reset_style(self: Any) -> None:
        """Reset the style to its default."""
        if self.required and self.default_value is None:
            self.set_required_style()
        else:
            self.set_empty_style()
