"""Presenter for the Home tab"""
import os
from qtpy.QtWidgets import QWidget


class HomePresenter:
    """Home presenter"""

    def __init__(self, view, model):
        self._view = view
        self._model = model
 
    @property
    def view(self):
        """Return the view for this presenter"""
        return self._view

    @property
    def model(self):
        """Return the model for this presenter"""
        return self._model
