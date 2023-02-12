"""
The screens dictionary contains the objects of the models and controllers
of the screens of the application.
"""

from Controller import (
    LoginScreenController,
    MainScreenController,
    ProfileScreenController,
    SignupScreenController,
    HistoryScreenController,
)
from Model import LoginScreenModel, MainScreenModel, ProfileScreenModel, SignupScreenModel, HistoryScreenModel

screens = {
    "history screen": {
        "model": HistoryScreenModel,
        "controller": HistoryScreenController,
    },
    "login screen": {
        "model": LoginScreenModel,
        "controller": LoginScreenController,
    },
    "signup screen": {
        "model": SignupScreenModel,
        "controller": SignupScreenController,
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