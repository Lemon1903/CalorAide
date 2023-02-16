"""
The screens dictionary contains the objects of the models and controllers
of the screens of the application.
"""

from Controller import (HistoryScreenController, HomeScreenController,
                        LoginScreenController, RegisterScreenController,
                        SignupScreenController)
from Model import (HistoryScreenModel, HomeScreenModel, LoginScreenModel,
                   RegisterScreenModel, SignupScreenModel)

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
    "home screen": {
        "model": HomeScreenModel,
        "controller": HomeScreenController,
    },
    "history screen": {
        "model": HistoryScreenModel,
        "controller": HistoryScreenController,
    },
}
