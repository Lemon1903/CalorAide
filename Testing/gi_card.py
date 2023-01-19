from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen

KV = """
<MyScreen>:
    MDCard:
        orientation: "vertical"
        padding: (20, 10)
        spacing: dp(10)
        size_hint: 0.8, None
        height: dp(200)
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        md_bg_color: app.theme_cls.primary_color

        MDLabel:
            text: "General Information"
            size_hint_y: None
            height: dp(30)

        MDFloatLayout:
            id: floatlayout

            MDFloatLayout:
                pos_hint: {"x": 0, "y": 0}

                MDLabel:
                    text: "First Info"
                    pos_hint: {"x": 0.05, "center_y": 0.4}

                MDLabel:
                    text: "Second Info"
                    pos_hint: {"x": 0.05, "center_y": 0.6}

                MDIconButton:
                    icon: "square-edit-outline"
                    pos_hint: {"right": 1, "y": 0}
                    on_press: root.on_edit()


<EditPopup>:
    orientation: "vertical"
    padding: dp(20)
    spacing: dp(15)
    pos_hint: {"x": 0, "y": 0}
    md_bg_color: app.theme_cls.primary_color

    MDTextField:
        hint_text: "First Info"
        mode: "rectangle"
        size_hint_x: 0.7
        pos_hint: {"x": 0}

    MDRaisedButton:
        text: "Done"
        pos_hint: {"right": 1}
"""


class EditPopup(MDBoxLayout):
    pass


class MyScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.edit_popup = EditPopup()

    def on_edit(self):
        if not self.edit_popup.parent:
            self.ids.floatlayout.add_widget(self.edit_popup)


class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Orange"

        Builder.load_string(KV)
        return MyScreen()


if __name__ == "__main__":
    MyApp().run()
