"""_module summary_"""

from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.snackbar import Snackbar

from View.base_screen import BaseScreenView


class GoalScreenView(BaseScreenView):
    """The View that handles the Goal part of the application.
    Consists of three choices which are the intensity of their goal.
    """

    chosen_button = None
    finalization_dialog = None

    def model_is_changed(self) -> None:
        """Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

    def show_goal_label(self, mode):
        """Setting up the label at the top of the Goal screen.
        Returns a string with markup."""
        goal_label = f"""Your mode is to\n[b][color=#F3AAA0][size=19]{mode.upper()} WEIGHT[/size][/color][b]"""
        return goal_label

    def modify_goal_buttons(self, chosen_button):
        """This function stores the list for the goal choices."""
        # self.modes_list = self.controller.
        goals = ["standard", "mild", "extreme"]
        for goal in goals:
            if goal == chosen_button:
                self.ids[chosen_button].md_bg_color = "#d58ceb"
            else:
                self.ids[goal].md_bg_color = "#261a38"

    def show_finalize_dialog(self):
        """Pops-up the dialog box after clicking the FINALIZE button.
        This initializes compiles and finalizes all the data input by the user.
        """
        if self.chosen_button is None:
            self.error_prompt("You must choose one level of intensity.")
            return
        if not self.finalization_dialog:
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
        self.finalization_dialog.open()

    def dismiss_dialog(self, *args):
        """This function closes the dialog box when the user clicks CANCEL."""
        self.finalization_dialog.dismiss()

    def error_prompt(self, error_text: str, color="#7B56BA"):
        """Error prompt whenever there are no inputs."""
        Snackbar(text=error_text, bg_color=color).open()

    def determine_goal(self, *args):
        """This function is called when the user finalizes their choice.
        This will be passed to the controller for the details to be compiled.
        """
        self.controller.get_user_goal()
