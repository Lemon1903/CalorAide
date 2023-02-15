"""_module summary_"""
import matplotlib.pyplot as plt
import matplotlib.style as style
# pylint: disable=no-name-in-module
from kivy.clock import mainthread
from kivy.properties import StringProperty

from View.base_screen import BaseScreenView

from .components import ActivityDialog


class ProfileScreenView(BaseScreenView):
    """The view that handles UI for profile screen."""

    current_activity = StringProperty("")

    def __init__(self, **kw):
        super().__init__(**kw)
        self.activity_dialog = ActivityDialog(
            confirm_callback=self._close_activity_dialog,
            cancel_callback=self._close_activity_dialog,
        )

        self.bar_days = 'Last 7 Days'
        self.pie_days = 'Today'


    @mainthread
    def model_is_changed(self) -> None:
        """Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        if self.model.updated_profile_part == "activity":
            self.current_activity = self.model.user_profile_data["Activity"].upper()
        elif self.model.updated_profile_part == "general information":
            self.update_general_information_card(self.model.user_profile_data)
        self.model.has_loaded_profile = True

    def update_general_information_card(self, profile_data: dict):
        """Updates the general information card UI about the changes in data."""
        self.ids.general_info.profile_layout.update_profile_information(profile_data)

        if self.controller.has_loaded_profile:
            self.ids.general_info.change_layout()

    def _close_activity_dialog(self):
        self.activity_dialog.dismiss()

    def show_bar_graph_data(self, button):
        style.use("seaborn-v0_8")
        fig, ax = plt.subplots(figsize=(3.8, 5))

        y, calorie_goal = self.controller.get_calories() 
        x = self.controller.get_dates()

        self.bar_days = button.text

        if self.bar_days == 'Last 7 Days': 
            self.bar_days = 'Last 14 Days'
            x = x[-7::]
            y = y[-7::]
        elif self.bar_days == 'Last 14 Days':
            self.bar_days = 'Last 7 Days'
            x = x[-14::]
            y = y[-14::]

        bars = ax.bar(x, y, color=self.theme_cls.accent_color)

        for bar in bars: 
            height = bar.get_height()
            ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
        
        ax.set_title('Calorie Intake Graph')        
        ax.set_xlabel(f"Last {len(x)} Days")
        plt.xticks(rotation=45)

        calorie = sum(y)      
        if calorie < calorie_goal:
            ax.set_ylim(0, calorie_goal)
        else:
            ax.set_ylim(0, calorie_goal+1000)

        plt.tight_layout()

        plt.savefig("assets/images/bar.png")

    def show_pie_chart_data(self, button):
        style.use("seaborn-v0_8")
        fig, ax = plt.subplots(figsize=(3.8, 5))
        foods, calories = self.controller.get_food()                   

        self.pie_days = button.text

        if self.pie_days == 'Today':
            self.pie_days = 'Yesterday'
            calories = calories[-1]
            foods = foods[-1]                                                  
            ax.set_xlabel("Today")
        elif self.pie_days == 'Yesterday':
            self.pie_days = 'Today'
            calories = calories[-2]
            foods = foods[-2]
            ax.set_xlabel("Yesterday")
    

        ax.pie(calories, labels=foods, textprops={'fontsize': 8}, wedgeprops={'width': 0.4, 'edgecolor': self.theme_cls.accent_color}, autopct='%1.1f%%', pctdistance=0.8, startangle=90)
        ax.set_title("Food Log Chart")
        plt.axis('equal')
        plt.tight_layout()
        plt.savefig("assets/images/pie.png")
        
        plt.clf()