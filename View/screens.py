"""
The screens dictionary contains the objects of the models and controllers
of the screens of the application.
"""

from Controller import (LoginScreenController, MainScreenController,
                        ProfileScreenController, SignupScreenController)
from Model import LoginScreenModel, MainScreenModel, ProfileScreenModel, SignupScreenModel

screens = {
    "signup screen":{
        "model": SignupScreenModel,
        "controller": SignupScreenController,
    },
    "login screen": {
        "model": LoginScreenModel,
        "controller": LoginScreenController,
    },
    "profile screen": {
        "model": ProfileScreenModel,
        "controller": ProfileScreenController,
    },

    "main screen": {
        "model": MainScreenModel,
        "controller": MainScreenController,
    },
}