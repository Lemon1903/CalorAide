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
importlib.reload(View.RegisterScreen.register_screen)

class RegisterScreenController:
    """
    The `RegisterScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    name = None
    gender = None
    height = 0
    weight = 0
    age = 0
    activity = None
    calorie_goal = 0

    user_bmi = None
    user_mode = None
    user_goal = None

    user_bmi_amount = 0
    user_bmr = 0

    def __init__(self, model):
        self.model = model  # Model.register_screen.RegisterScreenModel
        self.views = [
            RegisterScreenView(controller = self, model = self.model),
            ModeScreenView(controller = self, model = self.model),
            GoalScreenView(controller = self, model = self.model)
            ]

    def get_views(self) -> list[RegisterScreenView]:
        """Gets the view connected to this controller.

        Returns:
            RegisterScreenView: The view connected to this controller.
        """
        return self.views

# =================Registration Screen 1============================================

    def confirm_registration(self):
        """This function initializes all the values collected from the registration.
        Then calculates all of the remaining data to show.
        We are using metric system in our application.
        """
        user_info = self.views[0].store_details()
        self.name = user_info[0]
        self.gender = user_info[1]
        self.height = user_info[2]
        self.weight = user_info[3]
        self.age = user_info[4]
        self.activity = user_info[5]
        self.user_bmi = helpers.get_bmi_classification(self.height, self.weight)
        self.user_bmi_amount = self.get_bmi_amount(self.height, self.weight)
        self.user_bmr = helpers.get_user_bmr(self.gender, self.weight, self.height, self.age)

        self.model.push_bmi(self.user_bmi)

        self.views[1].change_screen("left", "mode screen")

    def pull_database_bmi(self):
        """Gets the BMI from the Database file"""
        return self.model.pull_bmi()

    def get_user_bmr(self, gender, weight, height, age):
        """This formula is based on Mifflin-St. Jeor Equation.
        This returns the value of the Basal Metabolic Rate of a person.
        That is the amount of calories they naturally burn with bodily functions.
        """
        bmr = 0
        if gender == "Male":
            bmr = float((10*weight)+(6.25*height)-(5*age)+5)
        elif gender == "Female":
            bmr = float((10*weight)+(6.25*height)-(5*age)-161)
        return bmr

    def get_bmi_amount(self, height_cm, weight_kg):
        """BMI formula that estimates a person's fat based on their height and weight.
        This function will return user's BMI value.
        """
        height_m = height_cm / 100
        return weight_kg/ (height_m**2)

# =================Registration Screen 2============================================

    def set_to_sedentary(self):
        """This sets the intensity to default as sedentary.
        Redirects the screen to the home screen.
        """
        self.user_goal = "sedentary"
        self.compile_details()

    def set_goal_screen(self):
        """Setting the UI of the Goal screen based on the inputs from the past screen."""
        self.views[2].ids.goal_label.text = self.views[2].show_goal_label(self.user_mode)

# =================Registration Screen 3============================================

    def get_user_goal(self):
        """Receives the goal of choice of the user from the second view."""
        self.user_goal = self.views[2].chosen_button
        self.compile_details()

    def compile_details(self):
        """This compiles all the inputs from the Register Screen.
        All will be passed to the application's Database.
        """
        self.calorie_goal = helpers.calculate_calorie_goal(
                self.user_bmr, self.activity, self.user_mode, self.user_goal)
        user_info = [self.name, self.age, self.height, self.weight, self.gender, self.activity,
                    self.user_bmi, self.user_mode, self.user_goal, self.calorie_goal, self.user_bmr]
        self.model.get_user_info(user_info)
        # Move to the main screen
