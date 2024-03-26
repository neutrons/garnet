"""Unit test for the garnet.tabs.home.model.home_presenter.py HomePresenter."""

import unittest
from typing import Any
from unittest.mock import MagicMock

# Import the HomePresenter class to be tested
from garnet.home.model import HomeModel
from garnet.home.presenter import HomePresenter
from garnet.home.view import HomeView


class TestHomePresenter(unittest.TestCase):
    """Test the HomePresenter class."""

    def test_init(self: Any) -> None:
        """Test the HomePresenter constructor."""
        mock_view = MagicMock(spec=HomeView)
        mock_model = MagicMock(spec=HomeModel)

        presenter = HomePresenter(mock_view, mock_model)

        assert presenter._view is mock_view
        assert presenter._model is mock_model

    def test_view_property(self: Any) -> None:
        """Test the view property."""
        mock_view = MagicMock(spec=HomeView)
        mock_model = MagicMock(spec=HomeModel)

        presenter = HomePresenter(mock_view, mock_model)
        assert presenter.view is mock_view

    def test_model_property(self: Any) -> None:
        """Test the model property."""
        mock_view = MagicMock(spec=HomeView)
        mock_model = MagicMock(spec=HomeModel)

        presenter = HomePresenter(mock_view, mock_model)
        assert presenter.model is mock_model
