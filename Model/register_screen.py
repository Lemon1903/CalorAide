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

    def get_bmi(self):
        """Returns the temporary bmi in `Database`."""
        return self._database.bmi

    def set_bmi(self, bmi):
        """Sets a new temporary bmi in `Database`."""
        self._database.bmi = bmi

    def get_bmi_value(self):
        """Returns the temporary bmi value in `Database`."""
        return self._database.bmi_value

    def set_bmi_value(self, bmi_value):
        """Sets a new temporary bmi value in `Database`."""
        self._database.bmi_value = bmi_value

    @multitasking.task
    def store_user_info(self, user_data, screen_from):
        """This function receives the user's information list from the Controller.
        It will then store each value into a dictionary and call a model function
        to pass it to the Firebase Database.
        """
        # TODO: add connection error
        if self._database.update_user_data(user_data, "UserInfo"):
            self.notify_observers(screen_from)
