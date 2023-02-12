"""_module summary_"""
import importlib
import time

import multitasking

import View.HistoryScreen.history_screen
from View import HistoryScreenView

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.HistoryScreen.history_screen)


class HistoryScreenController:
    """
    The `HistoryScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.main_screen.MainScreenModel
        self.views = [HistoryScreenView(self, self.model)]

    def get_data_from_model(self):
        """ Get data from history table thru model """
        self.history_data = self.model.getting_history_data()
        return(self.history_data)


    def get_views(self) -> list[HistoryScreenView]:
        """Gets the view connected to this controller.

        Returns:
            HistoryScreenView: The view connected to this controller.
        """
        return self.views
