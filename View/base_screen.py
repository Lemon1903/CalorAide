"""_module summary_"""

# pylint: disable=no-name-in-module
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior

from Utils.observer import Observer


class BaseScreenView(ThemableBehavior, Screen, Observer):
    """
    A base class that implements a visual representation of the model data.
    The view class must be inherited from this class. Follows the observer parttern.
    """

    controller = ObjectProperty()
    """
    Controller object - :class:`~Controller.login_screen.LoginScreenController`.

    :attr:`controller` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    model = ObjectProperty()
    """
    Model object - :class:`~Model.login_screen.LoginScreenModel`.

    :attr:`model` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    def __init__(self, **kw):
        super().__init__(**kw)

        # access the application object from the view class.
        self.app = MDApp.get_running_app()

        # add itself as observer of the model
        Clock.schedule_once(lambda _: self.model.add_observer(self), 1)
