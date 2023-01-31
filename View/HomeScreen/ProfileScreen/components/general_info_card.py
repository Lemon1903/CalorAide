"""Anything related to the general information of the user."""

# pylint: disable=no-name-in-module
from kivy.animation import Animation, AnimationTransition
from kivy.clock import Clock
from kivy.properties import (
    DictProperty,
    NumericProperty,
    ObjectProperty,
    StringProperty,
)
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.textfield import MDTextField


class GeneralInformationCard(MDCard):
    """Card for general information of the user."""

    controller = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.profile_layout = ProfileInformationLayout()
        self.edit_layout = EditInformationLayout()
        self.current_layout = self.profile_layout
        Clock.schedule_once(lambda _: self.add_widget(self.current_layout))

    def change_layout(self, new_layout: MDBoxLayout):
        """Changing the content inside the card.

        Args:
            new_layout (MDBoxLayout): the new layout to be shown.
        """
        self._animate_height(new_layout)

    def _animate_height(self, new_layout: MDBoxLayout):
        height_anim = Animation(
            height=new_layout.height + self.padding[1] * 2,
            transition=AnimationTransition.in_out_sine,
            duration=0.5,
        )
        height_anim.bind(
            on_start=lambda *_: self._fade_layout(self.current_layout, 0.0),
            on_progress=lambda *a: self._show_layout(new_layout, a[2]),
            on_complete=lambda *_: self._fade_layout(new_layout, 1.0),
        )
        height_anim.start(self)

    def _fade_layout(self, layout: MDBoxLayout, opacity: float):
        fade_anim = Animation(opacity=opacity, duration=0.2)
        fade_anim.start(layout)

    def _show_layout(self, new_layout, progress):
        if progress > 0.5:
            self.remove_widget(self.current_layout)
            self.add_widget(new_layout)
            self.current_layout = new_layout


class ProfileInformationLayout(MDBoxLayout):
    """The content layout for the profile information."""

    name_info = StringProperty("")
    age_info = NumericProperty(0)
    gender_info = StringProperty("")
    height_info = NumericProperty(0)
    weight_info = NumericProperty(0)
    bmi_info = StringProperty("")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._profile_info = {}

    @property
    def profile_info(self):
        """Returns the profile information of the user."""
        return self._profile_info

    def update_profile_information(self, new_info: dict):
        """Updates the profile information of the user.

        Args:
            new_info (dict): the new profile information.
        """
        self.name_info = new_info["Name"]
        self.age_info = new_info["Age"]
        self.gender_info = new_info["Gender"]
        self.height_info = new_info["Height"]
        self.weight_info = new_info["Weight"]
        self.bmi_info = new_info["BMI"]
        self._profile_info = new_info

    def on_edit_profile_info(self):
        """Callback function when editing the profile information."""
        self.parent.edit_layout.current_profile_info = self._profile_info
        self.parent.change_layout(self.parent.edit_layout)


class EditInformationLayout(MDBoxLayout):
    """The content layout for editing profile information."""

    current_profile_info = DictProperty({"Name": "", "Height": "", "Weight": ""})

    def submit_new_profile_info(self):
        """Callback function when submitting the new profile information."""
        textfields = self._get_textfields()
        if self._is_same_info(textfields):
            self.parent.change_layout(self.parent.profile_layout)
        elif self._has_no_error(textfields):
            self.parent.controller.update_user_data(textfields)
            self.parent.change_layout(self.parent.profile_layout)

    def _get_textfields(self):
        return [child for child in self.children if isinstance(child, MDTextField)]

    def _is_same_info(self, textfields):
        profile_info = self.parent.profile_layout.profile_info
        return all(tf.text == profile_info[tf.hint_text] for tf in textfields)

    def _has_no_error(self, textfields):
        return all(not tf.error for tf in textfields)
