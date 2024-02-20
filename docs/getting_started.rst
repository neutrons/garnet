Getting Started
===============

.. _getting_started:



Instructions for GARNET development
-----------------------------------

Conda Configuration
```````````````````
Create and activate conda environment for ``GARNET``.

.. code-block:: sh

    conda env create --file environment.yml
    # or
    mamba env create --file environment.yml

    conda activate garnet

Install ``GARNET`` (in `editable mode <https://pip.pypa.io/en/stable/cli/pip_install/#cmdoption-e>`_) and start application

.. code-block:: sh

    python -m pip install -e .

    garnet

If it has been a while, once can update using

.. code-block:: sh

    conda activate garnet
    conda env update --file environment.yml --prune


Testing
```````````````````
The project contains testing infrastructure in the tests/ folder:
- data/ : It contains the test data. Small data files can be included in this directory. Forl large data files, there is a subfolder garner-data 
 that is connected to a gitlfs data repo in gitlab as a submodule: https://code.ornl.gov/sns-hfir-scse/infrastructure/test-data/garnet-data
- tabs/ : Tests are organized into folders for every page:
    * home/
    * order_param/
    * peak_integr/
    * recp_space/
    * ub_peak_find/

    In every page-tab directory the tests are furtherd arranged in MVP-based filesystem structure:
    * models/
    * views/
    * presenter/
- utility/ : It contains tests for code elements that are shared among pages and belong to the corresponding file folder (utility/).
- workflows/ : It contains tests with code that spans among pages to test full reduction workflows.


How to setup garnet-data repository locally
Open a terminal and go to garnet repository root folder. Run:

- git submodule add https://code.ornl.gov/sns-hfir-scse/infrastructure/test-data/garnet-data tests/data/garnet-data

To update the changes for the data-repo. Run:
- git submodule update --init --recursive

No need to commit changes in this reposotiry. If a message appears to stage the garnet-data repository in this one, just run the above command.

Notes. 

Tests that use the garnet-data repository, will need to be configured additionally for github runners. 

Additionally, the marker `datarepo` is used to skip tests that required garnet-repo to be present (`if not has_datarepo`), in case garnet-repo has not been configured.

