"""_module summary_"""
from kivy.clock import mainthread
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineListItem
from .components import IntakeHistoryItem
from Utils import helpers

from View.base_screen import BaseScreenView


class HistoryScreenView(BaseScreenView):

    def __init__(self, controller, model, **kw):
        super().__init__(controller, model, **kw)
    
    def on_pre_enter(self):
        """ Loads everything on the screen """

        self.data = self.controller.get_data_from_model()

        for key,value in reversed(list(self.data.items())):
            self.date = self.get_dates(key)
            self.ids.lists.add_widget(MDLabel(text =self.date,
                pos_hint={"center_y": 0.1},
                size_hint_x= 0.5,
                font_name = "Poppins-Regular",
                opacity = 0.5))

            for inner_key, inner_value in value.items():
                if inner_key != "Calorie Goal":
                    self.item = IntakeHistoryItem(
                        food_name = inner_value["Food"],
                        calorie_amount = inner_value["Calorie Amount"]
                    )
                    self.ids.lists.add_widget(self.item)

            self.ids.lists.add_widget(OneLineListItem(text = "",
                divider= None))


    def back_btn(self):
        """ Change the Screen when back button is pressed, for now """

        self.change_screen("left", "login screen")
    
    def on_leave(self):
        """ Remove widgets when you exit the screen """

        self.ids.lists.clear_widgets()

    def get_dates(self, date):
        """ Function to get the dates and  convert to texts """

        date_today = helpers.get_date_today()
        yesterday = helpers.get_date_yesterday()
        another_days = helpers.get_date_in_text()
        if date == date_today:
            date= "Today"
        elif date == yesterday:
            date = "Yesterday"
        else: 
            date = another_days
        return date


    def model_is_changed(self) -> None:
        """Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
