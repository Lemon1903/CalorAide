"""
The screens dictionary contains the objects of the models and controllers
of the screens of the application.
"""

from Controller import LoginScreenController, SignupScreenController
from Model import LoginScreenModel, SignupScreenModel

screens = {
    "signup screen": {
        "model": SignupScreenModel,
        "controller": SignupScreenController,
    },
    "login screen": {
        "model": LoginScreenModel,
        "controller": LoginScreenController,
    },
}