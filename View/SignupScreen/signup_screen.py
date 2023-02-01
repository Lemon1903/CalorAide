"""_module summary_"""

from kivymd.uix.snackbar import Snackbar

from View.base_screen import BaseScreenView


class SignupScreenView(BaseScreenView):
    """I just showed an example loading spinner while doing an extensive calculations

    Args:
        BaseScreenView (_type_): _description_
    """

    def get_user_input(self):
        """
        Stores users input.
        """
        return [
            self.ids.username.text,
            self.ids.password.text,
            self.ids.confirm_password.text,
        ]

    def clear_text_fields(self):
        """
        CLear the text fields.
        """
        for text_field in self.get_user_input():
            text_field.text = ""

    def disable_confirm_button(self):
        """
        Disable the confirm button.
        """
        if not self.ids.btn.disabled:
            self.ids.btn.disabled = True

    def show_error_snackbar(self, error_text: str, color="#7B56BA"):
        """
        This function is called everytime an error has occured.
        """
        Snackbar(text=error_text, bg_color=color).open()

    def model_is_changed(self) -> None:
        """Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
