"""_module summary_"""

from kivy.clock import mainthread
from kivy.uix.widget import Widget
from kivymd.uix.button import MDFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.snackbar import Snackbar

from Utils import helpers
from View.base_screen import BaseScreenView

from .components import HistoryItem


class HistoryScreenView(BaseScreenView):
    """ The view that handles UI for History Screen. """

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
        """ Loads everything on the screen. """
        self.loading_view.open()
        self.controller.load_all_intake_history()

    def on_leave(self, *_):
        """ Clears the list when leaving the screen. """
        self.ids.lists.clear_widgets()

    @mainthread
    def model_is_changed(self) -> None:
        """ Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        for date_, intake_data in reversed(list(self.model.all_intake_history.items())):
            formatted_date = self.format_date(date_)
            self.ids.lists.add_widget(
                MDLabel(
                    text=formatted_date,
                    font_name="Poppins-Regular",
                    font_size=18,
                    opacity=0.5,
                    height="15dp",
                    size_hint_y=None,
                )
            )

            for identifier, intake_item in intake_data.items():
                if identifier != "Calorie Goal":
                    item = HistoryItem(
                        food_name=intake_item["Food"],
                        calorie_amount=intake_item["Calorie Amount"]
                    )
                    self.ids.lists.add_widget(item)

            self.ids.lists.add_widget(Widget(height="30dp", size_hint_y=None))
        self.loading_view.dismiss()

    def format_date(self, date_):
        """ Function to get the dates and convert to texts. """
        if date_ == helpers.get_date_today():
            date_= "Today"
        elif date_ == helpers.get_date_yesterday():
            date_ = "Yesterday"
        return date_
