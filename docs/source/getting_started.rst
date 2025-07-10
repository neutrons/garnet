===============
Getting Started
===============

.. _getting_started:


Instructions for GARNET installation and setup.
-----------------------------------------------

Create and activate pixi environment for ``GARNET``:

.. code-block:: sh

    cd /.../garnet
    pixi install
    pixi shell

This also installs ``garnet`` in editable mode with pip, so it can be run immediately:

.. code-block:: sh

    garnet

If it has been a while and there have been changes to garnet's ``pyproject.toml``,
the environment can be updated by pulling the latest changes and simply reinstalling:

.. code-block:: sh

    git pull
    pixi install


Setup the garnet-data submodule
```````````````````````````````

Open a terminal and go to garnet repository root folder. Run:

.. code-block:: sh

     git submodule update --init --recursive
     git submodule update --remote

This will clone the garnet-data repository in the garnet repository root folder. If for some reason the `.gitmodule` file is not present, you can add the submodule manually:

.. code-block:: sh

    git submodule add https://code.ornl.gov/sns-hfir-scse/infrastructure/test-data/garnet-data tests/data/garnet-data

To update to the latest commit for the data-repo. Run:

.. code-block:: sh

     git submodule update --remote

If the hash for the garnet-data repository has changed and you want to update the hash in the garnet repository, run:

.. code-block:: sh

        git add tests/data/garnet-data
        git commit -m "Update garnet-data to latest commit"
        git push

More information on git-lfs can be found in the Neutrons Confluence `Git-lfs page <https://ornl-neutrons.atlassian.net/wiki/spaces/NDPD/pages/19103745/Using+git-lfs+for+test+data>`_.


Checkout out our guide for :ref:`developers <dev_guidelines>` to learn more
about :ref:`coding standards <coding_standards>` and :ref:`testing <testing>`.
