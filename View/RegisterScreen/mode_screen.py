"""_module summary_"""

from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.snackbar import Snackbar

from Utils import helpers
from View.base_screen import BaseScreenView


class ModeScreenView(BaseScreenView):
    """The view that handles the Mode view part of the registration.
    Consists of three choices which are based on the user's calculated BMI.
    """

    user_mode = None
    chosen_button = None
    maintain_button = None
    modes_list = []

    def model_is_changed(self) -> None:
        """Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

    def on_enter(self, *args):
        self.bmi_amount_label()
        self.ids.bmi.text = self.set_category_label(self.controller.pull_database_bmi())
        self.getting_mode_list()
        self.disable_modes(self.controller.pull_database_bmi())

    def modify_mode_buttons(self, chosen_button):
        """Function that changes the colors of the buttons based on the one that was clicked."""
        for button in self.modes_list:
            if button == chosen_button:
                self.ids[chosen_button].md_bg_color = "#d58ceb"
            else:
                self.ids[button].md_bg_color = "#261a38"

    def getting_mode_list(self):
        """This function stores the list of the appropriate choices of modes."""
        self.modes_list = []
        modes_text = [self.ids.gain.text,
                      self.ids.maintain.text,
                      self.ids.lose.text]
        for i in modes_text:
            self.modes_list.append(i.lower())

    def disable_modes(self, category):
        """Determines which modes to disable based from the user's BMI.
        Removes the other choices from the list.
        """
        if category in ("Underweight", "Severely Underweight"):
            self.modes_list.remove('lose')
            self.modes_list.remove('maintain')
            self.ids.lose.disabled = True
            self.ids.maintain.disabled = True
        if category in ("Overweight", "Obese", "Severely Obese", "Morbidly Obese"):
            self.modes_list.remove('gain')
            self.modes_list.remove('maintain')
            self.ids.gain.disabled = True
            self.ids.maintain.disabled = True

    def confirm_mode(self):
        """Stores the 'chosen' mode of the user and passes it to the Controller."""
        if self.chosen_button:
            self.user_mode = self.chosen_button
            return self.user_mode

    def get_user_mode(self):
        """Takes the user's mode of choice from the Mode View."""
        self.controller.user_mode = self.confirm_mode()
        if not self.controller.user_mode:
            self.error_prompt("Select a mode before proceeding.")
        elif self.controller.user_mode == "maintain":
            self.finalize_maintain()
        else:
            self.controller.set_goal_screen()
            self.change_screen("left", "goal screen")

    def set_category_label(self, category):
        """Setting up the UI based on the inputs from the register screen."""
        category_label = f"""You are categorized as\n[b][color=#F3AAA0][size=19]{category.upper()}[/size][/color][b]"""
        return category_label

    def set_bmi_label(self, bmi):
        """Rounding off the BMI to two decimal places and showing it in the UI."""
        bmi_round_off = f"{bmi:.2f}"
        bmi_label = f"Your BMI is: [b][color=#F3AAA0]{bmi_round_off}[/color][b]"
        return bmi_label

    def finalize_maintain(self):
        """Pops-up only if the user chooses the "Maintain" mode.
        Confirming maintain will redirect the user to the home screen.
        """
        if not self.maintain_button:
            self.maintain_button = MDDialog(
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
        self.maintain_button.open()

    def bmi_amount_label(self):
        """Setting the UI of the Mode screen based on the inputs from the past screen"""
        self.ids.bmi_amount.text = self.set_bmi_label(self.controller.user_bmi_amount)

    def sedentary_mode(self, *args):
        """This function is called when the user finalizes their choice.
        This will be passed to the controller for the details to be compiled.
        """
        self.controller.set_to_sedentary()

    def dismiss_dialog(self, *args):
        """This function closes the dialog box when the user clicks CANCEL."""
        self.maintain_button.dismiss()

    def error_prompt(self, error_text: str, color="#7B56BA"):
        """Error prompt whenever there are no inputs."""
        Snackbar(text=error_text, bg_color=color).open()

    def change_screen(self, direction, next_screen):
        """Function that changes the view to the next desired screen."""
        self.manager.transition.direction = direction
        self.manager.current = next_screen
