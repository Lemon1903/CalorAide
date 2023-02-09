"""_module summary_"""

from typing import Union

import requests
from firebase import firebase


class DataBase:
    """Your methods for working with the database should be implemented in this class."""

    def __init__(self):
        self.firebase_ = firebase.FirebaseApplication(
            "https://fitrex-bfc21-default-rtdb.asia-southeast1.firebasedatabase.app/"
        )

    # USERDATA is the Table
    def get_data_table(self):
        """Returns data from database."""
        try:
            data = self.firebase_.get("USERDATA", '')
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
        self.firebase_.post("https://fitrex-bfc21-default-rtdb.asia-southeast1.firebasedatabase.app/USERDATA", self.data)

    def add(self, userdata):
        self.data = {
            "Username": userdata[0],
            "Password": userdata[1],
        }
        self.firebase_.post("https://fitrex-bfc21-default-rtdb.asia-southeast1.firebasedatabase.app/USERDATA", self.data)
        print("Posted!")

        return()

    def add_info(self, userinfo):
        # self.firebase_.put("USERDATA/Taylor/UserInfo",
        #                      {"Name": userinfo[0]},
        #                      {"Age": userinfo[1]},
        #                      {"Height": userinfo[2]},
        #                      {"Gender": userinfo[3]},
        #                      {"Weight": userinfo[4]},
        #                      {"BMI": userinfo[5]},
        #                      {"BMR": userinfo[6]},
        #                      {"Category": userinfo[7]},
        #                      {"Mode": userinfo[8]},
        #                      {"Goal": userinfo[9]},
        #                      )
        self.info = {
            "Name": userinfo[0],
            "Age": userinfo[1],
            "Height": userinfo[2],
            "Weight": userinfo[3],
            "Gender": userinfo[4],
            "BMI": userinfo[5],
            "BMR": userinfo[6],
            "Category": userinfo[7],
            "Mode": userinfo[8],
            "Activity": userinfo[9],

        }
        self.firebase_.put("USERDATA/Sabrina", "UserInfo", self.info)
        print("haha")

    def add_user_data(self, user_input):
        """Adds userdata to database."""
        try:
            data = {"Password": user_input[1]}
            self.firebase_.put(
                f"USERDATA/{user_input[2]}", "UserInfo", data, connection=None
            )
            return True
        except requests.exceptions.ConnectionError:
            return False
