from kivy.lang import Builder
from kivymd.app import MDApp

KV = """
#:import SlideTransition kivy.uix.screenmanager.SlideTransition

MDRelativeLayout:
    MDScreen:
        FitImage:
            source: "assets/images/DarkBG.png"

    MDScreenManager:
        id: manager

        MDScreen:
            name: "screen1"
            MDRaisedButton:
                text: "To Screen2"
                on_press: manager.current = "screen2"

        MDScreen:
            name: "screen2"
            MDRaisedButton:
                text: "To Screen3"
                on_press: manager.current = "screen3"

        MDScreen:
            name: "screen3"
            MDRaisedButton:
                text: "To Screen1"
                on_press: manager.current = "screen1"

        # MDScreen:
        #     MDBottomNavigation:
        #         selected_color_background: "orange"
        #         text_color_active: "lightgrey"
            
        #         MDBottomNavigationItem:
        #             name: 'screen 1'
        #             text: 'Mail'
        #             icon: 'gmail'
        #             badge_icon: "numeric-10"

        #             MDScreen:

        #         MDBottomNavigationItem:
        #             name: 'screen 2'
        #             text: 'Twitter'
        #             icon: 'twitter'
        #             badge_icon: "numeric-5"

        #             MDLabel:
        #                 text: 'Twitter'
        #                 halign: 'center'

        #         MDBottomNavigationItem:
        #             name: 'screen 3'
        #             text: 'LinkedIN'
        #             icon: 'linkedin'

        #             MDLabel:
        #                 text: 'LinkedIN'
        #                 halign: 'center'
"""


class Test(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)


Test().run()
