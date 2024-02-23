# Documentation

## Documenting Code

Every module, class, and method should be documented with a docstring. Below is a few examples of docstrings. Full documentation can be found [here](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html)

### Documenting a module

This docstring should be at the top of the file and give a detailed description of the module and its purpose.

```python
""" Summary of the module
This module is used to do things that people find useful
"""
```

### Documenting a class

Docstring should be located directly under the class definition and should contain information about the functionality, input parameters, returns, and exceptions.

```python
class GarnetClass(object):
    """ This is an example Garnet Class to do Garnet things

    :param some_param: str, some param for doing things
    :param other_param: class:`garnetClass`, some other param
    """

    def __init__(self, some_param: str, other_param: "GarnetClass"):
        """Initializes the GarnetClass"""
        self.some_param = some_param
        self.other_param = other_param
```


### Documenting a method
Similar to a class docstring, this should be directly below the definition and include any useful information for the method. If possible it should also describe algorithms or equations used.

```python
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
```

## Updating Documentation

When adding new views, presenters and methods, please navigate to docs/source/reference.rst. Add the new feature under the appropriate section following the given template:

```bash
.. automodule:: path.to.new.module
   :members:
```

Once complete, rebuild the documentation:
```bash
    cd docs/
    make clean
    make html
```
If you encounter any errors or warnings please fix them when building the docs be sure to fix them.



## Documentation Location

https://garnet.readthedocs.io/en/latest/



## Helpful resources
[sphinx.autodoc](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html) \
[Docstring Example](https://thomas-cokelaer.info/tutorials/sphinx/docstring_python.html) \
[Sphinx Docsting Example](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html) \
[Getting started with Sphinx](https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html) \
[Documenting Code with Sphinx](https://pythonhosted.org/an_example_pypi_project/sphinx.html) \
[Sphinx Documentation](https://www.sphinx-doc.org/en/master/usage/domains/python.html)