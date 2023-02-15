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
        # TODO: add a data to be monitored by the view
        self._database = database

    # TODO: make this a multitasking task and follows Observer pattern
    def is_account_taken(self, username: str, password: str):
        """ A method that checks if certain username and password exist in database. """
        data = self._database.get_data_table()
        for key, value in data.items():
            if key == username and value["UserInfo"]["Password"] == password:
                return True
        return False
