"""_module summary_"""

import requests
from firebase import firebase


class DataBase:
    """Your methods for working with the database should be implemented in this class."""

    def __init__(self):
        self._firebase = firebase.FirebaseApplication(
            "https://fitrex-bfc21-default-rtdb.asia-southeast1.firebasedatabase.app/"
        )

    # TODO: can be removed
    def get_data_table(self):
        """Returns the USERDATA table from database."""
        try:
            data = self._firebase.get("USERDATA", "", connection=None)
            return data
        except requests.exceptions.ConnectionError:
            return None

    # TODO: can be removed or stay
    def add_user_data(self, user_input):
        """Adds userdata to database."""
        try:
            data = {"Password": user_input[1]}
            self._firebase.put(
                f"USERDATA/{user_input[2]}", "UserInfo", data, connection=None
            )
            return True
        except requests.exceptions.ConnectionError:
            return False
