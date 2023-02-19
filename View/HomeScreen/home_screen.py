"""_module summary_"""

from kivymd.uix.button import MDFlatButton
from kivymd.uix.snackbar import Snackbar

from View.base_screen import BaseScreenView


class HomeScreenView(BaseScreenView):
    """ The view that handles UI for profile screen. """

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

    def on_enter(self, *_):
        self.controller.load_user_data()
