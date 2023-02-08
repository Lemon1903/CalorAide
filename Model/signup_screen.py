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
        self._is_done_adding = None
        self.database = database

    @property
    def is_done_adding(self):  # get
        """Indicates if the data is already been added to the database."""
        return self._is_done_adding

    @is_done_adding.setter
    def is_done_adding(self, value):  # set
        # We notify the View -
        # :class:`~View.MainScreen.main_screen.MainScreenView` about the
        # changes that have occurred in the data model.
        self._is_done_adding = value
        self.notify_observers("signup screen")

    def is_username_taken(self, username_input: str):
        """Checks if the username input is already taken."""
        data = self.database.get_data_table()
        for key in data.values():
            if key == username_input:
                return True
        return False

    @multitasking.task
    def to_database(self, user_input: list[str]):
        """If the user input is valid this function is called to add the data into the database."""
        self.is_done_adding = self.database.add_user_data(user_input)
