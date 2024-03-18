"""Unit tests for garnet.helpers.ui_elements.base_lineedit.py BaseLineEdit"""

from garnet.helpers.ui_elements.base_lineedit import INVALID_QLINEEDIT, REQUIRED_QLINEEDIT, BaseLineEdit


def test_required_style():
    """Test applying required style."""
    base_line_edit = BaseLineEdit(required=True)

    assert base_line_edit.required
    assert base_line_edit.styleSheet() == REQUIRED_QLINEEDIT


def test_invalid_style():
    """Test applying invalid style."""
    base_line_edit = BaseLineEdit(required=True)

    base_line_edit.set_invalid_style()
    assert base_line_edit.styleSheet() == INVALID_QLINEEDIT


def test_reset_style():
    """Test resetting the style."""
    base_line_edit = BaseLineEdit(required=True)

    base_line_edit.set_invalid_style()
    assert base_line_edit.styleSheet() == INVALID_QLINEEDIT

    base_line_edit.reset_style()
    assert base_line_edit.styleSheet() == REQUIRED_QLINEEDIT
