"""_module summary_"""

import multitasking

from Model.base_model import BaseScreenModel

multitasking.set_max_threads(10)


class ProfileScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.ProfileScreen.profile_screen.ProfileScreenView` class.
    """

    def __init__(self, database):
        # Just an example of the data. Use your own values.
        self._data = None
        self.database = database

    @property
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

    @multitasking.task
    def check_data(self):
        """Just an example of the method. Use your own code."""
        self.data = ["example item"]
