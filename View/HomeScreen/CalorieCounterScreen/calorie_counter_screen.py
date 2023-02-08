"""_module summary_"""

# pylint: disable=no-name-in-module
from kivy.clock import mainthread
from kivy.properties import NumericProperty
from kivymd.uix.button import MDFillRoundFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog

from View.base_screen import BaseScreenView

from .components import AddDialogContent, IntakeHistoryItem


class CalorieCounterScreenView(BaseScreenView):
    """The view that handles UI for calorie counter screen."""

    calorie_goal = NumericProperty(1900.0)

    def __init__(self, **kw):
        super().__init__(**kw)
        self.add_intake_dialog = MDDialog(
            title="Add caloric goal",
            type="custom",
            content_cls=AddDialogContent(),
            elevation=2,
            buttons=[
                MDFlatButton(text="Confirm", on_release=self._validate_intake_input),
                MDFlatButton(text="Cancel", on_release=self._close_add_intake_dialog),
            ],
        )
        self.add_button = MDFillRoundFlatButton(
            text="Add",
            font_name="Poppins-SemiBold",
            on_release=self.add_intake_dialog.open,
        )
        self.history_button = MDFillRoundFlatButton(
            text="History",
            font_name="Poppins-SemiBold",
            on_release=lambda *_: print("History"),
        )
        self.delete_button = MDFillRoundFlatButton(
            text="Delete",
            font_name="Poppins-SemiBold",
            on_release=lambda _: self.controller.delete_intake_to_database(
                self, self.calorie_goal
            ),
        )

    @mainthread
    def model_is_changed(self) -> None:
        """Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        if not self.model.user_intake_data:
            self.controller.show_connection_error()
        else:
            {
                "intake history": self._load_intake_history,
                "intake history add": self._add_intake_to_history,
                "intake history delete": self._delete_intake_in_history,
            }[self.model.updated_calorie_part](self.model.user_intake_data)

        self.calorie_goal = self.model.new_calorie_goal
        self.controller.has_loaded_calorie_counter = True
        self.controller.reset_calorie_counter_data()

    def on_check(self, *_):
        """Called when an intake history item is checked."""
        for intake_item in self.ids.intake_history.children:
            if intake_item.ids.checkbox.active:
                self._change_buttons([self.delete_button])
                return
        self._change_buttons([self.add_button, self.history_button])

    def get_checked_items(self):
        """Gets all the items with checkbox active."""
        return [
            intake_item
            for intake_item in self.ids.intake_history.children
            if intake_item.ids.checkbox.active
        ]

    def _load_intake_history(self, intake_history: dict | None):
        if intake_history:
            for intake_data in list(intake_history.items())[:-1]:
                self._add_intake_to_history(intake_data)

    def _validate_intake_input(self, *_):
        if self.add_intake_dialog:
            if self.add_intake_dialog.content_cls.has_empty_field():
                self.add_intake_dialog.content_cls.make_textfields_required()
            elif self.add_intake_dialog.content_cls.has_no_error():
                intake_input = self.add_intake_dialog.content_cls.get_input()
                self.controller.add_intake_to_database(intake_input, self.calorie_goal)

    def _close_add_intake_dialog(self, *_):
        if self.add_intake_dialog.parent:
            self.add_intake_dialog.dismiss()
            self.add_intake_dialog.content_cls.clear_textfields()

    def _add_intake_to_history(self, added_intake: tuple):
        intake_uuid, intake_item = added_intake
        item = IntakeHistoryItem(
            callback=self.on_check,
            identifier=intake_uuid,
            food_name=intake_item["Food"],
            calorie_amount=intake_item["Calorie Amount"],
        )
        self.ids.intake_history.add_widget(item, len(self.ids.intake_history.children))
        self._close_add_intake_dialog()

    def _delete_intake_in_history(self, delete_list: list):
        for delete_item in delete_list:
            self.ids.intake_history.remove_widget(delete_item)
        self._change_buttons([self.add_button, self.history_button])

    def _change_buttons(self, new_buttons: list[MDFillRoundFlatButton]):
        self.ids.buttons.clear_widgets()
        for button in new_buttons:
            button.size_hint_x = 1.0
            self.ids.buttons.add_widget(button)
        self.ids.buttons.size_hint_x = 0.3 * len(new_buttons)
