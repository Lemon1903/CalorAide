"""_module summary_"""
from __future__ import annotations

from typing import Union

import requests
from firebase import firebase

# import socket



# def get_connect(func, host="8.8.8.8", port=53, timeout=3):
#     """Checks for an active Internet connection."""

#     def wrapped(*args):
#         try:
#             socket.setdefaulttimeout(timeout)
#             socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
#             return func(*args)
#         except Exception:
#             return False

#     return wrapped


class DataBase:
    """Your methods for working with the database should be implemented in this class."""

    # name = "Firebase"

    # Address for users collections.
    # DATABASE_URL = "https://fitrydb-default-rtdb.asia-southeast1.firebasedatabase.app/"

    # RealTime Database attribute.
    # USER_DATA = "Userdata"

    def __init__(self):
        # self.real_time_firebase = firebase.FirebaseApplication(self.DATABASE_URL, None)
        self.firebase_ = firebase.FirebaseApplication("https://fitrex-bfc21-default-rtdb.asia-southeast1.firebasedatabase.app/")

    # @get_connect
    # def get_data_from_collection(self, name_collection: str) -> dict | bool | None:
    #     """Returns data of the selected collection from the database."""

    #     try:
    #         data = self.real_time_firebase.get(self.DATABASE_URL, name_collection, 100)
    #         return data
    #     except requests.exceptions.ConnectionError:
    #         return False

    def get_data(self):
        
        try:
            data = self.firebase_.get("USERDATA", '')
        except requests.exceptions.ConnectionError:
            return None
        return data 