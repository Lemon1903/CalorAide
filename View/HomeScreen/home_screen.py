"""_module summary_"""

from kivy.clock import mainthread

from View.base_screen import BaseScreenView


class HomeScreenView(BaseScreenView):
    """The view that handles UI for profile screen."""

    def on_enter(self, *_):
        self.controller.load_profile_data()

    @mainthread
    def model_is_changed(self) -> None:
        """Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        # if not self.loading_view.parent:
        #     self.loading_view.open()
        # else:
        #     self.loading_view.dismiss()
