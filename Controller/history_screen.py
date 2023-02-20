"""_module summary_"""

from View import HistoryScreenView


class HistoryScreenController:
    """
    The `HistoryScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.main_screen.MainScreenModel
        self.views = [HistoryScreenView(controller=self, model=self.model)]

    def load_all_intake_history(self):
        """ Get data from history table through model. """
        self.model.load_all_intake_history()

    def get_views(self) -> list[HistoryScreenView]:
        """ Gets the view connected to this controller.

        Returns:
            HistoryScreenView: The view connected to this controller.
        """
        return self.views
