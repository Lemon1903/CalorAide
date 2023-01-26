"""_module summary_"""
from kivy.clock import mainthread
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.dialog import MDDialog

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
        self.dialog = MDDialog(text = "Fill Username")
        self.dialog.open()
        return(self.dialog)
    def error_pass(self):
        self.dialog = MDDialog(text = "Fill Password")
        self.dialog.open()

    def error_conpass(self):
        self.dialog = MDDialog(text = "Re-type Password")
        self.dialog.open()

    def error_notmatch(self):
        self.dialog = MDDialog(text = "Password Do Not Match")
        self.dialog.open()

    def error_user_taken(self):
        self.dialog = MDDialog(text = "Username Already Taken")
        self.dialog.open()
        


    def model_is_changed(self) -> None:
        """Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

        self.dialog = MDDialog(text = "YEYYEYEYEYEYEYEYEY")
        self.dialog.open()
        # return(self.dialog)

        # gui na "sign up success"
        # goto reg screen
