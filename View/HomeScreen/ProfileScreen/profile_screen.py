"""_module summary_"""

# pylint: disable=no-name-in-module
import calendar
from datetime import date

import matplotlib.pyplot as plt
from kivy.clock import mainthread
from kivy.properties import StringProperty
from kivymd.uix.pickers import MDDatePicker
from matplotlib import style

from View.base_screen import BaseScreenView

from .components import ActivityDialog


class ProfileScreenView(BaseScreenView):
    """The view that handles UI for profile screen."""

    current_activity = StringProperty()
    current_graph1_date = StringProperty(date.today().strftime("%B %Y"))
    current_graph2_date = StringProperty(date.today().strftime("%B %d %Y"))

    def __init__(self, **kw):
        super().__init__(**kw)
        self.graph1_date = {"Month": date.today().month, "Year": date.today().year}

        self.activity_dialog = ActivityDialog(self)
        self.graph1_date_dialog = MDDatePicker(
            min_year = 2000,
            max_year = date.today().year,
            year=date.today().year,
            month=date.today().month,
            day=date.today().day
        )
        self.graph2_date_dialog = MDDatePicker(
            min_year = 2000,
            max_year = date.today().year,
            year=date.today().year,
            month=date.today().month,
            day=date.today().day
        )
        self.graph1_date_dialog.bind(on_save=self.set_graph1_date)
        self.graph2_date_dialog.bind(on_save=self.set_graph2_date)

    @mainthread
    def model_is_changed(self) -> None:
        """Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        if self.model.loaded_activity:
            self.model.loaded_activity = False
            self.update_activity(self.model.user_profile_data)

        elif self.model.loaded_general_info:
            self.model.loaded_general_info = False
            self.update_general_information_card(self.model.user_profile_data)

        elif self.model.loaded_calorie_progress:
            self.model.loaded_calorie_progress = False
            self.update_bar_graph_data(self.model.user_all_history_data)

        elif self.model.loaded_intake_breakdown:
            self.model.loaded_intake_breakdown = False
            self.update_pie_chart_data(self.model.user_specific_intake_data)

        self.controller.done_loading("profile")

    def update_activity(self, profile_data: dict):
        """Updates the activity label about the changes in data."""
        if profile_data is None:
            self.controller.show_connection_error()
            return

        self.current_activity = profile_data["Activity"].upper()
        self.activity_dialog.current_activity = profile_data["Activity"]
        self.controller.hide_connection_error()

    def update_general_information_card(self, profile_data: dict):
        """Updates the general information card UI about the changes in data."""
        if profile_data is None:
            self.controller.show_connection_error()
            return

        if self.current_activity:
            self.ids.general_info.change_layout()

        self.update_activity(profile_data)
        self.ids.general_info.profile_layout.update_profile_information(profile_data)
        self.controller.hide_connection_error()

    def update_bar_graph_data(self, all_history_data: dict):
        """Bar graphs the user calorie progress each day per month base on the data."""
        if all_history_data is None:
            self.controller.show_connection_error()
            return

        style.use("seaborn-v0_8")
        figure, axes = plt.subplots(figsize=(3.8, 5))
        x_axis, y_axis = self._get_calorie_progress_per_day(
            all_history_data, self.graph1_date["Month"], self.graph1_date["Year"]
        )

        # TODO: set xlim to where there is data, pan range must be within no of days of that month
        bars = axes.bar(x_axis, y_axis, color=self.theme_cls.accent_color)
        for bar_ in bars:
            height = bar_.get_height()
            axes.annotate(
                f'{height}',
                xy=(bar_.get_x() + bar_.get_width() / 2, height),
                xytext=(0, 5),  # 5 points vertical offset
                textcoords="offset points",
                ha='center',
                va='bottom',
            )

        # figure.patch.set_alpha(0.5)
        # axes.tick_params(axis="x", colors="white")
        axes.get_yaxis().set_visible(False)
        axes.set_xlim(0, 7)
        axes.set_ylim(0, max(y_axis) + 300)

        plt.tight_layout()
        self.ids.graph1.figure = figure
        self.ids.graph1.axes = axes
        self.controller.hide_connection_error()

    def update_pie_chart_data(self, specific_intake_data: dict):
        """Pie graphs the user intake breakdown in specific date base on the data."""
        if specific_intake_data is None:
            self.controller.show_connection_error()
            return

        style.use("seaborn-v0_8")
        figure, axes = plt.subplots(figsize=(3, 1))
        merged_foods, merged_calories = self._get_merged_intake_data(specific_intake_data)

        # TODO: change font size base in zoom or fixed size (8/9)
        shortcut = [food.split()[0] for food in merged_foods]
        axes.pie(
            merged_calories,
            labels=shortcut,
            textprops={'fontsize': 14},
            wedgeprops={'width': 1, 'edgecolor': self.theme_cls.accent_color},
            autopct='%1.1f%%',
            pctdistance=0.8,
            startangle=90
        )

        plt.tight_layout()
        self.ids.graph2.figure = figure
        self.ids.graph2.axes = axes
        self.controller.hide_connection_error()

    def _get_calorie_progress_per_day(self, all_history_data, month, year):
        """Get all the calorie progress per day of the user in a month.

        Args:
            all_history_data (dict): the raw history data of the user.
            month (int): the specific month to show all the calorie progress.
            year (int): the specific year to show all the calorie progress.

        Returns:
            tuple(list[int], list[float]): returns the day and its corresponding calorie progress.
        """
        month_range = calendar.monthrange(year, month)[1]
        total_calories, readable_dates = [], []

        for day in range(1, month_range + 1):
            date_ = f"{day:02}-{month:02}-{year}"
            calorie_sum = 0.0
            readable_dates.append(str(day))

            if date_ not in all_history_data:
                # no intake history of this date yet in database
                total_calories.append(calorie_sum)
            else:
                # store the calorie sum of this date from database
                for identifier, intake_item in all_history_data[date_].items():
                    if identifier != "Calorie Goal":
                        calorie_sum += intake_item['Calorie Amount']
                total_calories.append(calorie_sum)

        return readable_dates, total_calories

    def _get_merged_intake_data(self, intake_data: dict):
        """Get the merged foods and its corresponding calorie.

        Args:
            intake_data (dict): the raw intake data.

        Returns:
            tuple[list[str], list[float]]: the merged foods and corresponding calorie.
        """
        merged_foods, merged_calories = [], []
        for identifier, intake_item in intake_data.items():
            if identifier != "Calorie Goal":
                intake_food = intake_item["Food"].capitalize()
                if intake_food not in merged_foods:
                    # add unique food and its calorie amount to the list
                    merged_foods.append(intake_food)
                    merged_calories.append(intake_item["Calorie Amount"])
                else:
                    # add the same food calorie amount to its latest calorie amount
                    index = merged_foods.index(intake_food)
                    merged_calories[index] += intake_item["Calorie Amount"]
        return merged_foods, merged_calories

    def set_graph1_date(self, *args):
        """Sets the shown date in graph1 card."""
        self.graph1_date = {"Month": args[1].month, "Year": args[1].year}
        self.current_graph1_date = args[1].strftime("%B %Y")
        self.controller.load_all_history_data()

    def set_graph2_date(self, *args):
        """Sets the shown date in graph2 card."""
        self.current_graph2_date = args[1].strftime("%B %d %Y")
        self.controller.load_specific_intake_data(args[1].strftime("%d-%m-%Y"))
