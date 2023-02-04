"""_module summary_"""
import importlib

import View.HomeScreen.home_screen
from Utils import helpers
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
        self.has_loaded_profile = False

    def get_views(self) -> list[HomeScreenView]:
        """Gets the view connected to this controller.

        Returns:
            HomeScreenView: The view connected to this controller.
        """
        return self.views

    def load_profile_data(self, do_reload=False):
        """Loads all user profile information."""
        if not self.has_loaded_profile or do_reload:
            self.model.load_user_data()
            if do_reload:
                self.has_loaded_profile = False

    def reset_user_data(self):
        """Resets the user data to None."""
        self.model.reset_user_data()

    def update_user_data(self, textfields: list):
        """Updates user data in database.

        Args:
            textfields (list): the list of textfields to get the new data.
        """
        height = float(textfields[1].text)
        weight = float(textfields[0].text)
        bmi_classification = helpers.get_bmi_classification(height, weight)

        user_input = {
            "Name": textfields[2].text,
            "Height": height,
            "Weight": weight,
            "BMI": bmi_classification,
        }
        self.model.update_user_data(user_input)
