"""_module summary_"""

# pylint: disable=no-name-in-module
from kivy.properties import NumericProperty, StringProperty
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.snackbar import Snackbar

from View.base_screen import BaseScreenView


class ModeScreenView(BaseScreenView):
    """The view that handles the Mode view part of the registration.
    Consists of three choices which are based on the user's calculated BMI.
    """

    user_bmi_amount = NumericProperty()
    user_bmi = StringProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.user_mode = ""
        self.maintain_dialog = MDDialog(
            text="Are you sure you want to maintain your weight? This mode will use default calculations only.",
            buttons=[
                MDFlatButton(
                    text="CANCEL",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.dismiss_dialog
                ),
                MDRaisedButton(
                    text="YES",
                    theme_text_color="Custom",
                    text_color="white",
                    on_release=self.sedentary_mode
                ),
            ],
        )

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        self.loading_view.dismiss()
        # self.change_screen("left", "home screen")

    def on_enter(self, *_):
        self.user_bmi_amount = self.controller.get_database_bmi_value()
        self.user_bmi = self.controller.get_database_bmi().upper()
        self.disable_modes(self.user_bmi)

    def modify_mode_buttons(self, chosen_button):
        """Function that changes the colors of the buttons based on the one that was clicked."""
        self.user_mode = chosen_button.text.title()
        for button in self.ids.modes_list.children:
            if not button.disabled:
                button.md_bg_color = "#d58ceb" if button == chosen_button else "#261a38"

    def disable_modes(self, category: str):
        """
        Determines which modes to disable based from the user's BMI.
        Removes the other choices from the list.
        """
        if category in ("UNDERWEIGHT", "SEVERELY UNDERWEIGHT"):
            self.ids.lose.disabled = True
            self.ids.maintain.disabled = True
        elif category in ("OVERWEIGHT", "OBESE", "SEVERELY OBESE", "MORBIDLY OBESE"):
            self.ids.gain.disabled = True
            self.ids.maintain.disabled = True

    def get_user_mode(self):
        """Takes the user's mode of choice from the Mode View."""
        if not self.user_mode:
            self.error_prompt("Select a mode before proceeding.")
        elif self.user_mode == "Maintain":
            self.maintain_dialog.open()
        else:
            self.controller.set_goal_screen(self.user_mode.upper())
            self.change_screen("left", "goal screen")

    def sedentary_mode(self, *_):
        """
        This sets the intensity to default as sedentary.
        Redirects the screen to the home screen.
        """
        self.loading_view.open()
        self.dismiss_dialog()
        self.controller.compile_details("mode screen")

    def dismiss_dialog(self, *_):
        """This function closes the dialog box when the user clicks CANCEL."""
        self.maintain_dialog.dismiss()

    # TODO: can be moved to helpers
    def error_prompt(self, error_text: str, color="#7B56BA"):
        """Error prompt whenever there are no inputs."""
        Snackbar(text=error_text, bg_color=color).open()
