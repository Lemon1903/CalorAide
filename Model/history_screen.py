"""_module summary_"""
import multitasking


from Model.base_model import BaseScreenModel

multitasking.set_max_threads(10)


class HistoryScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.MainScreen.main_screen.MainScreenView` class.
    """

    def __init__(self, database):
        # Just an example of the data. Use your own values.
        self._data = None
        self.database = database

    @property
    def data(self):
        """_data summary_

        Returns:
            _type_: _description_
        """
        return self._data

    @data.setter
    def data(self, value):
        # We notify the View -
        # :class:`~View.MainScreen.main_screen.MainScreenView` about the
        # changes that have occurred in the data model.
        self._data = value
        self.notify_observers("history screen")

    
    def getting_history_data(self):
        """ Get data from database history table """
        self.history_data = self.database.get_history("History")
        return self.history_data




