"""_module summary_"""
import importlib

import View.RegisterScreen.goal_screen
import View.RegisterScreen.mode_screen
import View.RegisterScreen.register_screen
from Utils import helpers
from View import GoalScreenView, ModeScreenView, RegisterScreenView

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.RegisterScreen.goal_screen)
importlib.reload(View.RegisterScreen.mode_screen)
importlib.reload(View.RegisterScreen.register_screen)


class RegisterScreenController:
    """
    The `RegisterScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.register_screen.RegisterScreenModel
        self.views = [
            RegisterScreenView(controller=self, model=self.model),
            ModeScreenView(controller=self, model=self.model),
            GoalScreenView(controller=self, model=self.model)
        ]
        self.user_inputs = {}

    def get_views(self) -> list[RegisterScreenView]:
        """Gets the view connected to this controller.

        Returns:
            RegisterScreenView: The view connected to this controller.
        """
        return self.views

# =================Registration Screen=============================================

    def confirm_registration(self, user_inputs: dict):
        """This function initializes all the values collected from the registration.
        Then calculates all of the remaining data to show.
        We are using metric system in our application.
        """
        user_bmi_value = helpers.get_bmi_value(user_inputs["Height"], user_inputs["Weight"])
        self.user_inputs = user_inputs
        self.user_inputs.update({
            "BMI Value": user_bmi_value,
            "BMI": helpers.get_bmi_classification(user_bmi_value)
        })
        self.model.set_bmi(self.user_inputs["BMI"])
        self.model.set_bmi_value(self.user_inputs["BMI Value"])

# =================Mode Screen======================================================

    def get_database_bmi(self):
        """Gets the BMI from the `Database` class."""
        return self.model.get_bmi()

    def get_database_bmi_value(self):
        """Gets the BMI value from the `Database` class."""
        return self.model.get_bmi_value()

    def set_goal_screen(self, user_mode: str):
        """Setting the UI of the Goal screen based on the inputs from the past screen."""
        self.views[2].user_mode = user_mode

# =================Goal Screen======================================================

    def compile_details(self, screen_from: str):
        """This compiles all the inputs from the Register Screen.
        All will be passed to the application's Database.
        """
        user_bmr = helpers.get_user_bmr(
            self.user_inputs["Gender"],
            self.user_inputs["Weight"],
            self.user_inputs["Height"],
            self.user_inputs["Age"],
        )
        calorie_goal = helpers.calculate_calorie_goal(
            user_bmr,
            self.user_inputs["Activity"],
            self.views[1].user_mode,
            self.views[2].user_goal,
        )
        self.user_inputs.update({
            "Mode": self.views[1].user_mode,
            "Intensity": self.views[2].user_goal,
            "Calorie Goal": calorie_goal,
            "BMR": user_bmr,
        })
        self.model.store_user_info(self.user_inputs, screen_from)