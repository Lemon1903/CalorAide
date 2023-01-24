"""
The screens dictionary contains the objects of the models and controllers
of the screens of the application.
"""

from Controller.main_screen import MainScreenController
from Model.main_screen import MainScreenModel
from Controller.signup_screen import SignupScreenController
from Model.signup_screen import SignupScreenModel

screens = {
    "signup screen": {
        "model": SignupScreenModel,
        "controller": SignupScreenController,
    },
    "main screen": {
        "model": MainScreenModel,
        "controller": MainScreenController,
    },
}
