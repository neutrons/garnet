"""BaseStatusBar
-------------

This module defines the BaseStatusBar class, a custom status bar for PyQt applications.
The BaseStatusBar provides functionality for displaying error messages and additional information
through QLabel widgets. It includes methods to update the status label with error messages
and the CWE (Caution, Warnings or Error) label with relevant information.

"""  # noqa D205

from typing import Any, Dict, Optional

from qtpy.QtWidgets import QLabel, QStatusBar, QWidget


class BaseStatusBar(QStatusBar):
    """Custom status bar for displaying error messages and additional information."""

    def __init__(
        self: Any,
        parent: Optional[QWidget] = None,
        **kwargs: dict[str, Any],
    ) -> None:
        """Initialize the BaseStatusBar.

        :param parent: The parent widget. Defaults to None.
        :type parent: QWidget, optional
        :param *args: Additional positional arguments that will be passed to the parent class constructor.
        :param **kwargs: Additional keyword arguments that will be passed to the parent class constructor.

        """
        super().__init__(parent, **kwargs)
        self.error_text: Dict[object, str] = {}
        self.setFixedWidth(600)
        self.cwe_label = QLabel("", self)
        self.status_label = QLabel("", self)
        self.addWidget(self.status_label)
        self.addPermanentWidget(self.cwe_label)

    def update_status_label(self: Any, error_text: Optional[Dict[object, str]] = None) -> bool:
        """Update the status_label with the provided error_text.

        :param error_text:  Dictionary of error messages. Defaults to None.
        :type error_text: Dict[object, str], optional

        :return bool: True if there are any invalid entries, False otherwise.
        """
        if error_text is not None:
            for key in error_text:
                self.error_text[key] = error_text[key]

        self.error_text = {k: v for k, v in self.error_text.items() if v != ""}
        has_invalid = any(self.error_text.values())
        self.status_label.setText("\n".join(self.error_text.values()))
        return has_invalid

    def update_cwe_label(self: Any, text: str) -> None:
        """Update the cwe_label with the provided text.

        :param text: The text to be displayed in the Caution, Warning, Error label.
        :type text: str

        """
        self.cwe_label.setText(text)
