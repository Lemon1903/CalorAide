"""This module contains the custom Activity Dialog class."""

# pylint: disable=no-name-in-module
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import ListProperty, ObjectProperty, StringProperty
from kivymd.material_resources import DEVICE_TYPE
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import BaseDialog


class ConfirmationDialog(BaseDialog):
    """Custom Dialog for picking a new activity."""

    title = StringProperty()
    current_item = StringProperty()
    items = ListProperty()
    callback = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_item = self.items[0].type
        self.selected_item = self.current_item
        self.radius = [dp(10), dp(10), dp(10), dp(10)]
        self.size_hint = (None, None)

        # adjust the width according to the device
        if DEVICE_TYPE in ("desktop", "tablet"):
            self.width = min(dp(560), Window.width - dp(50))
        elif DEVICE_TYPE == "mobile":
            self.width = min(dp(280), Window.width - dp(50))

        for item in self.items:
            self.ids.confirmation_items.add_widget(item, 1)
            item.parent = self

    def on_pre_open(self):
        """Called before opening the dialog."""
        for confirm_item in self.ids.confirmation_items.children:
            if (
                isinstance(confirm_item, ConfirmationItem)
                and confirm_item.type == self.current_item
            ):
                confirm_item.ids.checkbox.active = True


class ConfirmationItem(MDBoxLayout):
    """Activity Dialog checkbox items."""

    type = StringProperty()
    description = StringProperty()

    def _on_active(self, instance_checkbox, value: bool):
        """Called when an `ActivityItem` checkbox is clicked."""
        if value:
            self.ids.description.opacity = 1.0
            self.ids.description.height = self.ids.description.texture_size[1]
            self.parent.selected_item = self.type
        else:
            self.ids.description.opacity = 0.0
            self.ids.description.height = 0
        instance_checkbox.disabled = value
