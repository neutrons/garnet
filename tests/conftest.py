"""pytest config"""
import os

import pytest


@pytest.fixture(scope="session")
def has_datarepo():
    """Fixture that returns True if the datarepo_dir is available"""
    readme_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "garnet-data", "README.md")
    return os.path.exists(readme_data)


@pytest.fixture(scope="session")
def datarepo_dir():
    """Named tuple with the directory **absolute** paths for test data."""
    root_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "garnet-data")
    return root_data
