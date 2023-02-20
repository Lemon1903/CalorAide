"""_module summary_"""

from datetime import date

from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.snackbar import Snackbar

from View.base_screen import BaseScreenView


class RegisterScreenView(BaseScreenView):
    """The View that handles the registration part of the application.
    Consists of the text fields which collects the basic information of the user.
    """

    def __init__(self, **kw):
        super().__init__(**kw)
        self.user_age = 0
        gender_menu_list = [
            {
                "viewclass": "OneLineListItem",
                "text": gender,
                "on_release": lambda x=gender: self.set_gender(x),
            } for gender in ("Male", "Female")
        ]
        activity_menu_list = [
            {
                "viewclass": "OneLineListItem",
                "text": activity,
                "on_release": lambda x=activity: self.set_activity(x),
            } for activity in ("Sedentary", "Light", "Moderate", "Active", "Very Active")
        ]
        self.gender_menu = MDDropdownMenu(
            background_color=self.theme_cls.primary_dark,
            caller=self.ids.gender,
            items=gender_menu_list,
            position="bottom",
            max_height="100dp",
            width_mult=2,
        )
        self.activity_menu = MDDropdownMenu(
            background_color=self.theme_cls.primary_dark,
            caller=self.ids.activity,
            items=activity_menu_list,
            position="bottom",
            max_height="150dp",
            width_mult=2,
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
        self.gender_menu.dismiss()

    def set_activity(self, chosen_activity):
        """Sets the activity textfield to the chose activity."""
        self.ids.activity.text = chosen_activity
        self.activity_menu.dismiss()

    def validate_user_input(self):
        """Gets the values of all the text fields while validating if all the inputs
        were valid. If all were valid, this function moves the screen to the next.
        """
        if self._has_errors():
            self.error_prompt()
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
    def error_prompt(self, color="#7B56BA"):
        """Prompt that pops-up whenever there is an error before proceeding."""
        Snackbar(text="Please check if there are invalid inputs.", bg_color=color).open()