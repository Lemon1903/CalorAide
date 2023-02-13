"""_module summary_"""

import importlib
from decimal import Decimal

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

    def get_views(self) -> list[HomeScreenView]:
        """Gets the view connected to this controller.

        Returns:
            list[HomeScreenView]: The views connected to this controller.
        """
        return self.views

    def load_user_data(self, do_reload=False):
        """Loads all user information."""
        if do_reload:
            self.model.has_loaded_profile = False
            self.model.has_loaded_intake_history = False

        if not self.model.has_loaded_screens():
            self.views[0].open_loading_view()
            self.model.load_user_profile_data()
            self.model.load_user_intake_history()

    def show_connection_error(self):
        """Shows the connection error snackbar."""
        self.views[0].connection_error_snackbar.open()

    def hide_connection_error(self):
        """Hides the connection error snackbar."""
        self.views[0].connection_error_snackbar.dismiss()

    def update_user_profile_data(self, textfields: list):
        """Updates user data in database.

        Args:
            textfields (list): the list of textfields to get the new data.
        """
        self.views[0].open_loading_view()
        height = float(textfields[1].text)
        weight = float(textfields[0].text)
        bmi_classification = helpers.get_bmi_classification(height, weight)
        user_input = {
            "Name": textfields[2].text,
            "Height": height,
            "Weight": weight,
            "BMI": bmi_classification,
        }
        self.model.update_user_profile_data(user_input)

    def add_intake_to_database(self, user_input: list, calorie_goal: float):
        """Adds the food intake to the users history in database.

        Args:
            user_input (list): the list of user inputs to be stored.
            calorie_goal (float): the calorie goal to be updated.
        """
        self.views[0].open_loading_view()
        date_today = helpers.get_date_today()
        user_input[0] = float(user_input[0])
        calorie_goal -= user_input[0]
        self.model.update_calorie_goal(round(calorie_goal, 1), f"History/{date_today}")
        self.model.add_intake_to_database(user_input)

    def delete_intake_to_database(self, checked_items: list, calorie_goal: float):
        """Deletes the food intake of the user in database.

        Args:
            calorie_screen (CalorieCounterScreenView): the calorie counter screen view.
            calorie_goal (float): the calorie goal to be updated.
        """
        self.views[0].open_loading_view()
        date_today = helpers.get_date_today()
        calorie_goal += sum(item.calorie_amount for item in checked_items)
        self.model.update_calorie_goal(round(calorie_goal, 1), f"History/{date_today}")
        self.model.delete_intake_to_database(checked_items)

    def update_all_calorie_goal(self, new_activity: str):
        """Updates the base calorie goal and current calorie goal of the user.
        
        Args:
            new_activity (str): the new activity selected by the user.
        """
        self.views[0].open_loading_view()
        date_today = helpers.get_date_today()
        user_data = self.model.user_profile_data

        # compute new calorie goal for the user information.
        bmr = helpers.get_user_bmr(
            user_data["Gender"], user_data["Weight"], user_data["Height"], user_data["Age"]
        )
        calorie_goal = helpers.calculate_calorie_goal(
            bmr, new_activity, user_data["Mode"], user_data["Goal"]
        )
        self.model.update_user_profile_data({"Activity": new_activity})
        self.model.update_calorie_goal(float(calorie_goal), "UserInfo")

        # compute new calorie goal for the calorie counter screen
        for identifier, item in self.model.user_intake_history_data.items():
            if identifier != "Calorie Goal":
                calorie_goal -= Decimal(str(item["Calorie Amount"]))
        self.model.update_calorie_goal(float(calorie_goal), f"History/{date_today}")
        