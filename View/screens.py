"""
The screens dictionary contains the objects of the models and controllers
of the screens of the application.
"""

from Controller import (LoginScreenController, MainScreenController,
                        ProfileScreenController, RegisterScreenController,
                        SignupScreenController)
from Model import (LoginScreenModel, MainScreenModel, ProfileScreenModel,
                   RegisterScreenModel, SignupScreenModel)

screens = {
    "register screen,mode screen,goal screen": {
        "model": RegisterScreenModel,
        "controller": RegisterScreenController,
    },
    "signup screen": {
        "model": SignupScreenModel,
        "controller": SignupScreenController,
    },
    "profile screen": {
        "model": ProfileScreenModel,
        "controller": ProfileScreenController,
    },
    "login screen": {
        "model": LoginScreenModel,
        "controller": LoginScreenController,
    },
    "main screen": {
        "model": MainScreenModel,
        "controller": MainScreenController,
    },
}
