"""_module summary_"""

from kivy.clock import mainthread
from kivymd.uix.snackbar import Snackbar

from View.base_screen import BaseScreenView


class ProfileScreenView(BaseScreenView):
    """The view that handles UI for profile screen."""

    def __init__(self, **kw):
        super().__init__(**kw)
        self.profile_parts = {
            "general information": self.update_general_information_card,
        }

    @mainthread
    def update_general_information_card(self):
        """Updates the general information card UI about the changes of data."""
        if self.model.user_data is None:
            Snackbar(
                text="Connection error",
                snackbar_x="10dp",
                snackbar_y="100dp",
                size_hint_x=0.90,
                pos_hint={"center_x": 0.5},
            ).open()
        else:
            self.ids.general_info.profile_layout.update_profile_information(self.model.user_data)

        if self.controller.has_loaded_profile:
            self.ids.general_info.change_layout()

        self.controller.has_loaded_profile = True
        self.controller.reset_user_data()

    def model_is_changed(self) -> None:
        """Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        self.profile_parts[self.model.updated_part]()
