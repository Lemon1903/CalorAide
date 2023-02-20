"""_module summary_"""

from datetime import date

from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.snackbar import Snackbar

from View.base_screen import BaseScreenView
from View.HomeScreen.ProfileScreen.components import (ConfirmationDialog,
                                                      ConfirmationItem)


class RegisterScreenView(BaseScreenView):
    """The View that handles the registration part of the application.
    Consists of the text fields which collects the basic information of the user.
    """

    def __init__(self, **kw):
        super().__init__(**kw)
        self.user_age = 0
        self.activity_dialog = ConfirmationDialog(
            title="What's your Activity?",
            callback=self.set_activity,
            items=[
                ConfirmationItem(type="Sedentary", description="Little to no exercise"),
                ConfirmationItem(type="Light", description="Exercise 1-3 times/week"),
                ConfirmationItem(type="Moderate", description="Exercise 4-5 times/week"),
                ConfirmationItem(type="Active", description="Daily exercise or intense exercise 3-4 times/week"),
                ConfirmationItem(type="Very Active", description="Intense exercise 6-7 times/week"),
            ]
        )
        self.gender_dialog = ConfirmationDialog(
            title="What's your gender?",
            callback=self.set_gender,
            items=[
                ConfirmationItem(type="Male"),
                ConfirmationItem(type="Female"),
            ]
        )
        self.date_dialog = MDDatePicker(
            min_year = 1980, max_year = 2015, year=2003, month=1, day=1
        )
        self.date_dialog.bind(on_save=self.set_birthdate)

    def set_birthdate(self, *args):
        """Sets the birthdate textfield to the chosen birthdate."""
        user_birthdate = args[1]
        self.ids.birthdate.text = str(user_birthdate)
        self.user_age = int((date.today() - user_birthdate).days/365)
        self.date_dialog.dismiss()

    def set_gender(self, chosen_gender):
        """Sets the gender textfield to the chose gender."""
        self.ids.gender.text = chosen_gender
        self.gender_dialog.current_item = chosen_gender

    def set_activity(self, chosen_activity):
        """Sets the activity textfield to the chose activity."""
        self.ids.activity.text = chosen_activity
        self.activity_dialog.current_item = chosen_activity

    def validate_user_input(self):
        """Gets the values of all the text fields while validating if all the inputs
        were valid. If all were valid, this function moves the screen to the next.
        """
        if self._has_errors():
            self.error_prompt("Please check if there are invalid inputs.")
        else:
            self.controller.confirm_registration(self.get_user_inputs())
            self._clear_textfields()
            self.change_screen("left", "mode screen")

    def get_user_inputs(self):
        """Stores the user details into a list to be passed to the Controller."""
        return {
            "Name": self.ids.name.text,
            "Gender": self.ids.gender.text,
            "Height": float(self.ids.height.text),
            "Weight": float(self.ids.weight.text),
            "Age": self.user_age,
            "Activity": self.ids.activity.text,
        }

    def _clear_textfields(self):
        for textfield in self.ids.basic_info.children:
            textfield.text = ""
            textfield.error = False
            textfield.required = False

    # TODO: can be moved to helpers
    def _has_errors(self):
        """Returns `True` if any of the widgets' textfields are on_error or empty."""
        return any(tf.error or not tf.text for tf in self.ids.basic_info.children)

    # TODO: can be moved to helpers
    def error_prompt(self, error_text: str, color="#7B56BA"):
        """Prompt that pops-up whenever there is an error before proceeding."""
        Snackbar(
            text=error_text,
            bg_color=color,
            snackbar_x=30,
            snackbar_y=20,
            size_hint_x=0.95,
            pos_hint={"center_x": 0.5},
        ).open()
