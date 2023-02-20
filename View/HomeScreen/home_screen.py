"""_module summary_"""

from kivymd.uix.button import MDFlatButton
from kivymd.uix.snackbar import Snackbar

from View.base_screen import BaseScreenView


class HomeScreenView(BaseScreenView):
    """The view that handles UI for profile screen."""

    def __init__(self, **kw):
        super().__init__(**kw)
        self.connection_error_snackbar = Snackbar(
            text="Connection error",
            snackbar_x="10dp",
            snackbar_y="100dp",
            size_hint_x=0.90,
            pos_hint={"center_x": 0.5},
            auto_dismiss=False,
            buttons=[
                MDFlatButton(
                    text="Retry",
                    text_color=(1, 1, 1, 1),
                    on_release=lambda _: self.controller.load_user_data(True),
                )
            ],
        )

    def on_pre_enter(self, *_):
        self.ids.profile_screen.ids.scroll_view.scroll_y = 1

    def on_enter(self, *_):    
        self.controller.load_user_data()

    def on_logout(self):
        """When user logs out."""
        # clears the username in the local txt file
        with open("Model/username.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()

        lines[0] = ' ' + '\n'

        with open("Model/username.txt", "w", encoding="utf-8") as file:
            file.writelines(lines)
        self.ids.profile_screen.on_logout()
        self.ids.calorie_screen.on_logout()
        self.change_screen("right", "login screen")

    def get_graph2_date(self):
        """Gets the currently shown date in graph2 card."""
        return self.ids.profile_screen.database_date

    def set_user_mode(self, mode: str):
        """Sets the calorie counter screen mode."""
        self.ids.calorie_screen.user_mode = mode.upper()
