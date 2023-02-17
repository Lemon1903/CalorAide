"""_module summary_"""

from kivy.clock import mainthread
from kivymd.uix.snackbar import Snackbar

from View.base_screen import BaseScreenView


class SignupScreenView(BaseScreenView):
    """_class summary_"""

    @mainthread
    def model_is_changed(self) -> None:
        """Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        self.change_screen("left", "login screen")
        self.loading_view.dismiss()

    def check_text_field(self):
        """Checks the input of the user."""
        user_input = self._get_user_input()

        if user_input[2] == "":
            self._show_error_snackbar("Fill Username")
        # TODO: make it asynch cheking if possible
        elif self.model.is_username_taken(user_input[2]):
            self._show_error_snackbar("Username Already Taken")
        elif user_input[1] == "":
            self._show_error_snackbar("Fill Password")
        elif user_input[0] == "":
            self._show_error_snackbar("Re-type Password")
        elif user_input[1] != user_input[0]:
            self._show_error_snackbar("Password Do Not Match")
        else:
            self.loading_view.open()
            self._clear_text_fields()
            self.controller.pass_data(user_input)

    # TODO: can be moved to helpers
    def _show_error_snackbar(self, error_text: str, color="#7B56BA"):
        """This function is called everytime an error has occured."""
        Snackbar(
            text=error_text,
            bg_color=color,
            snackbar_x=30,
            snackbar_y=20,
            size_hint_x=0.95,
            pos_hint={"center_x": 0.5},
        ).open()

    # TODO: can be moved to helpers
    def _get_user_input(self):
        """Stores users input."""
        return [textfield.text for textfield in self.ids.form_layout.children]

    # TODO: can be moved to helpers
    def _clear_text_fields(self):
        """Clear the textfields state."""
        for textfield in self.ids.form_layout.children:
            textfield.text = ""
            textfield.required = False
            textfield.error = False
