"""_module summary_"""

# pylint: disable=no-name-in-module
from kivy.clock import mainthread
from kivy.properties import StringProperty
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.snackbar import Snackbar

from View.base_screen import BaseScreenView


class GoalScreenView(BaseScreenView):
    """The View that handles the Goal part of the application.
    Consists of three choices which are the intensity of their goal.
    """

    user_mode = StringProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.user_goal = "Sedentary"
        self.finalization_dialog = MDDialog(
            text="Do you want to finalize?",
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
                    on_release=self.determine_goal
                ),
            ],
        )

    @mainthread
    def model_is_changed(self) -> None:
        """Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        self.loading_view.dismiss()
        self.controller.user_inputs.clear()
        self.change_screen("left", "home screen")

    def modify_goal_buttons(self, chosen_button, intensity: str):
        """This function stores the list for the goal choices."""
        self.user_goal = intensity
        for button in self.ids.modes_list.children:
            button.md_bg_color = "#d58ceb" if button == chosen_button else "#261a38"

    def show_finalize_dialog(self):
        """Pops-up the dialog box after clicking the FINALIZE button.
        This initializes compiles and finalizes all the data input by the user.
        """
        if self.user_goal == "Sedentary":
            self.error_prompt("You must choose one level of intensity.")
        else:
            self.finalization_dialog.open()

    def determine_goal(self, *_):
        """This function is called when the user finalizes their choice.
        This will be passed to the controller for the details to be compiled.
        """
        self.loading_view.open()
        self.dismiss_dialog()
        self.controller.compile_details("goal screen")

    def reset_button_state(self):
        """Reset button states."""
        self.user_goal = "Sedentary"
        for button in self.ids.modes_list.children:
            button.disabled = False
            button.md_bg_color = self.theme_cls.primary_color

    def dismiss_dialog(self, *_):
        """This function closes the dialog box when the user clicks CANCEL."""
        self.finalization_dialog.dismiss()

    def error_prompt(self, error_text: str, color="#7B56BA"):
        """Error prompt whenever there are no inputs."""
        Snackbar(text=error_text, bg_color=color).open()
