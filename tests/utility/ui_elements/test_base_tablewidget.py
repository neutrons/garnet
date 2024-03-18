"""Unit test for the garnet.helpers.ui_elements.base_tablewidget.py BaseTableWidget."""

from garnet.helpers.ui_elements.base_tablewidget import INVALID_QTABLEWIDGET, REQUIRED_QTABLEWIDGET, BaseTableWidget


def test_required_style():
    """Test applying required style."""
    base_table_widget = BaseTableWidget(required=True)

    assert base_table_widget.required
    assert base_table_widget.styleSheet() == REQUIRED_QTABLEWIDGET


def test_invalid_style():
    """Test applying invalid style."""
    base_table_widget = BaseTableWidget(required=True)

    base_table_widget.set_invalid_style()
    assert base_table_widget.styleSheet() == INVALID_QTABLEWIDGET


def test_set_empty_style():
    """Test setting the empty style."""
    base_table_widget = BaseTableWidget(required=False)
    assert base_table_widget.styleSheet() == ""


def test_with_args():
    """Test setting the read only style."""
    num_rows = 12
    num_columns = 3
    base_table_widget = BaseTableWidget(num_rows, num_columns, required=True)

    assert base_table_widget.rowCount() == num_rows
    assert base_table_widget.columnCount() == num_columns
