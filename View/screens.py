"""
The screens dictionary contains the objects of the models and controllers
of the screens of the application.
"""

from Controller.main_screen import MainScreenController
from Model.main_screen import MainScreenModel

screens = {
    "main screen": {
        "model": MainScreenModel,
        "controller": MainScreenController,
    },
}
