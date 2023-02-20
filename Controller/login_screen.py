"""_module summary_"""

from View import LoginScreenView


class LoginScreenController:
    """
    The `LoginScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.login_screen.LoginScreenModel
        self.views = [LoginScreenView(controller=self, model=self.model)]

    def get_views(self) -> list[LoginScreenView]:
        """Gets the view connected to this controller.

        Returns:
            LoginScreenView: The view connected to this controller.
        """
        return self.views

    def check_account_exist(self, username: str, password: str):
        """Check if the account exist in the database."""
        self.model.is_account_taken(username, password)

    def reset_is_account_exist(self):
        """Resets the `is_account_exist` after checking."""
        self.model.reset_is_account_exist()
