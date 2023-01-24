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
        self.view = SignupScreenView(self, self.model)

    # @multitasking.task
    # def do_extensive_calculations(self):
    #     self.view.show_loading()
    #     print("doing some extensive calculations...")
    #     time.sleep(5)
        # self.view.close_loading()

    def get_view(self) -> SignupScreenView:
        """Gets the view connected to this controller.

        Returns:
            SignupScreenView: The view connected to this controller.
        """
        return self.view
