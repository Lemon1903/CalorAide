"""_module summary_"""

from kivy.animation import Animation
from kivy.uix.image import Image
from kivymd.uix.screen import MDScreen


class SplashScreenView(MDScreen):
    """_class summary_"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "splash_screen"
        self.image = Image(source="assets/images/logo.png", opacity=0)
        self.animate_image()
        self.add_widget(self.image)

    def animate_image(self):
        """Animates the logo, changing the opacity from 0% to 100% and remove it after 5 sec"""
        animation = Animation(opacity=0.1)
        animation += Animation(opacity=0.5, duration=1)
        animation += Animation(opacity=0.9, duration=1)
        animation += Animation(opacity=1, duration=3)
        animation += Animation(opacity=0, duration=0.01)
        animation.start(self.image)
