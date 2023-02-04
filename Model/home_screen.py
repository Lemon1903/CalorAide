"""_module summary_"""

import multitasking

from Model.base_model import BaseScreenModel

multitasking.set_max_threads(10)


class HomeScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.HomeScreen.profile_screen.HomeScreenView` class.
    """

    def __init__(self, database):
        # Just an example of the data. Use your own values.
        self._user_data = None
        self.updated_part = None
        self.database = database

    @property
    def user_data(self):
        """The current data of the user."""
        return self._user_data

    @user_data.setter
    def user_data(self, value: dict | None):
        # We notify the View -
        # :class:`~View.HomeScreen.profile_screen.HomeScreenView` about the
        # changes that have occurred in the data model.
        self._user_data = value
        self.updated_part = "general information"
        self.notify_observers("profile screen")

    def reset_user_data(self):
        """Resets user data to None and removes Spinner."""
        self._user_data = None
        self.notify_observers("home screen")

    @multitasking.task
    def load_user_data(self):
        """Query user data in database"""
        self.notify_observers("home screen")
        self.user_data = self.database.get_user_data()

    @multitasking.task
    def update_user_data(self, user_data: dict):
        """Updates the user data in database.

        Args:
            user_data (dict): the JSON format data to be sent to the database.
        """
        self.database.update_user_data(user_data)
        self.load_user_data()
