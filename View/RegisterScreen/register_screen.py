"""_module summary_"""

from datetime import datetime

from dateutil import relativedelta
from kivy.metrics import dp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.snackbar import Snackbar

from View.base_screen import BaseScreenView


class RegisterScreenView(BaseScreenView):
    """The View that handles the registration part of the application.
    Consists of the text fields which collects the basic information of the user.
    """

    user_name = None
    user_height = None
    user_weight = None
    user_gender = None
    user_age = None
    user_activity = None

    date_dialog = None
    gender_menu = None
    activity_menu = None

    def model_is_changed(self) -> None:
        """Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

    def get_user_details(self):
        """Gets the values of all the text fields while validating if all the inputs were valid.
        If all were valid, this function moves the screen to the next.
        """
        user_input_name = self.ids.name.text
        user_input_height = self.ids.height.text
        user_input_weight = self.ids.weight.text
        self.user_name = self.name_valid(user_input_name)
        self.user_height = self.measurement_valid(user_input_height)
        self.user_weight = self.measurement_valid(user_input_weight)
        all_inputs_valid = self.check_for_errors()

        if all_inputs_valid:
            self.controller.confirm_registration()

    def select_gender(self):
        """Opens up the pop-up menu for the Gender textfield.
        This returns the string of the chosen gender.
        """
        gender_menu_list = [{
                "viewclass": "OneLineListItem",
                "text": "Male",
                "on_release": lambda gender = "Male": self.set_gender(gender),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Female",
                "on_release": lambda gender = "Female": self.set_gender(gender),
            }]
        self.gender_menu = MDDropdownMenu(
            background_color=self.theme_cls.primary_dark,
            caller = self.ids.gender,
            items = gender_menu_list,
            position="center",
            max_height= dp(100),
            width_mult = 1.5,)
        self.gender_menu.open()

    def set_gender(self, user_gender):
        """Stores the gender string into a variable."""
        self.ids.gender.text = user_gender
        self.user_gender = self.menu_choice_valid(user_gender, "gender")
        self.gender_menu.dismiss()

    def show_date_picker(self):
        """Opens up the MDDatePicker Widget from the KivyMD Library."""
        self.date_dialog = MDDatePicker(
            min_year = 1980,
            max_year = 2015,
            year=2003, month=1, day=1
        )
        self.date_dialog.bind(on_save=self.set_birthdate, on_cancel=self.on_cancel)
        self.date_dialog.open()

    def set_birthdate(self, instance, value, date_range):
        """Stores the value of the birthdate inside a variable."""
        user_birthdate = value
        self.ids.birthdate.text = str(user_birthdate)
        self.user_age = self.birthdate_valid(user_birthdate)
        self.date_dialog.dismiss()

    def on_cancel(self, instance, value):
        """Closes the MDDatePicker pop-up menu after clicking the CANCEL button"""

    def select_activity(self):
        """Opens up the pop-up menu for the Activity textfield.
        This returns the string of the chosen activity level.
        """
        activity_menu_list = [{
                "viewclass": "OneLineListItem",
                "text": "Sedentary",
                "on_release": lambda x = "Sedentary": self.set_activity(x),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Light",
                "on_release": lambda x = "Light": self.set_activity(x),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Moderate",
                "on_release": lambda x = "Moderate": self.set_activity(x),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Active",
                "on_release": lambda x = "Active": self.set_activity(x),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Very Active",
                "on_release": lambda x = "Very Active": self.set_activity(x),
            },]
        self.activity_menu = MDDropdownMenu(
            background_color=self.theme_cls.primary_dark,
            caller = self.ids.activity,
            items = activity_menu_list,
            position="bottom",
            width_mult = 2,
            max_height= "150dp",)
        self.activity_menu.open()

    def set_activity(self, user_activity):
        """This stores the selected activity inside a variable."""
        self.ids.activity.text = user_activity
        self.user_activity = self.menu_choice_valid(user_activity, "activity")
        self.activity_menu.dismiss()

    def store_details(self):
        """Stores the user details into a list to be passed to the Controller."""
        details = [self.user_name, self.user_gender, self.user_height,
                   self.user_weight, self.user_age, self.user_activity]
        return details

# ========================================================================================================

    def name_valid(self, name):
        """Checks whether the user input in the name is properly written with alphabet.
        Returns the string of the name.
        """
        if self.ids.name.error or self.ids.name.text == "":
            return None
        return name

    def measurement_valid(self, measurement):
        """Checks whether the user inputs in height and weight are valid.
        Returns the value of height or weight.
        """
        try:
            user_measurement = float(measurement)
            return user_measurement
        except ValueError:
            return None

    def birthdate_valid(self, user_birthdate):
        """Uses two Python Libraries which are datetime and timedelta to calculate
        the difference between the chosen date and the current date.
        """
        chosen_date = user_birthdate
        current_date = datetime.now().date()
        birthdate = datetime.strptime(str(chosen_date), "%Y-%m-%d")
        today = datetime.strptime(str(current_date), "%Y-%m-%d")
        date_difference = relativedelta.relativedelta(today, birthdate)
        if today < birthdate or date_difference.years == 0:
            self.ids.birthdate.error = True
            return None
        self.ids.birthdate.error = False
        return date_difference.years

    def menu_choice_valid(self, selected, id):
        """Checks whether the user has chosen between the two choices in the pop-up menu.
        If the textfield is empty, this will turn to an error.
        """
        if self.ids[id].text == "":
            return None
        return selected

    def test_run(self):
        """Test run
        """
        print(f"{self.user_name} + {type(self.user_name)}")
        print(f"{self.user_height} + {type(self.user_height)}")
        print(f"{self.user_weight} + {type(self.user_weight)}")
        print(f"{self.user_gender} + {type(self.user_gender)}")
        print(f"{self.user_age} + {type(self.user_age)}")
        print(f"{self.user_activity} + {type(self.user_activity)}")

    def change_screen(self, direction, next_screen):
        """Function that changes the view to the next desired screen."""
        self.manager.transition.direction = direction
        self.manager.current = next_screen

    def error_prompt(self, color="#7B56BA"):
        """Prompt that pops-up whenever there is an error before proceeding."""
        Snackbar(text="Please check if there are invalid inputs.", bg_color=color).open()

    def check_for_errors(self):
        """Checks if all the widgets' textfields are on_error or empty.
        Returns an error prompt.
        """
        for i in self.ids.basic_info.children[1::]:
            if i.error or i.text == "":
                self.error_prompt()
                return False
        return all(not textfield.error for textfield in self.ids.basic_info.children[2::])
