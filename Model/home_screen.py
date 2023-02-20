"""_module summary_"""

# pylint: disable=attribute-defined-outside-init
import multitasking

from Model.base_model import BaseScreenModel
from Utils import helpers

multitasking.set_max_threads()


class HomeScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.HomeScreen.profile_screen.HomeScreenView` class.
    """

    def __init__(self, database):
        self._database = database
        self.reset_all_local_data()

    def reset_all_local_data(self):
        """Resets all the data being monitored when user logs out."""
        # the data that the profile screen monitors
        self.user_profile_data = None
        self.user_all_history_data = None
        self.user_specific_intake_data = None

        # the data that the calorie counter screen monitors
        self.new_calorie_goal = None
        self.user_calorie_intake_data = None
        self.user_added_intake_data = None
        self.user_deleted_intake_data = None

        # indicates which part of the UI needs to change
        self.loaded_mode = False
        self.loaded_activity = False
        self.loaded_general_info = False
        self.loaded_calorie_progress = False
        self.loaded_intake_breakdown = False
        self.updated_calorie_part = None

    def update_local_profile_data(self):
        """Updates the user profile data stored."""
        if self.user_profile_data:
            self.user_profile_data.update(self._database.general_info)

    @multitasking.task
    def load_user_profile_data(self, part: str):
        """Loads UserInfo table of the user in database.

        Args:
            part (str): the part being updated in the profile screen.
        """
        self.user_profile_data = self._database.get_user_data("UserInfo")
        if part == "general information":
            self.loaded_general_info = True
            if self.user_profile_data:
                self._database.general_info.update(self.user_profile_data)
        else:
            self.loaded_activity = True
        self.notify_observers("profile screen")

    @multitasking.task
    def load_all_history_data(self):
        """Loads all the user history data in database."""
        self.user_all_history_data = self._database.get_user_data("History")
        self.loaded_calorie_progress = True
        self.notify_observers("profile screen")

    @multitasking.task
    def load_specific_intake_data(self, date_: str):
        """Loads the intake data of the user at specific date."""
        self.user_specific_intake_data = self._database.get_user_data(f"History/{date_}")
        self.loaded_intake_breakdown = True
        self.notify_observers("profile screen")

    @multitasking.task
    def load_user_calorie_intake_history(self):
        """Load user intake history in database"""
        date_today = helpers.get_date_today()
        self.user_calorie_intake_data = self._database.get_user_data(f"History/{date_today}")

        if self.user_calorie_intake_data is None:
            # connection error and no data is loaded
            self.new_calorie_goal = 0.0
        elif self.user_calorie_intake_data == {}:
            # no intake history meaning its a new day
            self._database.max_id = 0
            self.new_calorie_goal = self._database.get_user_data("UserInfo/Calorie Goal")
        else:
            # successfully loaded intake history in that day
            self._database.max_id = len(self.user_calorie_intake_data) - 1
            self.new_calorie_goal = self.user_calorie_intake_data["Calorie Goal"]

        self.updated_calorie_part = "intake history"
        self.notify_observers("calorie counter screen")

    @multitasking.task
    def update_user_profile_data(self, user_input: dict):
        """Updates the user data in database.

        Args:
            user_input (list): the list of user input to be sent to the database.
        """
        self._database.update_user_data(user_input, "UserInfo")
        if "Activity" in user_input:
            self.load_user_profile_data("activity")
        else:
            self._database.general_info.update(user_input)
            self.load_user_profile_data("general information")

    @multitasking.task
    def update_calorie_goal(self, new_calorie_goal: float, table_name: str):
        """Updates the calorie goal of the user in the database.

        Args:
            new_calorie_goal (float): the updated calorie goal.
            table_name (str): the table where calorie goal will be updated.
        """
        new_data = {"Calorie Goal": new_calorie_goal}
        if self._database.update_user_data(new_data, table_name):
            if table_name.startswith("History"):
                self.new_calorie_goal = new_calorie_goal
                self.updated_calorie_part = "calorie goal"
                self.notify_observers("calorie counter screen")
        else:
            self.new_calorie_goal = 0.0

    @multitasking.task
    def add_intake_to_database(self, user_input: list):
        """Adds the food intake to the users history.

        Args:
            user_data (list): the list of intake input to be inserted to the users history.
        """
        # the data to be added to the database
        self._database.max_id += 1
        date_today = helpers.get_date_today()
        intake_data = {
            self._database.max_id: {
                "Food": user_input[1],
                "Calorie Amount": user_input[0],
            }
        }

        if self._database.update_user_data(intake_data, f"History/{date_today}"):
            # added successfully to the database
            self.user_calorie_intake_data = self._database.get_user_data(f"History/{date_today}")
            self.user_added_intake_data = (
                self._database.max_id, intake_data[self._database.max_id]
            )
        else:
            # connection error and nothing is added
            self.user_added_intake_data = None

        self.updated_calorie_part = "intake history add"
        self.notify_observers("calorie counter screen")

    @multitasking.task
    def delete_intake_to_database(self, delete_list: list):
        """Deletes the food intake of the user in database.

        Args:
            delete_list (list): the list of items to be deleted.
        """
        # the data to be updated in the database
        date_today = helpers.get_date_today()

        if self._database.delete_user_data_collection(delete_list, f"History/{date_today}"):
            # successfully updated and delete data in database
            self.user_calorie_intake_data = self._database.get_user_data(f"History/{date_today}")
            self.user_deleted_intake_data = delete_list
        else:
            # connection error and no data deleted or updated
            self.user_deleted_intake_data = None

        self.updated_calorie_part = "intake history delete"
        self.notify_observers("calorie counter screen")
