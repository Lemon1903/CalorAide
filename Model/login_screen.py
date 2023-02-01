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
        self._data = None
        self.database = database
        self.result = ""

    @property # getter
    def data(self):
        """_data summary_

        Returns:
            _type_: _description_
        """
        return self._data

    @data.setter 
    def data(self, value):
        # We notify the View -
        # :class:`~View.ProfileScreen.profile_screen.ProfileScreenView` about the
        # changes that have occurred in the data model.
        self._data = value
        self.notify_observers("profile screen")

    # @multitasking.task
    def is_username_taken(self, login_info):
        """Just an example of the method. Use your own code."""
        # self.database.create_table()
        self.username = login_info[0]
        self.password = login_info[1]
        self.db = self.database.get_data()

        for key, value in self.db.items(): 
            if value["Username"] == self.username and value["Password"] == self.password:  
                return True
           
        return False