"""_module summary_"""

# pylint: disable=no-name-in-module
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
        self.add_intake_dialog = None
        self.add_button = MDFillRoundFlatButton(
            text="Add",
            font_name="Poppins-SemiBold",
            on_release=self._open_add_intake_dialog,
        )
        self.history_button = MDFillRoundFlatButton(
            text="History",
            font_name="Poppins-SemiBold",
            on_release=lambda *_: print("History"),
        )
        self.delete_button = MDFillRoundFlatButton(
            text="Delete",
            font_name="Poppins-SemiBold",
            on_release=self._delete_intake_in_history,
        )

    def model_is_changed(self) -> None:
        """Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

    def on_check(self, *_):
        """Called when an intake history item is checked."""
        for intake_item in self.ids.intake_history.children:
            if intake_item.ids.checkbox.active:
                self._change_buttons([self.delete_button])
                return
        self._change_buttons([self.add_button, self.history_button])

    def _open_add_intake_dialog(self, *_):
        if not self.add_intake_dialog:
            self.add_intake_dialog = MDDialog(
                title="Add caloric goal",
                type="custom",
                content_cls=AddDialogContent(),
                elevation=2,
                buttons=[
                    MDFlatButton(
                        text="Confirm", on_release=self._validate_intake_input
                    ),
                    MDFlatButton(
                        text="Cancel", on_release=self._close_add_intake_dialog
                    ),
                ],
            )
        self.add_intake_dialog.open()

    def _validate_intake_input(self, *_):
        if self.add_intake_dialog:
            if self.add_intake_dialog.content_cls.has_empty_field():
                self.add_intake_dialog.content_cls.make_textfields_required()
            elif self.add_intake_dialog.content_cls.has_no_error():
                intake_input = self.add_intake_dialog.content_cls.get_input()
                self._add_intake_to_history(intake_input[1], float(intake_input[0]))

    def _close_add_intake_dialog(self, *_):
        if self.add_intake_dialog:
            self.add_intake_dialog.dismiss()
            self.add_intake_dialog.content_cls.clear_textfields()

    def _add_intake_to_history(self, food_name: str, calorie_amount: float):
        item = IntakeHistoryItem(
            view=self, food_name=food_name, calorie_amount=calorie_amount
        )
        self.ids.intake_history.add_widget(item)
        self.calorie_goal -= calorie_amount
        self._close_add_intake_dialog()

    def _delete_intake_in_history(self, *_):
        for intake_item in self.ids.intake_history.children[::-1]:
            if intake_item.ids.checkbox.active:
                self.calorie_goal += intake_item.calorie_amount
                self.ids.intake_history.remove_widget(intake_item)
        self._change_buttons([self.add_button, self.history_button])

    def _change_buttons(self, new_buttons: list[MDFillRoundFlatButton]):
        self.ids.buttons.clear_widgets()
        for button in new_buttons:
            button.size_hint_x = 1.0
            self.ids.buttons.add_widget(button)
        self.ids.buttons.size_hint_x = 0.3 * len(new_buttons)
