"""
The screens dictionary contains the objects of the models and controllers
of the screens of the application.
"""

from Controller import (HistoryScreenController, HomeScreenController,
                        LoginScreenController)
from Model import HistoryScreenModel, HomeScreenModel, LoginScreenModel

screens = {
    "login screen": {
        "model": LoginScreenModel,
        "controller": LoginScreenController,
    },
    "history screen": {
        "model": HistoryScreenModel,
        "controller": HistoryScreenController,
    },
    "home screen": {
        "model": HomeScreenModel,
        "controller": HomeScreenController,
    },
}
