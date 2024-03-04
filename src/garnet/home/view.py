"""PyQt widget for the home tab"""
from contextlib import suppress
from typing import Any, Dict, Optional

from garnet.base.base_lineedit import BaseLineEdit
from garnet.base.base_statusbar import BaseStatusBar
from qtpy.QtGui import QDoubleValidator
from qtpy.QtWidgets import QFormLayout, QLabel, QPushButton, QWidget


class HomeView(QWidget):
    """Home widget

    :param QWidget: The main widget
    :type QWidget: QWidget
    """

    def __init__(self: Any, parent: QWidget = None) -> None:
        """Initialize the home widget"""
        super().__init__(parent)

        self.label_welcome = QLabel(self)
        self.label_welcome.setText(
            "Welcome to GARNET\n\nThis is still under active development and currently" "provides no functionality."
        )

        self.plan_name = BaseLineEdit(required=True, parent=self)
        self.wavelength = BaseLineEdit(required=True, default_value=1.486, parent=self)
        self.plan_name.setToolTip(
            "Enter the name of a reduction plan.\n"
            "If the name already exists, the existing plan will be overwritten."
        )
        self.wavelength.setToolTip("Set the wavelength (in Å)")

        self.wavelength_validator = QDoubleValidator(0.0, 1000.0, 7, self)
        self.wavelength_validator.setNotation(QDoubleValidator.StandardNotation)
        self.wavelength.setValidator(self.wavelength_validator)

        self.plan_name.textChanged.connect(self.update_plan_name)
        self.wavelength.textChanged.connect(self.update_wavelength)

        self.save_button = QPushButton("Save Reduction Plan", self)
        self.save_button.setEnabled(False)
        self.save_button.clicked.connect(self.save_reduction_plan)
        self.invalid_fields = [self.plan_name]

        # Create Status Bar
        self.status_bar = BaseStatusBar(self)

        # Create layout
        layout = QFormLayout()
        layout.addRow(self.label_welcome)
        layout.addRow("Reduction Plan Name *", self.plan_name)
        layout.addRow("Wavelength *", self.wavelength)
        layout.addRow(self.save_button)
        layout.addRow(self.status_bar)

        self.setLayout(layout)

    def update_plan_name(self: Any):
        """Update the plan name field.

        If the plan name is empty, set the style to indicate an invalid field with a red border,
        add an error message to the status bar, and disable the save button.
        Otherwise, clear the style, remove the error message from the status bar, and enable the save button.
        """
        plan_name = self.plan_name.text()
        if not plan_name:
            self.plan_name.set_invalid_style()
            error_text = "Reduction Plan Name: Name is required."
            self.invalid_fields.append(self.plan_name)
        else:
            self.plan_name.set_empty_style()
            error_text = ""
            with suppress(ValueError):
                self.invalid_fields.remove(self.plan_name)
        self.update_button_status({self.plan_name: error_text})

    def update_wavelength(self: Any):
        """Update the wavelength field.

        If the input cannot be converted to a float, set the style to indicate an invalid field with a red border,
        add an error message to the status bar, and disable the save button.
        Otherwise, clear the style, remove the error message from the status bar, and enable the save button.
        """
        try:
            float(self.wavelength.text())
            self.wavelength.set_empty_style()
            error_text = ""
        except ValueError:
            self.wavelength.set_invalid_style()
            error_text = "Wavelength: Wavelength is required."

        self.update_button_status({self.wavelength: error_text})

    def update_button_status(self: Any, error_text: Optional[Dict[str, str]] = None):
        """Update the status of the save button based on the presence of invalid fields and error messages.

        :param error_text: Dictionary of error messages for specific fields.
        :type (Optional[Dict[str, str]]):

        The save button will be enabled only if there are no invalid fields and no error messages.
        """
        has_invalid = self.status_bar.update_status_label(error_text)
        button_status = not has_invalid and (len(self.invalid_fields) == 0)
        self.save_button.setEnabled(button_status)

    def save_reduction_plan(self: Any) -> None:
        """Save reduction plan"""
        pass  # noqa
