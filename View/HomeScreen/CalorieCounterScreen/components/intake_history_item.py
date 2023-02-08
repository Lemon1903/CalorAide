"""Module that holds the class for intake history item."""

# pylint: disable=no-name-in-module
from kivy.properties import NumericProperty, StringProperty
from kivymd.uix.boxlayout import MDBoxLayout


class IntakeHistoryItem(MDBoxLayout):
    """Represents the items in the intake history."""

    food_name = StringProperty()
    calorie_amount = NumericProperty()
    identifier = NumericProperty()

    def __init__(self, callback, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.on_check_callback = callback
