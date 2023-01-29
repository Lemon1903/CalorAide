"""_module summary_"""
import importlib
import time

import multitasking

import View.SignupScreen.signup_screen
from View import SignupScreenView


# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.SignupScreen.signup_screen)


class SignupScreenController:
    """
    The `MainScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.main_screen.MainScreenModel
        self.views = [SignupScreenView(self, self.model)]

    def clear_txt_field(self):
        self.views[0].ids.user.text = ""
        self.views[0].ids.passw.text = ""
        self.views[0].ids.conpass.text = ""

    def disabled_btn(self):
        if self.views[0].ids.btn.disabled == False:
            self.views[0].ids.btn.disabled =True
    
    def pass_data(self):
        self.userdata = self.views[0].get_userdata()
        self.model.to_database(self.userdata)

    def check_clr_disable(self):
        self.pass_data()
        self.disabled_btn()
        self.clear_txt_field()

    def check_txt_field(self):  #bind sa kv file
        self.usern = self.username_check()

        if self.views[0].ids.user.text == "":
            print("Fill Username")
            self.views[0].error_user()

        elif self.views[0].ids.user.text == self.usern:
            print("username taken")
            self.views[0].error_user_taken()

        elif self.views[0].ids.passw.text == "":
            print("Fill Password")
            self.views[0].error_pass()

        elif self.views[0].ids.conpass.text == "":
            print("Re-type Password")
            self.views[0].error_conpass()

        elif self.views[0].ids.passw.text != self.views[0].ids.conpass.text:
            print("Password Do not Match")
            self.views[0].error_notmatch()

        else:
            self.check_clr_disable()
    
    def username_check(self):
        self.userdata = self.views[0].get_userdata()
        self.name = self.model.check_username(self.userdata)
        return(self.name)

    def get_views(self) -> list[SignupScreenView]:
        """Gets the view connected to this controller.

        Returns:
            SignupScreenView: The view connected to this controller.
        """
        return self.views



