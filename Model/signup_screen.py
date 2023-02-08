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
        self.database = database

    def is_username_taken(self, username_input: str):
        """Checks if the username input is already taken."""
        return username_input in self.database.get_data_table()

    @multitasking.task
    def to_database(self, user_input: list[str]):
        """If the user input is valid this function is called to add the data into the database."""
        if self.database.add_user_data(user_input):
            self.notify_observers("signup screen")
