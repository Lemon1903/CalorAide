"""Module that holds the class for intake history item."""

# pylint: disable=no-name-in-module
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivymd.uix.boxlayout import MDBoxLayout


class HistoryItem(RectangularRippleBehavior, ButtonBehavior, MDBoxLayout):
    """Represents the items in the intake history."""

    food_name = StringProperty()
    calorie_amount = NumericProperty()
    identifier = NumericProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ripple_alpha = 0.2
        self.ripple_duration_out = 0.15
        self.ripple_duration_in_fast = 0.15
        self.ripple_duration_in_slow = 0.15
        self.ripple_canvas_after = False
