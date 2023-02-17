"""_module summary_"""

# pylint: disable=no-name-in-module
from kivy.clock import mainthread
from kivy.properties import StringProperty

from View.base_screen import BaseScreenView

from .components import ActivityDialog


class ProfileScreenView(BaseScreenView):
    """The view that handles UI for profile screen."""

    current_activity = StringProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.activity_dialog = ActivityDialog(self)

    @mainthread
    def model_is_changed(self) -> None:
        """Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        if self.model.updated_profile_part == "activity":
            self.current_activity = self.model.user_profile_data["Activity"].upper()
        elif self.model.updated_profile_part == "general information":
            self.update_general_information_card(self.model.user_profile_data)
        self.model.has_loaded_profile = True

    def update_general_information_card(self, profile_data: dict):
        """Updates the general information card UI about the changes in data."""
        if profile_data:
            self.current_activity = self.model.user_profile_data["Activity"].upper()
            self.activity_dialog.current_activity = self.model.user_profile_data["Activity"]
            self.ids.general_info.profile_layout.update_profile_information(profile_data)
            if self.model.has_loaded_profile:
                self.ids.general_info.change_layout()
            self.controller.hide_connection_error()
        else:
            self.controller.show_connection_error()
