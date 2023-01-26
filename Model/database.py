"""_module summary_"""

from typing import Union

import requests
from firebase import firebase

class DataBase:
    """Your methods for working with the database should be implemented in this class."""
    def __init__(self):
        self.firebase_ = firebase.FirebaseApplication("https://fitrex-bfc21-default-rtdb.asia-southeast1.firebasedatabase.app/")
    
    #USERDATA is the Table
    def get_data(self):
        
        try:
            data = self.firebase_.get("USERDATA", '')
        except requests.exceptions.ConnectionError:
            return None
        return data 

    def create_table(self):
        self.data ={
            "Username" : "rae",
            "Password" : "try"
        }
        self.firebase_.post("https://fitrex-bfc21-default-rtdb.asia-southeast1.firebasedatabase.app/USERDATA", self.data)
    
    def add(self, userdata):
        self.data = {
            "Username": userdata[0],
            "Password": userdata[1]
        }
        self.firebase_.post("https://fitrex-bfc21-default-rtdb.asia-southeast1.firebasedatabase.app/USERDATA", self.data)
        print("posted")
        return()
