import pytest
import os


@pytest.fixture(scope="session")
def has_datarepo():
    """Fixture that returns True if the datarepo_dir is available"""
    root_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "garnet-data")
    return os.path.exists(root_data)


@pytest.fixture(scope="session")
def datarepo_dir():
    """A namedtuple with the directory **absolute** paths for test data."""
    root_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "garnet-data")
    return root_data
