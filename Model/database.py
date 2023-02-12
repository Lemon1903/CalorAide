"""_module summary_"""

from typing import Union

import requests
from firebase import firebase


class DataBase:
    """Your methods for working with the database should be implemented in this class."""

    def __init__(self):
        self._firebase = firebase.FirebaseApplication(
            "https://fitrex-bfc21-default-rtdb.asia-southeast1.firebasedatabase.app/"
        )
        self.bmi = ""
        self._username = "Daniel"

    # USERDATA is the Table
    def get_data_table(self):
        """Returns data from database."""
        try:
            data = self._firebase.get("USERDATA", '')
        except requests.exceptions.ConnectionError:
            return None
        return data

    def create_table(self):
        self.data ={
            "Username" : "rae",
            "Password" : "try",
            "Name": "Asd Fgh",
            "Height": 175,
            "Weight": 60,
            "Activity": 1,

        }
        self._firebase.post("https://fitrex-bfc21-default-rtdb.asia-southeast1.firebasedatabase.app/USERDATA", self.data)

    def add(self, userdata):
        self.data = {
            "Username": userdata[0],
            "Password": userdata[1],
        }
        self._firebase.post("https://fitrex-bfc21-default-rtdb.asia-southeast1.firebasedatabase.app/USERDATA", self.data)
        print("Posted!")

        return()

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

    def update_user_data(self, new_data: dict, table_name: str):
        """Updates user data of the selected collection in database.
        Args:
            user_input (dict): the new user data to be stored.
            key (str): the user table to be accessed.
            table_name (str): the table under user table to be accessed.
        """
        try:
            self._firebase.patch(
                f"USERDATA/{self._username}/{table_name}", new_data, connection=None
            )
            return True
        except requests.exceptions.ConnectionError:
            return False
