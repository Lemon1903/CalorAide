"""_module summary_"""
import importlib

import View.HomeScreen.home_screen
from View import HomeScreenView

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.HomeScreen.home_screen)


class HomeScreenController:
    """
    The `HomeScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.home_screen.HomeScreenModel
        self.views = [HomeScreenView(controller=self, model=self.model)]

    def submit_for_review(self):
        print("submit")

    def get_views(self) -> list[HomeScreenView]:
        """Gets the view connected to this controller.

        Returns:
            HomeScreenView: The view connected to this controller.
        """
        return self.views
