"""_module summary_"""

# pylint: disable=no-name-in-module
from kivy.clock import Clock
from kivy.properties import BooleanProperty, ObjectProperty
from kivy.uix.modalview import ModalView
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.screen import MDScreen

from Utils import Observer
from Utils.observer import Observer


class BaseScreenView(ThemableBehavior, MDScreen, Observer):
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

        # loading spinner for all screens
        self.loading_view = LoadingView()

        # add itself as observer of the model
        Clock.schedule_once(lambda _: self.model.add_observer(self), 1)

    def change_screen(self, direction: str, next_screen: str):
        """Function that changes the view to the next desired screen.

        Args:
            direction (str): the transition direction.
            next_screen (str): the next screen to go to.
        """
        self.manager.transition.direction = direction
        self.manager.current = next_screen


class LoadingView(ModalView):
    """The ModalView with the Spinner which represents loading state."""

    active = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(
            on_open=lambda *_: self._change_spinner_state(True),
            on_dismiss=lambda *_: self._change_spinner_state(False),
        )

    def _change_spinner_state(self, state):
        self.active = state
