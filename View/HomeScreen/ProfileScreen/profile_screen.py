"""_module summary_"""

from kivy.clock import mainthread

from View.base_screen import BaseScreenView


class ProfileScreenView(BaseScreenView):
    """The view that handles UI for profile screen."""

    def update_general_information_card(self, profile_data: dict):
        """Updates the general information card UI about the changes in data."""
        self.ids.general_info.profile_layout.update_profile_information(profile_data)

        if self.controller.has_loaded_profile:
            self.ids.general_info.change_layout()

    @mainthread
    def model_is_changed(self) -> None:
        """Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        if not self.model.user_profile_data:
            self.controller.show_connection_error()
        else:
            {"general information": self.update_general_information_card,}[
                self.model.updated_profile_part
            ](self.model.user_profile_data)

        self.controller.has_loaded_profile = True
        self.controller.reset_user_profile_data()
