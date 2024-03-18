"""Unit test for the garnet.helpers.ui_elements.base_checkbox.py BaseCheckBox."""

from garnet.helpers.ui_elements.base_checkbox import INVALID_QCHECKBOX, REQUIRED_QCHECKBOX, BaseCheckBox


def test_required_checkbox_style():
    """Test required checkbox style."""
    checkbox = BaseCheckBox(required=True)

    assert not checkbox.isChecked()
    assert checkbox.required
    assert checkbox.styleSheet() == REQUIRED_QCHECKBOX


def test_invalid_checkbox_style():
    """Test invalid checkbox style."""
    checkbox = BaseCheckBox(required=True)

    checkbox.set_invalid_style()
    assert checkbox.styleSheet() == INVALID_QCHECKBOX
