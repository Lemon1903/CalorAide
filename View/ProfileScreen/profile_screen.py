"""_module summary_"""

from View.base_screen import BaseScreenView


class ProfileScreenView(BaseScreenView):
    """The view that handles UI for profile screen."""

    def model_is_changed(self) -> None:
        """Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
