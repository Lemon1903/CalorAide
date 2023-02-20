"""_module summary_"""

from kivy.clock import mainthread
from kivymd.uix.snackbar import Snackbar

from View.base_screen import BaseScreenView


class LoginScreenView(BaseScreenView):
    """The view that handles UI for login screen."""

    @mainthread
    def model_is_changed(self) -> None:
        """Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        self.loading_view.dismiss()
        if self.model.is_account_exist:
            if not self.model.is_password_correct:
                self.show_error_snackbar("The password you have entered is incorrect.")
            else:
                next_screen = "home screen" if self.model.has_account else "register screen"
                self.reset_status()
                self.change_screen("left", next_screen)
        else:
            self.show_error_snackbar("Account does not exist!")
        self.controller.reset_is_account_exist()

    # TODO: can be moved to helpers
    def get_user_input(self):
        """A method that stores the user input from the text fields (username and password)."""
        return [self.ids.textfield_username.text, self.ids.textfield_password.text]

    # TODO: can be moved to helpers
    def reset_status(self):
        """A method that resets the error and required status of text field."""
        self.ids.textfield_username.required = False
        self.ids.textfield_username.error = False
        self.ids.textfield_password.required = False
        self.ids.textfield_password.error = False

    # TODO: can be moved in helpers
    def clear_text_fields(self):
        """A method that simply clear the text fields (username and password)."""
        self.ids.textfield_username.text = ""
        self.ids.textfield_password.text = ""

    # TODO: can be moved to helpers or change the representation of error
    def show_error_snackbar(self, error_text: str, color="#7B56BA"):
        """A method that show snackbar with a message that comes from its parameter."""
        Snackbar(
            text=error_text,
            bg_color=color,
            snackbar_x=30,
            snackbar_y=20,
            size_hint_x=0.95,
            pos_hint={"center_x": 0.5},
        ).open()

    def validate_user_input(self):
        """A method that show snackbar with different messages in different scenarios."""
        username, password = self.get_user_input()

        if not username and not password:
            self.show_error_snackbar("Please fill username and password")
        elif not username and password:
            self.show_error_snackbar("Please fill username")
        elif username and not password:
            self.show_error_snackbar("Please fill password")
        else:
            self.loading_view.open()
            self.controller.check_account_exist(username, password)

        self.clear_text_fields()
