"""_module summary_"""

from kivymd.uix.snackbar import Snackbar

from View.base_screen import BaseScreenView


class LoginScreenView(BaseScreenView):
    """The view that handles UI for profile screen."""

    def model_is_changed(self) -> None:
        """Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
    def store_input(self): 
        return ([self.ids.textfield_username.text, self.ids.textfield_password.text])

    def reset_status(self):
        if self.ids.textfield_username.required == True:
            self.ids.textfield_username.required = False
            self.ids.textfield_password.required = False

    def clear_text_fields(self):
        self.ids.textfield_username.text = ""
        self.ids.textfield_password.text = ""
    
    def show_error_snackbar(self, error_text: str, color="#7B56BA"):
        Snackbar(text=error_text, bg_color=color).open()

    def show_errors_snackbar(self): 
        if self.ids.textfield_username.text == '' and self.ids.textfield_password.text == '': 
            self.show_error_snackbar("Please fill username and password")
        elif self.ids.textfield_username.text == '' and not self.ids.textfield_password.text == '':
            self.show_error_snackbar("Please fill username")
        elif not self.ids.textfield_username.text == '' and self.ids.textfield_password.text == '':
            self.show_error_snackbar("Please fill password")
        else:
            self.show_error_snackbar("Account does not exist!")
            
        