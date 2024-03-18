Base UI Elements Usage Guide
============================

Introduction
------------

This document provides an overview of the base UI elements available in the Garnet framework
and how to use them effectively in your views. These base classes provide customized widgets
with added functionality for common UI elements. These classes are designed to be used as
base classes for your custom UI elements, allowing you to easily add validation and styling
consistant with the rest of the application.

Required Fields
---------------

The base UI elements provide a `required` parameter that can be set to `True` or `False`.
When set to `True`, the field will be marked as required and will be styled differently.
The `required` parameter is set to `False` by default. It is up to the developer to determine if
a field is required or not. If a field is required it should also be validated before the form is submitted.

Invalid Fields
--------------
The base UI elements provide a `set_invalid_style()` method that can be used to mark the field as invalid.
This method will change the style of the field to indicate that it is invalid. The `reset_style()` method
can be used to reset the style to its default. If a field is invalid it should also be validated before the
form is submitted. Invalid fields should also include a message to the user explaining why the field is invalid.

BaseLineEdit
------------

The `BaseLineEdit` class provides a customized `QLineEdit <https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QLineEdit.html>`_.

Usage:

1. Import the `BaseLineEdit` class:

   .. code-block:: python

      from garnet.helpers.ui_elements.base_lineedit import BaseLineEdit

2. Create an instance of `BaseLineEdit`:

   .. code-block:: python

      base_line_edit = BaseLineEdit(required=True)

3. Use the `set_invalid_style()` method to mark the field as invalid:

   .. code-block:: python

      base_line_edit.set_invalid_style()

4. Use the `reset_style()` method to reset the style to its default:

   .. code-block:: python

      base_line_edit.reset_style()


BaseListWidget
--------------

The `BaseListWidget` class provides a customized `QListWidget <https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QListWidget.html>`_.

Usage:

1. Import the `BaseListWidget` class:

   .. code-block:: python

      from garnet.helpers.ui_elements.base_listwidget import BaseListWidget

2. Create an instance of `BaseListWidget`:

   .. code-block:: python

      base_list_widget = BaseListWidget(required=True)

3. Use the `set_invalid_style()` method to mark the list widget as invalid:

   .. code-block:: python

      base_list_widget.set_invalid_style()

4. Use the `set_selection_mode()` method to set the selection mode:

   .. code-block:: python

      base_list_widget.set_selection_mode(BaseListWidget.MultiSelection)


BaseTableWidget
---------------

The `BaseTableWidget` class provides a customized `QTableWidget <https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QTableWidget.html>`_.

Usage:

1. Import the `BaseTableWidget` class:

   .. code-block:: python

      from garnet.helpers.ui_elements.base_tablewidget import BaseTableWidget

2. Create an instance of `BaseTableWidget`:

   .. code-block:: python

      base_table_widget = BaseTableWidget(required=True)

3. Use the `set_invalid_style()` method to mark the table widget as invalid:

   .. code-block:: python

      base_table_widget.set_invalid_style()

4. Use the `setColumnCount()` and `setRowCount()` methods to define the table dimensions:

   .. code-block:: python

      base_table_widget.setColumnCount(3)
      base_table_widget.setRowCount(3)


BaseCheckBox
------------

The `BaseCheckBox` class provides a customized `QCheckBox <https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QCheckBox.html>`_.
Usage:

1. Import the `BaseCheckBox` class:

   .. code-block:: python

      from garnet.helpers.ui_elements.base_checkbox import BaseCheckBox

2. Create an instance of `BaseCheckBox`:

   .. code-block:: python

      base_checkbox = BaseCheckBox(required=True)

3. Use the `set_invalid_style()` method to mark the checkbox as invalid:

   .. code-block:: python

      base_checkbox.set_invalid_style()
