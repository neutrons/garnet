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


Contributing
````````````
pre-commit can be installed using the following command:

.. code-block:: sh

    pre-commit install

You should only need to do this once. pre-commit will now run on every commit.

If you want to run it manually, you can run the following command to run pre-commit on all staged changes:

.. code-block:: sh

    pre-commit

To run pre-commit on all files in the repository, run the following command:

.. code-block:: sh

    pre-commit run --all
