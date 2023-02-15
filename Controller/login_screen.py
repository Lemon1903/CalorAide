"""_module summary_"""
import importlib

import View.LoginScreen.login_screen
from View import LoginScreenView

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.LoginScreen.login_screen)


class LoginScreenController:
    """
    The `LoginScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.login_screen.LoginScreenModel
        self.views = [LoginScreenView(self, self.model)]


    def get_views(self) -> list[LoginScreenView]:
        """Gets the view connected to this controller.

        Returns:
            LoginScreenView: The view connected to this controller.
        """
        return self.views

    # def check_account_reset_clear(self):
    #     """ A method that checks if account exists and resets the status of the text fields. """
    #     username, password = self.views[0].store_user_input()
    #     if self.model.is_account_taken(username, password):
    #         self.views[0].reset_status()
    #     else:
    #         self.views[0].show_errors_snackbar()
    #     self.views[0].clear_text_fields()

    # def check_account_reset(self):
    #     """A method that replicates the is_account_taken from the Model but it has a condition that if an account exists it should reset the status of the text field"""
    #     username, password = self.views[0].store_user_input()
    #     if self.model.is_account_taken(username, password):
    #         self.views[0].reset_status()
    #         return True
    #     return False
    