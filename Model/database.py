"""_module summary_"""
from __future__ import annotations

from typing import Union

import requests
from firebase import firebase


class DataBase:
    """Your methods for working with the database should be implemented in this class."""

    def __init__(self):
        # self.real_time_firebase = firebase.FirebaseApplication(self.DATABASE_URL, None)
        self.firebase_ = firebase.FirebaseApplication("https://fitrex-bfc21-default-rtdb.asia-southeast1.firebasedatabase.app/")

    def get_data(self):
        
        try:
            data = self.firebase_.get("USERDATA", '')
        except requests.exceptions.ConnectionError:
            return None
        return data 