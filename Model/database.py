"""_module summary_"""
from __future__ import annotations

import requests
from firebase import firebase


class DataBase:
    """Your methods for working with the database should be implemented in this class."""

    # Address for users collections.
    DATABASE_URL = (
        "https://sample-d0d72-default-rtdb.asia-southeast1.firebasedatabase.app/"
    )

    def __init__(self):
        self.real_time_firebase = firebase.FirebaseApplication(self.DATABASE_URL, None)

    def get_user_data(self, key: str = "Lemon") -> dict | bool | None:
        """Returns data of the selected collection from the database."""
        try:
            data = self.real_time_firebase.get("USERDATA", key, connection=None)
            return data
        except requests.exceptions.ConnectionError:
            return None

    def update_user_data(self, user_input: dict, key: str = "Lemon"):
        """Updates user data in database.

        Args:
            user_input (dict): the new user data to be stored.
        """
        try:
            self.real_time_firebase.patch(
                url=f"USERDATA/{key}", data=user_input, connection=None
            )
            return True
        except requests.exceptions.ConnectionError:
            return False
