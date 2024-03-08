.. _coding_standards:

============
Contributing
============

We welcome contributions to the project. Please read the following guidelines before
submitting a pull request.

All contributors agree to the following:
- You have permission and any required rights to submit your contribution.
- Your contribution is provided under the license of this project and may be redistributed as such.
- All contributions to this project are public.

All contributions must be
`"signed off" in the commit <https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---signoff>`_
log and by doing so you agree to the above.

Getting access to the main project
----------------------------------

Direct commit access to the project is currently restricted to core developers.
All other contributions should be done through pull requests using the standard github mechanisms.

=============
Pull Requests
=============

* All pull requests should be made against the ``next`` branch.
* All changes made require associated tests and should follow :ref:`testing guidelines <testing>`.
* Developers should run the pre-commit hooks locally *before* submitting a pull request.
* Pull requests do not currently run the tests that require the garnet-data submodule. Developers should run these tests locally *before* submitting a pull request.
* If applicable, the pull request should include updates to the :ref:`documentation <documentation>`.
* All pull requests should include any information required to test the changes. This may include:

  * A description of the changes
  * A description of how to test the changes
  * Any relevant data or scripts required to test the changes

A simple example of this workflow would be as follows:

.. code-block:: sh

    git checkout -b my_new_feature
    # Write Tests for your new feature
    python -m pytest # New tests should fail
    # Write code to make the tests pass
    python -m pytest # All tests should pass
    # update the documentation (if applicable)
    git add <files>
    git commit -m "My new feature" # pre-commit will run here
    git push -u origin my_new_feature

Then, go to the `github page <https://github.com/neutrons/garnet/>`_ for the repository and create a new pull request from the ``my_new_feature`` branch to the ``next`` branch.

================
Coding Standards
================

A few notes on coding standards:

* Variable and function names should be descriptive and follow the ``lower_case_with_underscores`` convention (commonly referred to as ``snake_case``).
* Filenames should be lowercase and use underscores to separate words.
* All code will be checked and formatted using `ruff <https://docs.astral.sh/ruff/rules/>`_.
* Docstrings should be used to document all functions, classes, and Modules.
* Pre-commit hooks are configured to run for every PR, and can be run locally on every commit.

Pre-commit
----------

Pre-commit is a tool that is used to ensure that all code is formatted and linted before being committed.

Install pre-commit
++++++++++++++++++

pre-commit can be installed using the following command:

.. code-block:: sh

    pre-commit install

You should only need to do this once. pre-commit will now run on every commit.

Run pre-commit manually
+++++++++++++++++++++++

The following command will run pre-commit on all staged changes:

.. code-block:: sh

    pre-commit

To run pre-commit on all files in the repository, run the following command:

.. code-block:: sh

    pre-commit run --all

More information on pre-commit can be found in the `pre-commit documentation <https://pre-commit.com/>`_.


========================
Documentation Guidelines
========================

.. _documentation:

This project uses `Sphinx <https://www.sphinx-doc.org/en/master/>`_ to generate documentation and is updated with every pull request.
The documentation is a combination of pages written in `reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_ and
docstrings pulled from the code.

Documenting Code
----------------
Every module, class, and method should be documented with a docstring. Below is a few examples of docstrings.
Full documentation can be found in the `sphinx documentation here <https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html>`_.

Documenting a module
++++++++++++++++++++

This docstring should be at the top of the file and give a detailed description of the module and its purpose.

.. code-block:: python

    """ Summary of the module
    This module is used to do things that people find useful
    """

Documenting a class
+++++++++++++++++++

Docstring should be located directly under the class definition and should contain information about the functionality, input parameters, returns, and exceptions.

.. code-block:: python

    class GarnetClass(object):
        """ This is an example Garnet Class to do Garnet things

        :param some_param: str, some param for doing things
        :param other_param: class:`garnetClass`, some other param
        """

        def __init__(self, some_param: str, other_param: "GarnetClass"):
            """Initializes the GarnetClass"""
            self.some_param = some_param
            self.other_param = other_param


Documenting a function
++++++++++++++++++++++

Similar to a class docstring, this should be directly below the definition and include any useful information for the method. If possible it should also describe algorithms or equations used.

.. code-block:: python

    def garnet_method(self, input_a: float, input_b: float):
        """Returns a the result of some useful equation on the inputs a and b

        :param input_a: float, first input
        :param input_b: float, second input

        Uses the equation:

        .. math::
            \sum_{input\_a=1}^{\\infty} x_{input\_b}

        :return: result of equation
        :rtype: float
        """


Updating the Documentation
--------------------------

When adding new views, presenters and methods, please navigate to docs/source/reference.rst. Add the new feature under the appropriate section following the given template:

.. sourcecode:: RST

    .. automodule:: path.to.module
        :members:

Adding New Documents
--------------------
Documents are `reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_ documents located in ``docs/source/``. If you create a
new documentation file, you must also add it to the ``index.rst`` toctree or it will not be included in the build.

.. note::

    If you are creating a new pages or sections, please update the toctree in the appropriate index files. This will ensure that the new pages are included in the documentation build.

Adding Diagrams
---------------
Design or workflow diagrams can be added to your documents with the use of [mermaid](https://mermaid.js.org/intro/). Below is a basic example of including a diagram in a reStructuredText document:

.. code-block:: bash

    .. mermaid::

        graph TD;
        A-->B;
        A-->C;
        B-->D;
        C-->D;

This will render the following diagram in the documentation:

.. mermaid::

    graph TD;
        A-->B;
        A-->C;
        B-->D;
        C-->D;


Building the Documentation
--------------------------
To build the documentation locally, run the following commands from the root of the repository:
If you encounter any errors or warnings please fix them when building the docs be sure to fix them.

.. code-block:: sh

    cd docs
    make clean
    make html

The documentation will be built in the ``docs/_build/html`` directory.

Helpful Links
-------------
| `Sphinx Documentation <https://www.sphinx-doc.org/en/master/usage/domains/python.html>`_
| `Sphinx Docsting Example <https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html>`_
| `Getting started with Sphinx <https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html>`_
| `Documenting Code with Sphinx <https://pythonhosted.org/an_example_pypi_project/sphinx.html>`_
| `Docstring Example <https://thomas-cokelaer.info/tutorials/sphinx/docstring_python.html>`_
| `Sphinx.autodoc <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_
| `reStructuredText Primer <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_
| `Mermaid <https://mermaid.js.org/intro/>`_
