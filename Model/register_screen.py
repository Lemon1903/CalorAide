"""_module summary_"""

import multitasking

from Model.base_model import BaseScreenModel

multitasking.set_max_threads(10)


class RegisterScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.RegisterScreen.Register_screen.RegisterScreenView` class.
    """

    def __init__(self, database):
        # Just an example of the data. Use your own values.
        self._data = None
        self.database = database

    @property
    def data(self):
        """_data summary_

        Returns:
            _type_: _description_
        """
        return self._data

    @data.setter
    def data(self, value):
        # We notify the View -
        # :class:`~View.RegisterScreen.profile_screen.RegisterScreenView` about the
        # changes that have occurred in the data model.
        self._data = value
        self.notify_observers("register screen")

    @multitasking.task
    def check_data(self):
        """Just an example of the method. Use your own code."""
        self.data = ["example item"]

    def get_user_info(self, info_list):
        """This function receives the user's information list from the Controller.
        It will then store each value into a dictionary and call a model function to pass
            it to the Database.
        """
        user_info = info_list
        info_dict = {
            "Name": user_info[0],
            "Age": user_info[1],
            "Height": user_info[2],
            "Weight": user_info[3],
            "Gender": user_info[4],
            "Activity": user_info[5],
            "BMI": user_info[6],
            "Mode": user_info[7],
            "Intensity": user_info[8],
            "Calorie Goal": user_info[9],
            "BMR": user_info[10],
        }
        self.database.update_user_data(info_dict, "UserInfo")

    def push_bmi(self, bmi):
        self.database.bmi = bmi

    def pull_bmi(self):
        return self.database.bmi
