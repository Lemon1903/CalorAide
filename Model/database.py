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

    # def create_table(self, userdata):
    #     self.data ={
    #         "Username" : "rae",
    #         "Password" : "try"
    #     }
    #     #self.firebase_.post("https://fitrex-bfc21-default-rtdb.asia-southeast1.firebasedatabase.app/USERDATA", self.data)
    #     self.firebase_.put("USERDATA", userdata[0], self.data)
    
    # def add(self, userdata):
    #     self.data = {
    #         "Username": userdata[0],
    #         "Password": userdata[1]
    #     }
    #     # self.firebase_.post("https://fitrex-bfc21-default-rtdb.asia-southeast1.firebasedatabase.app/USERDATA", self.data)
    #     self.firebase_.put("USERDATA", userdata[0], self.data)
    #     print("Posted!")

    #     return()
    
    # 2 pag ilalagay mo na sa github
    def create_table(self, userdata):
        self.info = {
            "Password": userdata[0],
            }
        # self.history = {"ano": "ehe"}
        # # self.datavis = {"hoy": "yeah"}

        self.firebase_.put(f"USERDATA/{userdata[0]}", "UserInfo", self.info)
        self.firebase_.put(f"USERDATA/{userdata[0]}", "History", self.history)
        self.firebase_.put(f"USERDATA/{userdata[0]}", "DataVis", "")
        self.firebase_.put("USERDATA/Sabrina", "UserInfo", self.info)
        return
    
    def get_history(self, table_name):
        """ Function to acces history table """
        history = self.firebase_.get(f"USERDATA/Lemon/", table_name)
        return history


