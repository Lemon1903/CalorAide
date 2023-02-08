"""_module summary_"""
import importlib

import View.ProfileScreen.profile_screen
from View import ProfileScreenView

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.ProfileScreen.profile_screen)


class ProfileScreenController:
    """
    The `ProfileScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.profile_screen.ProfileScreenModel
        self.views = [ProfileScreenView(controller=self, model=self.model)]

    def get_views(self) -> list[ProfileScreenView]:
        """Gets the view connected to this controller.

        Returns:
            ProfileScreenView: The view connected to this controller.
        """
        return self.views
