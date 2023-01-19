"""_module summary_"""

# pylint: disable=no-name-in-module
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.screen import MDScreen


class BaseScreenView(ThemableBehavior, MDScreen):
    """
    A base class that implements a visual representation of the model data.
    The view class must be inherited from this class. Follows the observer parttern.
    """

    def __init__(self, controller, model, **kw):
        super().__init__(**kw)

        self.controller = controller
        """Controller object - :class:`~Controller.controller_screen.ClassScreenControler`."""

        self.model = model
        """Model object - :class:`~Model.model_screen.ClassScreenModel`."""

        # access the application object from the view class.
        self.app = MDApp.get_running_app()

        # adding a view class as observer.
        self.model.add_observer(self)

    def model_is_changed(self):
        """The method that will be called on the observer when the model changes."""
        raise NotImplementedError(
            "This is an observer, it should be notified about the changes in the model."
        )
