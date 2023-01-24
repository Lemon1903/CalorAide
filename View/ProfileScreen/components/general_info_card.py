# pylint: disable=no-name-in-module
from kivy.animation import Animation, AnimationTransition
from kivy.properties import ObjectProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard


class ProfileInformationLayout(MDBoxLayout):
    def on_edit_profile_info(self):
        self.parent.change_layout(self.parent.edit_layout)


class EditInformationLayout(MDBoxLayout):
    def submit_new_profile_info(self):
        print("submit")
        self.parent.change_layout(self.parent.profile_layout)


class GeneralInformationCard(MDCard):
    current_layout = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.profile_layout = ProfileInformationLayout()
        self.edit_layout = EditInformationLayout()

    def change_layout(self, new_layout: MDBoxLayout):
        self._animate_height(new_layout)

    def _animate_height(self, new_layout):
        height_anim = Animation(
            height=new_layout.height + self.padding[1] * 2,
            transition=AnimationTransition.in_out_sine,
            duration=0.5,
        )

        height_anim.bind(
            on_start=lambda *_: self._fade_layout(self.current_layout, 0.0))
        height_anim.bind(
            on_progress=lambda *a: self._show_layout(new_layout, a[2]))
        height_anim.bind(
            on_complete=lambda *_: self._fade_layout(new_layout, 1.0))
        height_anim.start(self)

    def _fade_layout(self, layout: MDBoxLayout, opacity):
        fade_anim = Animation(opacity=opacity, duration=0.3)
        fade_anim.start(layout)

    def _show_layout(self, new_layout, progress):
        if progress > 0.8:
            self.remove_widget(self.current_layout)
            self.add_widget(new_layout)
            self.current_layout = new_layout
