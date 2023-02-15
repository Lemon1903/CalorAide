"""_module summary_"""
from __future__ import annotations

from typing import Union

import requests
from firebase import firebase


class DataBase:
    """Your methods for working with the database should be implemented in this class."""

    def __init__(self):
        self.firebase_ = firebase.FirebaseApplication("https://fitrex-bfc21-default-rtdb.asia-southeast1.firebasedatabase.app/")

    def get_data(self):
        """A method that gets the data from the database that has a table name USERDATA"""
        try:
            data = self.firebase_.get("USERDATA", '')
        except requests.exceptions.ConnectionError:
            return None
        return data 