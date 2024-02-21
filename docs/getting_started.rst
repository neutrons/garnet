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
    * data/ : It contains the test data. Small data files can be included in this directory. Forl large data files, there is a subfolder garner-data that is connected to a gitlfs data repo in gitlab as a submodule: https://code.ornl.gov/sns-hfir-scse/infrastructure/test-data/garnet-data
    * tabs/ : Tests are organized into folders for every page:
        * home/
        * order_param/
        * peak_integr/
        * recp_space/
        * ub_peak_find/

        In every page-tab directory the tests are furtherd arranged in MVP-based filesystem structure:
            * models/
            * views/
            * presenter/

    * utility/ : It contains tests for code elements that are shared among pages and belong to the corresponding file folder (utility/).
    * workflows/ : It contains tests with code that span among pages to test full reduction workflows.


How to setup the garnet-data repository locally
```````````````````

Open a terminal and go to garnet repository root folder. Run:

.. code-block:: sh

    git submodule add https://code.ornl.gov/sns-hfir-scse/infrastructure/test-data/garnet-data tests/data/garnet-data

To update the changes for the data-repo. Run:

.. code-block:: sh

     git submodule update --init --recursive

No need to commit changes in this repository. If a message appears to stage the garnet-data repository in this one, just run the above command.

More information on git-lfs can be found here:

.. code-block:: sh

    https://ornl-neutrons.atlassian.net/wiki/spaces/NDPD/pages/19103745/Using+git-lfs+for+test+data


Tests that use the garnet-data repository, will need to be configured for github runners (TBD).

Additionally, the marker `datarepo` is used to skip tests that require garnet-repo to be present (`if not has_datarepo`).

Instructions for CIS Testing - PRs:

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

in case there is specific Mantid build and /or version in another conda environment, garnet can be installed in that environment:

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
