"""_module summary_"""

import multitasking

from Model.base_model import BaseScreenModel
from Utils import helpers

multitasking.set_max_threads(10)


class HomeScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.HomeScreen.profile_screen.HomeScreenView` class.
    """

    def __init__(self, database):
        self._new_calorie_goal = None
        self.user_profile_data = None
        self.user_intake_data = None
        self.updated_profile_part = None
        self.updated_calorie_part = None
        self.database = database

    @property
    def new_calorie_goal(self):
        """Returns the current calorie goal."""
        return self._new_calorie_goal

    # TODO: tentative pa if 0 na kapag less than 0 or ipakita pa negative pero nakared.
    @new_calorie_goal.setter
    def new_calorie_goal(self, value):
        """Sets the new value to the calorie goal."""
        self._new_calorie_goal = value if value >= 0 else 0

    def reset_user_profile_data(self):
        """Resets user data to None and removes Spinner."""
        self.user_profile_data = None
        self.notify_observers("home screen")

    def reset_calorie_counter_data(self):
        """Resets calorie counter data to None and removes Spinner."""
        self.user_intake_data = None
        self._new_calorie_goal = None
        self.notify_observers("home screen")

    @multitasking.task
    def load_user_profile_data(self):
        """Load user profile data in database"""
        self.user_profile_data = self.database.get_user_data("UserInfo")
        self.updated_profile_part = "general information"
        self.notify_observers("profile screen")

    @multitasking.task
    def load_user_intake_history(self):
        """Load user intake history in database"""
        date_today = helpers.get_date_today()
        self.user_intake_data = self.database.get_user_data(f"History/{date_today}")
        if self.user_intake_data:
            self.database.max_id = len(self.user_intake_data) - 1
            self.new_calorie_goal = self.user_intake_data["Calorie Goal"]
        else:
            self.database.max_id = 0
            # TODO: papalitan pa ng default value na nasa UserInfo
            self.new_calorie_goal = 1900.0
        self.updated_calorie_part = "intake history"
        self.notify_observers("calorie counter screen")

    @multitasking.task
    def update_user_profile_data(self, user_input: list):
        """Updates the user data in database.

        Args:
            user_data (list): the list of user input to be sent to the database.
        """
        bmi_classification = helpers.get_bmi_classification(
            user_input[1], user_input[2]
        )
        data = {
            "Name": user_input[0],
            "Height": user_input[1],
            "Weight": user_input[2],
            "BMI": bmi_classification,
        }
        self.database.update_user_data(data, "UserInfo")
        self.load_user_profile_data()

    @multitasking.task
    def add_intake_to_database(self, user_input: list, new_calorie_goal: float):
        """Adds the food intake to the users history.

        Args:
            user_data (list): the list of intake input to be inserted to the users history.
            new_calorie_goal (float): the updated calorie goal.
        """
        self.database.max_id += 1
        date_today = helpers.get_date_today()
        intake_data = {
            self.database.max_id: {
                "Food": user_input[1],
                "Calorie Amount": user_input[0],
            },
            "Calorie Goal": new_calorie_goal,
        }

        if self.database.update_user_data(intake_data, f"History/{date_today}"):
            self.new_calorie_goal = new_calorie_goal
            self.user_intake_data = (
                self.database.max_id,
                intake_data[self.database.max_id],
            )
        else:
            self.new_calorie_goal = 0.0
            self.user_intake_data = None

        self.updated_calorie_part = "intake history add"
        self.notify_observers("calorie counter screen")

    @multitasking.task
    def delete_intake_to_database(self, delete_list: list, new_calorie_goal: float):
        """Deletes the food intake of the user in database.

        Args:
            delete_list (list): the list of items to be deleted.
            new_calorie_goal (float): the updated calorie goal.
        """
        date_today = helpers.get_date_today()
        new_data = {"Calorie Goal": new_calorie_goal}

        if self.database.delete_user_data_collection(
            delete_list, f"History/{date_today}"
        ) and self.database.update_user_data(new_data, f"History/{date_today}"):
            self.new_calorie_goal = new_calorie_goal
            self.user_intake_data = delete_list
        else:
            self.new_calorie_goal = 0.0
            self.user_intake_data = None

        self.updated_calorie_part = "intake history delete"
        self.notify_observers("calorie counter screen")
