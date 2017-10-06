"""
This module contains the Player and Event classes along with all their child classes
"""

class Player(object):

    """
    Holds player data
    Atributes:
                id - Player ID - integer
                firstName - Player's first name - string
                lastName - Player's last name - string
                dob - Player's date of birth - date
                chessRating - Player's FIDE chess rating - integer
    """

    def __init__(self, newID, newFirstName, newLastName, newDOB, newChessRating = 1000):
        
        """
        Initialiser for class Player
        Paramiters:
                    newID - player id - integer
                    newFirstName - first name of player - string
                    newLastName - last name of player - string
                    newDOB - player's date of birth - date
                    newChessRating - player's FIDE chess rating (if applicable) - integer - deafult = 1000
        """

        self.id = newID
        self.firstName = newFirstName
        self.lastName = newLastName
        self.dob = newDOB
        self.chessRating = newChessRating

    def __getid(self):
        return self.__id
    def __setid(self, newValue):
        self.__id = newValue
    def __delid(self):
        del self.__id
    id = property(__getid, __setid, __delid, "Player ID")

    def __getfirstName(self):
        return self.__firstName
    def __setfirstName(self, newValue):
        self.__firstName = newValue
    def __delfirstName(self):
        del self.__firstName
    firstName = property(__getfirstName, __setfirstName, __delfirstName, "Player's first name")

    def __getlastName(self):
        return self.__lastName
    def __setlastName(self, newValue):
        self.__lastName = newValue
    def __dellastName(self):
        del self.__lastName
    lastName = property(__getlastName, __setlastName, __dellastName, "Player's last name")

    def __getdob(self):
        return self.__dob
    def __setdob(self, newValue):
        self.__dob = newValue
    def __deldob(self):
        del self.__dob
    dob = property(__getdob, __setdob, __deldob, "Player's date of birth")

    def __getchessRating(self):
        return self.__chessRating
    def __setchessRating(self, newValue):
        self.__chessRating = newValue
    def __delchessRating(self):
        del self.__chessRating
    chessRating = property(__getchessRating, __setchessRating, __delchessRating, "Player's FIDE chess rating")

    def __dict__(self):

        """
        Converts the Player class into a dictionary object
        """

        return {"id": self.id, "first_name": self.firstName, "lastName": self.lastName, "dob": self.dob, "chess_rating": self.chessRating}

class Event:

    """
    Holds event data for manipulation or transmition
    Atributes:
                id - The db event ID - integer
                name - The event name - string
                startDateTime - The datetime stamp for the start of the event - datetime
                info - Event info - string
    """

    def __init__(self, newID, newName, newStartDateTime, newInfo):

        """
        Initialiser for class Event
        Paramiters:
                    newID - event id - integer
                    newName - name of event - string
                    newStartDateTime - start date and time of the event - datetime
                    newInfo - event info - string
        """

        self.id = newID
        self.name = newName
        self.startDateTime = newStartDateTime
        self.info = newInfo

    def __getid(self):
        return self.__id
    def __setid(self, newValue):
        self.__id = newValue
    def __delid(self):
        del self.__id
    id = property(__getid, __setid, __delid, "The db event ID")

    def __getname(self):
        return self.__name
    def __setname(self, newValue):
        self.__name = newValue
    def __delname(self):
        del self.__name
    name = property(__getname, __setname, __delname, "The event name")

    def __getstartDateTime(self):
        return self.__startDateTime
    def __setstartDateTime(self, newValue):
        self.__startDateTime = newValue
    def __delstartDateTime(self):
        del self.__startDateTime
    startDateTime = property(__getstartDateTime, __setstartDateTime, __delstartDateTime, "The datetime stamp for the start of the event")

    def __getinfo(self):
        return self.__info
    def __setinfo(self, newValue):
        self.__info = newValue
    def __delinfo(self):
        del self.__info
    info = property(__getinfo, __setinfo, __delinfo, "Event info")

    def __dict__(self):

        """
        Converts the Event class into a dictionary object
        """

        return {"id": self.id, "name": self.name, "start_date_time": self.startDateTime, "info": self.info}