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
        self._is_done_adding = None
        self.database = database

    @property
    def is_done_adding(self):  # get
        """_data summary_

        Returns:
            _type_: _description_
        """
        return self._is_done_adding

    @is_done_adding.setter
    def is_done_adding(self, value):  # set
        # We notify the View -
        # :class:`~View.MainScreen.main_screen.MainScreenView` about the
        # changes that have occurred in the data model.
        self._is_done_adding = value
        self.notify_observers("signup screen")

    def is_username_taken(self, username_input: str):
        data = self.database.get_data_table()
        for key in data.values():
            if key == username_input:
                return True
        return False

    @multitasking.task
    def to_database(self, user_input: list[str]):
        self.is_done_adding = self.database.add_user_data(user_input)
