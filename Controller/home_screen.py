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
        self.has_loaded_profile = False
        self.has_loaded_calorie_counter = False

    def get_views(self) -> list[HomeScreenView]:
        """Gets the view connected to this controller.

        Returns:
            list[HomeScreenView]: The views connected to this controller.
        """
        return self.views

    def load_user_data(self, do_reload=False):
        """Loads all user profile information."""
        if (
            not self.has_loaded_profile
            and not self.has_loaded_calorie_counter
            or do_reload
        ):
            if do_reload:
                self.has_loaded_profile = False
                self.has_loaded_calorie_counter = False
                self.views[0].connection_error_snackbar.dismiss()
            self.views[0].open_loading_view()
            self.model.load_user_profile_data()
            self.model.load_user_intake_history()

    def show_connection_error(self):
        """Shows the connection error snackbar."""
        self.views[0].connection_error_snackbar.open()

    def reset_user_profile_data(self):
        """Resets the user data to None."""
        self.model.reset_user_profile_data()

    def reset_calorie_counter_data(self):
        """Resets the calorie counter data to None."""
        self.model.reset_calorie_counter_data()

    def update_user_profile_data(self, textfields: list):
        """Updates user data in database.

        Args:
            textfields (list): the list of textfields to get the new data.
        """
        self.views[0].open_loading_view()
        user_input = [
            textfields[2].text,
            float(textfields[1].text),
            float(textfields[0].text),
        ]
        self.model.update_user_profile_data(user_input)

    def add_intake_to_database(self, user_input: list, calorie_goal: float):
        """Adds the food intake to the users history in database.

        Args:
            user_input (list): the list of user inputs to be stored.
            calorie_goal (float): the calorie goal to be updated.
        """
        self.views[0].open_loading_view()
        user_input[0] = float(user_input[0])
        new_calorie_goal = calorie_goal - user_input[0]
        self.model.add_intake_to_database(user_input, new_calorie_goal)

    def delete_intake_to_database(self, calorie_screen, calorie_goal: float):
        """Deletes the food intake of the user in database.

        Args:
            calorie_screen (CalorieCounterScreenView): the calorie counter screen view.
            calorie_goal (float): the calorie goal to be updated.
        """
        self.views[0].open_loading_view()
        checked_items = calorie_screen.get_checked_items()
        for item in checked_items:
            calorie_goal += item.calorie_amount
        self.model.delete_intake_to_database(checked_items, calorie_goal)
