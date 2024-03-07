
.. _MVP_Guidelines:

=====================================
Model-View-Presenter (MVP) Guidelines
=====================================

Overview
========

The Model-View-Presenter (MVP) pattern is a software design pattern
that separates the structure of an application into three main components:
Model, View, and Presenter. This separation enhances modularity, testability,
and maintainability of the codebase.

Components
===========

1. **Model:**
   The Model represents the application's data and algorithm logic. It is
   responsible for retrieving and manipulating data, as well as notifying the
   Presenter of any changes. The Model is independent of both the View and the
   Presenter.

2. **View:**
   The View is responsible for presenting the data to the user and receiving
   user input. It remains passive and delegates user interactions to the Presenter.
   The View does not contain any application logic and is only concerned with
   displaying information to the user. Each View is associated with a single Presenter.

3. **Presenter:**
   The Presenter acts as an intermediary between the Model and the View. It
   contains the application logic, responds to user input from the View, and
   updates the Model accordingly. The Presenter also updates the View in response
   to changes in the Model. This separation allows for easier testing and
   maintenance of the application logic. There is only one Presenter for each View.

Communication Flow
===================

1. User interacts with the View by triggering events.
2. The View forwards user input events to the Presenter.
3. The Presenter processes the events, updates the Model as needed, and
   communicates changes back to the View.
4. The View reflects the changes made by the Presenter.

.. mermaid::

    graph LR
    User((User))
    View(View)
    Presenter(Presenter)
    Model(Model)

    User -->|User Interaction| View
    View -->|User Input Events| Presenter
    Presenter -->|Update Model| Model
    Model -->|Notify Changes| Presenter
    Presenter -->|Update View| View
    View -->|View Updates| User


|

Guidelines
===========

Model
`````

1. The Model should be independent of the View and the Presenter.
2. The Model should contain the application's data and algorithm logic.
3. The Model should be reusable and not tied to a specific View or Presenter.
4. Absolutely no UI logic should be present in the Model.

View
````
1. The View should be passive and not contain any application logic.
2. The View should delegate user interactions to the Presenter.
3. The View should be responsible for displaying data to the user and receiving user input.
4. The View should not contain any logic or data manipulation other than :ref:`field validation <field_validation>` and event triggering.
5. The View should never directly access the Model.
6. The View should **Never** contain a mantid workspace.

Presenter
`````````
1. The Presenter should act as an intermediary between the Model and the View.
2. The Presenter should contain the application logic and respond to user input from the View.
3. The Presenter should update the Model and the View as needed.
4. The Presenter should never directly access the View or the Model.
5. The Presenter should **Never** contain Qt or other UI elements.

Advantages
==========

1. **Separation of Responsibility:**
   MVP separates the application into distinct components, promoting a clean and
   modular code structure. This separation makes it easier to manage and test each
   component independently.

2. **Testability:**
   Since the application logic resides in the Presenter and Algorithms in the Model,
   it is easier to unit test without involving the UI components. This facilitates
   a more effective testing strategy.

3. **Maintainability:**
   The clear separation of responsibilities makes the codebase more maintainable.
   Changes in one component, such as the View or Model, do not directly impact the
   others.

===========
MVP Example
===========

The following is a simple example demonstrating the MVP pattern in Garnet.

.. code-block:: python

   import sys
   from qtpy.QtWidgets import (
      QApplication,
      QMainWindow,
      QWidget,
      QVBoxLayout,
      QPushButton,
      QLabel,
      QLineEdit,
   )


   # Model
   class CalculatorModel:
      def square_and_sum(self, a, b):
         return int(a)**2 + int(b)**2

      def square_root(self, num):
         return num ** 0.5

   # View
   class CalculatorView(QWidget):
      def __init__(self):
         super().__init__()

         self.input_a_label = QLabel("Side A:")
         self.input_a_edit = QLineEdit()

         self.input_b_label = QLabel("Side B:")
         self.input_b_edit = QLineEdit()

         self.result_label = QLabel("Side C:")

         self.calculate_button = QPushButton("Calculate")
         self.calculate_button.clicked.connect(self.apply_calculate)

         layout = QVBoxLayout()
         layout.addWidget(self.input_a_label)
         layout.addWidget(self.input_a_edit)
         layout.addWidget(self.input_b_label)
         layout.addWidget(self.input_b_edit)
         layout.addWidget(self.calculate_button)
         layout.addWidget(self.result_label)

         self.setLayout(layout)

         self.apply_calculate_callback = None

      def connect_apply_calculate(self, func):
         self.apply_calculate_callback = func

      def apply_calculate(self):
         params = {'a': self.input_a_edit.text(), 'b': self.input_b_edit.text()}
         self.apply_calculate_callback(params)

      def set_result(self, result):
         self.result_label.setText(f"Result: {result}")

   # Presenter
   class CalculatorPresenter:
      def __init__(self, model, view):
         self.model = model
         self.view = view

         self.view.connect_apply_calculate(self.calculate)

      def calculate(self, params):
         ab_square = self.model.square_and_sum(params['a'], params['b'])
         self.view.set_result(self.model.square_root(ab_square))


   # Main Application
   class CalculatorApp(QMainWindow):
      def __init__(self):
         super().__init__()

         self.model = CalculatorModel()
         self.view = CalculatorView()
         self.presenter = CalculatorPresenter(self.model, self.view)

         self.setCentralWidget(self.view)
         self.setWindowTitle("Pythagorean Theorem Calculator")


   if __name__ == "__main__":
      app = QApplication(sys.argv)
      calculator_app = CalculatorApp()
      calculator_app.show()
      sys.exit(app.exec_())
