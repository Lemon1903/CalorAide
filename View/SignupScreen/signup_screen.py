"""_module summary_"""
from kivy.clock import mainthread
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.snackbar import Snackbar
from View.base_screen import BaseScreenView



class SignupScreenView(BaseScreenView):
    """I just showed an example loading spinner while doing an extensive calculations

    Args:
        BaseScreenView (_type_): _description_
    """

    def __init__(self, controller, model, **kw):
        super().__init__(controller, model, **kw)
        pass

    def get_userdata(self): 
       return ( [self.ids.user.text, self.ids.passw.text, self.ids.conpass.text])

    def error_user(self):
        return(Snackbar(text = "Fill Username", bg_color = "#7B56BA").open())

    def error_pass(self):
        return(Snackbar(text = "Fill Password", bg_color = "#7B56BA").open())

    def error_conpass(self):
        return(Snackbar(text = "Re-type Password", bg_color = "#7B56BA").open())

    def error_notmatch(self):
        return(Snackbar(text = "Password Do Not Match", bg_color = "#7B56BA").open())

    def error_user_taken(self):
        return(Snackbar(text = "Username Already Taken", bg_color = "#7B56BA").open())
        


    def model_is_changed(self) -> None:
        """Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """



