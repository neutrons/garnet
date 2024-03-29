"""Unit test for the garnet.helpers.ui_elements.base_listwidget.py BaseListWidget."""

from garnet.helpers.ui_elements.base_listwidget import INVALID_QLISTWIDGET, REQUIRED_QLISTWIDGET, BaseListWidget


def test_required_style():
    """Test applying required style."""
    base_list_widget = BaseListWidget(required=True)

    assert base_list_widget.required
    assert base_list_widget.styleSheet() == REQUIRED_QLISTWIDGET


def test_invalid_style():
    """Test applying invalid style."""
    base_list_widget = BaseListWidget(required=True)

    base_list_widget.set_invalid_style()
    assert base_list_widget.styleSheet() == INVALID_QLISTWIDGET


def test_reset_style():
    """Test resetting the style."""
    base_list_widget = BaseListWidget(required=True)

    base_list_widget.set_invalid_style()
    assert base_list_widget.styleSheet() == INVALID_QLISTWIDGET

    base_list_widget.reset_style()
    assert base_list_widget.styleSheet() == REQUIRED_QLISTWIDGET


def test_set_empty_style():
    """Test setting the empty style."""
    base_list_widget = BaseListWidget(required=False)
    assert base_list_widget.styleSheet() == ""
