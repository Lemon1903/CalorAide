"""_module summary_"""
import multitasking

from Model.base_model import BaseScreenModel

multitasking.set_max_threads(10)


class SignupScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.SignupScreen.signup_screen.SignupScreenView` class.
    """

    def __init__(self, database):
        # Just an example of the data. Use your own values.
        self._is_valid = False
        self.database = database

    @property
    def is_valid(self):  # get
        """_data summary_

        Returns:
            _type_: _description_
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, value):  # set
        # We notify the View -
        # :class:`~View.MainScreen.main_screen.MainScreenView` about the
        # changes that have occurred in the data model.
        self._is_valid = value
        self.notify_observers("signup screen")

    @multitasking.task
    def to_database(self, user_data):
        self.is_valid = True
        self.database.add(user_data)

    @multitasking.task
    def is_username_taken(self, username_input: str):
        data = self.database.get_data()
        for value in data.values():
            if value["Username"] == username_input:
                return True
        return False
