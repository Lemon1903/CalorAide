"""_module summary_"""

from View import SignupScreenView


class SignupScreenController:
    """
    The `SignupScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.signup_screen.SignupScreenModel
        self.views = [SignupScreenView(controller=self, model=self.model)]

    def pass_data(self, user_input: list[str]):
        """Pass the user input to a function in model called `to_database`."""
        self.model.to_database(user_input)

    def get_views(self) -> list[SignupScreenView]:
        """Gets the view connected to this controller.

        Returns:
            SignupScreenView: The view connected to this controller.
        """
        return self.views
