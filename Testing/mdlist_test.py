from kivy.lang import Builder
from kivymd.app import MDApp

KV = """
MDScrollView:
    MDList:
        MDBoxLayout:
            adaptive_height: True
            MDLabel:
                text: "Item"
            MDLabel:
                text: "Item"

        MDBoxLayout:
            adaptive_height: True
            MDLabel:
                text: "Item"
            MDLabel:
                text: "Item"
"""


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)


Example().run()
