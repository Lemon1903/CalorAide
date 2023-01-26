"""_module summary_"""
import multitasking

from Model.base_model import BaseScreenModel

multitasking.set_max_threads(10)


class SignupScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.SignupScreen.signup_screen.SignupScreenView` class.
    """

    def __init__(self, database):
        # Just an example of the data. Use your own values.
        self._is_valid = False
        self.database = database

    @property
    def is_valid(self): #get
        """_data summary_

        Returns:
            _type_: _description_
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, value): #set
        # We notify the View -
        # :class:`~View.MainScreen.main_screen.MainScreenView` about the
        # changes that have occurred in the data model.
        self._is_valid = value
        self.notify_observers("signup screen")

    @multitasking.task
    def check_data(self, userdata): #check if valid yung data from controller
        """Just an example of the method. Use your own code."""
        # self.database.create_table()
        self.username = userdata[0]
        self.data = self.database.get_data()
        for key,value in self.data.items():
            if value['Username']  == self.username:
                self.is_valid = False
            else: 
                self.is_valid = True 
                self.database.add(userdata)
            return
    
    def to_database(self, userdata):
        self.is_valid = True
        self.database.add(userdata)

    def check_username(self, userdata):
        self.username = userdata[0]
        self.data = self.database.get_data()
        for key,value in self.data.items():
            if value["Username"]  == self.username:
                return(value["Username"])

        


    
        

        
              
              
    

