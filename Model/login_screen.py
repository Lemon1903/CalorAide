"""_module summary_"""

import multitasking

from Model.base_model import BaseScreenModel

multitasking.set_max_threads(10)


class LoginScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.ProfileScreen.profile_screen.ProfileScreenView` class.
    """

    def __init__(self, database):
        self._database = database
        self.is_account_exist = False
        self.has_account = False

    def reset_is_account_exist(self):
        """Resets the `is_account_exist` after checking."""
        self.is_account_exist = False

    @multitasking.task
    def is_account_taken(self, username: str, password: str):
        """A method that checks if certain username and password exist in database."""
        data = self._database.get_data_table()
        for key, value in data.items():
            if key == username and value["UserInfo"]["Password"] == password:
                self.is_account_exist = True
                self._database.username = username
                self.has_account = "Name" in value["UserInfo"]
                break
        self.notify_observers("login screen")
