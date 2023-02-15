"""
Script for managing hot reloading of the project.
For more details see the documentation page -

https://kivymd.readthedocs.io/en/latest/api/kivymd/tools/patterns/create_project/

To turn off the hot reload, just change the value of DEBUG to False
"""

import importlib
import os

from kivy import Config
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivymd.tools.hotreload.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager

import View.screens
from Model.database import DataBase

Config.set("graphics", "multisamples", 0)
os.environ["KIVY_GL_BACKEND"] = "angle_sdl2"

LabelBase.register(name='Poppins-Regular', fn_regular='assets/fonts/Poppins/Poppins-Regular.ttf')
LabelBase.register(name='Poppins-SemiBold', fn_regular='assets/fonts/Poppins/Poppins-SemiBold.ttf')
LabelBase.register(name='Poppins-Medium', fn_regular='assets/fonts/Poppins/Poppins-Medium.ttf')
LabelBase.register(name='Poppins-MediumItalic', fn_regular='assets/fonts/Poppins/Poppins-MediumItalic.ttf')
LabelBase.register(name='Poppins-Bold', fn_regular='assets/fonts/Poppins/Poppins-Bold.ttf')


class Fitrex(MDApp):
    """_summary_

    Args:
        DEBUG (bool): The switch indicator for hot reloading.
        KV_DIRS (list[str]): The directory path to the kivy files.
    """
    
    DEBUG = True
    KV_DIRS = [os.path.join(os.getcwd(), "View")]

    def build_app(self, *_) -> MDScreenManager:
        # In this method, you don't need to change
        # anything other than the application theme.

        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 0.8
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.primary_hue = "400"
        self.theme_cls.accent_palette = "DeepPurple"
        self.theme_cls.accent_hue = "800"
        self.theme_cls.material_style = "M3"

        database = DataBase()
        manager_screens = MDScreenManager()

        importlib.reload(View.screens)
        screens = View.screens.screens

        for name_screen, value in screens.items():
            model = value["model"](database)
            controller = value["controller"](model)

            for view in controller.get_views():
                view.name = name_screen
                manager_screens.add_widget(view)

        return manager_screens

    def switch_theme_style(self):
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )
      

if __name__ == "__main__":
    # adjust this base on your screen
    Window.size = (360, 640)
    Window.left = 1160
    Fitrex().run()
