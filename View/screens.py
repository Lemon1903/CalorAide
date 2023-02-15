"""
The screens dictionary contains the objects of the models and controllers
of the screens of the application.
"""

from Controller import LoginScreenController, RegisterScreenController, SignupScreenController
from Model import LoginScreenModel, RegisterScreenModel, SignupScreenModel

screens = {
    "login screen": {
        "model": LoginScreenModel,
        "controller": LoginScreenController,
    },
    "signup screen": {
        "model": SignupScreenModel,
        "controller": SignupScreenController,
    },
    "register screen,mode screen,goal screen": {
        "model": RegisterScreenModel,
        "controller": RegisterScreenController,
    },
}
