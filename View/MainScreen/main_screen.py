"""_module summary_"""
from kivy.clock import mainthread
from kivymd.uix.floatlayout import MDFloatLayout

from View.base_screen import BaseScreenView

from .components.loading import LoadingImage


class MainScreenView(BaseScreenView):
    """I just showed an example loading spinner while doing an extensive calculations

    Args:
        BaseScreenView (_type_): _description_
    """

    def __init__(self, controller, model, **kw):
        super().__init__(controller, model, **kw)
        self.loading_bg = MDFloatLayout(md_bg_color="black", opacity=0.5)
        self.loading_img = LoadingImage()

    @mainthread
    def show_loading(self):
        self.ids.btn1.disabled = True
        self.add_widget(self.loading_bg)
        self.add_widget(self.loading_img)

    @mainthread
    def close_loading(self):
        print("done!")
        self.ids.btn1.disabled = False
        self.remove_widget(self.loading_bg)
        self.remove_widget(self.loading_img)

    def model_is_changed(self) -> None:
        """Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
