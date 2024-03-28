.. _testing:

=======
Testing
=======

The project contains testing infrastructure in the tests/ folder:
    * data/ : It contains the test data. Small data files can be included in this
      directory. For large data files, there is a subfolder garner-data that is connected to a gitlfs data
      repo in gitlab as a submodule: https://code.ornl.gov/sns-hfir-scse/infrastructure/test-data/garnet-data
    * tabs/ : Tests are organized into folders for every page:

        * home/
        * order_param/
        * peak_integr/
        * recp_space/
        * ub_peak_find\/

        In every page-tab directory the tests are furtherd arranged in MVP-based filesystem structure:

            * models/
            * views/
            * presenter/

    * utility/ : It contains tests for code elements that are shared among pages and belong to the corresponding file folder (utility/).
    * workflows/ : It contains tests with code that span among pages to test full reduction workflows.

Writing Tests
`````````````
We strongly encourage adopting a Test-Driven Development (TDD) approach throughout the development process. By writing tests before implementing
features, we promote code reliability, maintainability, and faster debugging. Embrace TDD as a best practice to enhance the overall quality of our project.
The general approach is to write tests for every function and method in the code. The tests should cover all possible input combinations and edge cases.

The tests are implemented using the `pytest <https://docs.pytest.org/>`_ framework to enable automated testing. These tests aim to achieve an overall test
coverage of 90% of the entire codebase. Test files follow the naming convention test\_\*.py and are organized within the relevant directory of the code they
validate. Additionally, the project Continuous Integration (CI) process has configured `Codecov <https://docs.codecov.com/>`_ to run for every pull request (PR) to enforce the target
test coverage. If the overall coverage is less than 90% or the coverage drops more than the configured 2% in a single PR it will cause the CI check to fail.
The target and the threshold are both configured in the ``.codecov.yml`` file.

To check test coverage locally you can run the following command:

.. code-block:: sh

    python -m pytest --cov=src --cov-report=term-missing

Tests that use the garnet-data submodule, will need to be configured for github runners (TBD).
Additionally, the `pytest marker <https://docs.pytest.org/en/8.0.x/reference/reference.html#custom-marks>`_ ``datarepo`` is used to skip tests that require
garnet-data submodule to be present.

Running Tests
`````````````
The tests can be run using the `pytest <https://docs.pytest.org/>`_ framework. The tests can be run in the garnet conda environment.
The following instructions assume that the current working directory is the root of the garnet repository and that the garnet conda environment is activated.

To run all tests:

.. code-block:: sh

    python -m pytest

To run a specific test:

.. code-block:: sh

    python -m pytest path/to/test_file.py

To run a specific test function:

.. code-block:: sh

    python -m pytest path/to/test_file.py::test_function

To run tests that require the garnet-data submodule:

.. code-block:: sh

    python -m pytest -m datarepo


=====================
Testing a specific PR
=====================

Checkout to the PR by following the Pull-Request instructions:

.. code-block:: sh

    conda activate <garnet_environment>
    cd /path/to/my/local/garnet/repo/
    git fetch origin pull/<PULL_REQUEST_NUMBER>/head:pr<PULL_REQUEST_NUMBER>
    git switch pr<PULL_REQUEST_NUMBER>
    #run tests
    python -m pytest <item_to_test>
    #and/or start garnet
    garnet

To test a specific Mantid build and/or version in another conda environment, garnet can be installed in that environment:

.. code-block:: sh

    conda activate <mantid_environment>
    #in case of a mantid build, else skip
    ./bin/AddPythonPath.py
    cd /path/to/my/local/garnet/repo/
    git fetch origin pull/<PULL_REQUEST_NUMBER>/head:pr<PULL_REQUEST_NUMBER>
    git switch pr<PULL_REQUEST_NUMBER>
    python -m pip install -e .
    #run tests
    python -m pytest <item_to_test>
    #and/or start garnet
    garnet
