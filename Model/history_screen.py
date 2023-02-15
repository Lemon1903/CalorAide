"""_module summary_"""
import multitasking

from Model.base_model import BaseScreenModel

multitasking.set_max_threads(10)


class HistoryScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.HistoryScreen.main_screen.HistoryScreenView` class.
    """

    def __init__(self, database):
        # Just an example of the data. Use your own values.
        self._database = database
        self.all_intake_history = None

    @multitasking.task
    def load_all_intake_history(self):
        """ Get data from database history table. """
        self.all_intake_history = self._database.get_user_data("History")
        self.notify_observers("history screen")
