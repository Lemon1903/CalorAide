"""_module summary_"""

import multitasking

from Model.base_model import BaseScreenModel

multitasking.set_max_threads(10)


class RegisterScreenModel(BaseScreenModel):
    """
    Implements the data logic of the
    :class:`~View.RegisterScreen.register_screen.RegisterScreenView`,
    :class:`~View.RegisterScreen.mode_screen.ModeScreenView`,
    :class:`~View.RegisterScreen.goal_screen.GoalScreenView`, classes.
    """

    def __init__(self, database):
        self._database = database

    def get_general_info(self):
        """Get the general info from the database."""
        return self._database.general_info

    def set_general_info(self, data: dict):
        """Get the general info from the database."""
        self._database.general_info.update(data)

    @multitasking.task
    def store_user_info(self, user_data, screen_from, from_profile):
        """This function receives the user's information list from the Controller.
        It will then store each value into a dictionary and call a model function
        to pass it to the Firebase Database.
        """
        # TODO: add connection error
        if self._database.update_user_data(user_data, "UserInfo"):
            self._database.general_info.update(user_data)
            self.notify_observers(screen_from)

        if from_profile:
            self.notify_observers("profile screen")
