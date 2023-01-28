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
        self._is_valid = None
        self.database = database

    @property
    def is_valid(self):
        """_data summary_

        Returns:
            _type_: _description_
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, value):
        # We notify the View -
        # :class:`~View.ProfileScreen.profile_screen.ProfileScreenView` about the
        # changes that have occurred in the data model.
        self._is_valid = value
        self.notify_observers("login screen")

    @multitasking.task
    def check_data(self):
        """Just an example of the method. Use your own code."""
        # data = database
        # if true:
        #   is_valid = True
        #   updatae_database()
        # else:
        #   is_valid = False
