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

* Variable and function names should be descriptive and follow the ``lower_case_with_underscores`` convention.
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

Updating the Documentation
--------------------------
This project uses `Sphinx <https://www.sphinx-doc.org/en/master/>`_ to generate documentation and is updated with every pull request.
The documentation is a combination of pages written in `reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_ and
docstrings pulled from the code.
A simple guide to updating documentation in Garnet can be found `here <https://github.com/neutrons/garnet/blob/next/docs/README.md>`_.

Building the Documentation
--------------------------
To build the documentation locally, run the following commands from the root of the repository:

.. code-block:: sh

    cd docs
    make clean
    make html

The documentation will be built in the ``docs/_build/html`` directory.
