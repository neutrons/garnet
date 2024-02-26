"""Presenter for the Home tab"""
from typing import Any

from garnet.home.model import HomeModel
from garnet.home.view import HomeView


class HomePresenter:
    """Home presenter

    :param view: The view for this presenter
    :type view: HomeView
    :param model: The model for this presenter
    :type model: HomeModel
    """

    def __init__(self: Any, view: HomeView, model: HomeModel) -> None:
        """Initialize the home presenter"""
        self._view = view
        self._model = model

    @property
    def view(self: Any) -> HomeView:
        """Return the view for this presenter"""
        return self._view

    @property
    def model(self: Any) -> HomeModel:
        """Return the model for this presenter"""
        return self._model
