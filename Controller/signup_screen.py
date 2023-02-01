"""_module summary_"""
import importlib

import View.SignupScreen.signup_screen
from View import SignupScreenView

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.SignupScreen.signup_screen)


class SignupScreenController:
    """
    The `SignupScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.signup_screen.SignupScreenModel
        self.views = [SignupScreenView(self, self.model)]

    def check_text_field(self):  # bind sa kv file
        """
        Checks the input of the user.
        """
        user_input = self.views[0].get_user_input()

        if user_input[0] == "":
            self.views[0].show_error_snackbar("Fill Username")

        elif self.model.is_username_taken(user_input[0]):
            self.views[0].show_error_snackbar("Username Already Taken")

        elif user_input[1] == "":
            self.views[0].show_error_snackbar("Fill Password")

        elif user_input[2] == "":
            self.views[0].show_error_snackbar("Re-type Password")

        elif user_input[1] != user_input[2]:
            self.views[0].show_error_snackbar("Password Do Not Match")

        else:
            self._pass_data(user_input)

    def _pass_data(self, user_input: list[str]):
        """
        Pass the user input to a function in model called `to_database`.
        Calls the functions `disable_confirm_button` and `clear_text_field` from SignupScreenView.
        """
        self.model.to_database(user_input)
        self.views[0].disable_confirm_button()
        self.views[0].clear_text_fields()

    def get_views(self) -> list[SignupScreenView]:
        """Gets the view connected to this controller.

        Returns:
            SignupScreenView: The view connected to this controller.
        """
        return self.views
