"""_module summary_"""

from typing import Union

import requests
from firebase import firebase

class DataBase:
    """Your methods for working with the database should be implemented in this class."""
    def __init__(self):
        self.firebase_ = firebase.FirebaseApplication("https://fitrex-bfc21-default-rtdb.asia-southeast1.firebasedatabase.app/")

    #USERDATA is the Table
    def get_data_table(self):
        """
        Returns data from database.
        """
        try:
            data = self.firebase_.get("USERDATA", '')
            return data
        except requests.exceptions.ConnectionError:
            return None

    def add_user_data(self, user_input):
        """
        Adds userdata to database
        """
        self.data = {"Password": user_input[1]}
        self.firebase_.put("USERDATA", user_input[0], self.data)
