"""_module summary_"""

import requests
from firebase import firebase


class DataBase:
    """Your methods for working with the database should be implemented in this class."""

    def __init__(self):
        self._firebase = firebase.FirebaseApplication(
            "https://fitrex-bfc21-default-rtdb.asia-southeast1.firebasedatabase.app/"
        )
        self.bmi = ""
        self.bmi_value = 0.0
        self.username = ""

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

    # TODO: can be removed
    def get_data_table(self):
        """Returns the USERDATA table from database."""
        try:
            data = self._firebase.get("USERDATA", "", connection=None)
            return data
        except requests.exceptions.ConnectionError:
            return None

    def get_user_data(self, table_name: str) -> dict | None:
        """Returns data of the selected collection from the database.

        Args:
            table_name (str): the table under user table to be accessed.
        """
        try:
            data = self._firebase.get(
                f"USERDATA/{self.username}", table_name, connection=None
            )
            return data if data else {}
        except requests.exceptions.ConnectionError:
            return None

    def update_user_data(self, new_data: dict, table_name: str):
        """Updates user data of the selected collection in database.

        Args:
            new_data (dict): the new user data to be stored.
            table_name (str): the table under user table to be accessed.
        """
        try:
            self._firebase.patch(
                f"USERDATA/{self.username}/{table_name}", new_data, connection=None
            )
            return True
        except requests.exceptions.ConnectionError:
            return False

    def delete_user_data_collection(self, delete_list: list, table_name: str):
        """Deletes user data of the selected collection in the database.

        Args:
            delete_list (list): the list of items to be deleted.
            table_name (str): the table under user table to be accessed.
        """
        try:
            for delete_item in delete_list:
                self._firebase.delete(
                    f"USERDATA/{self.username}/{table_name}",
                    int(delete_item.identifier),
                    connection=None,
                )
            return True
        except requests.exceptions.ConnectionError:
            return False
