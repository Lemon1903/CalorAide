"""
The screens dictionary contains the objects of the models and controllers
of the screens of the application.
"""

from Controller import (
    HistoryScreenController,
    HomeScreenController,
    LoginScreenController,
    MainScreenController,
    SignupScreenController,
)
from Model import (
    HistoryScreenModel,
    HomeScreenModel,
    LoginScreenModel,
    MainScreenModel,
    SignupScreenModel
)

screens = {
    "login screen": {
        "model": LoginScreenModel,
        "controller": LoginScreenController,
    },
    "signup screen": {
        "model": SignupScreenModel,
        "controller": SignupScreenController,
    },
    "home screen": {
        "model": HomeScreenModel,
        "controller": HomeScreenController,
    },
    "history screen": {
        "model": HistoryScreenModel,
        "controller": HistoryScreenController,
    },
    "main screen": {
        "model": MainScreenModel,
        "controller": MainScreenController,
    },
}