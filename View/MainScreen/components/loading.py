# pylint: disable=no-name-in-module
from kivy.animation import Animation
from kivy.properties import NumericProperty
from kivy.uix.image import Image


class LoadingImage(Image):
    angle = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.rotation_angle = -360
        anim = Animation(angle=self.rotation_angle, d=2)
        anim += Animation(angle=self.rotation_angle, d=2)
        anim.repeat = True
        anim.start(self)

    def on_angle(self, item, angle):
        if angle == self.rotation_angle:
            item.angle = 0
