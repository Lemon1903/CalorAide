"""
The screens dictionary contains the objects of the models and controllers
of the screens of the application.
"""

from Controller import (HomeScreenController, LoginScreenController,
                        MainScreenController)
from Model import HomeScreenModel, LoginScreenModel, MainScreenModel

screens = {
    "home screen": {
        "model": HomeScreenModel,
        "controller": HomeScreenController,
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
