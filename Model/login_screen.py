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
        # Just an example of the data. Use your own values.
        self.database = database

    def is_account_taken(self, username: str, password: str):
        """ A method that checks if certain username and password exist in database. """
        data = self.database.get_data()
        for value in data.values(): 
            if value["Username"] == username and value["Password"] == password:  
                return True
        return False
