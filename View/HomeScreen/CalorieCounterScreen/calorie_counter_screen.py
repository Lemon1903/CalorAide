"""_module summary_"""

from kivy.clock import Clock

from View.base_screen import BaseScreenView


class CalorieCounterScreenView(BaseScreenView):
    """The view that handles UI for calorie counter screen."""

    def model_is_changed(self) -> None:
        """Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
