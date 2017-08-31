import json

class Text(object):
    """An object with one property 'text' that contains a string value"""

    def __init__(self, newText):

        self.text = newText

    def __dict__(self):

        return {"text":self._text}

    @staticmethod
    def create_From_JSON(dictionary):

        return Text(dictionary["text"])

    def getText(self):
        return self._text
    def setText(self, newValue):
        self._text = newValue
    def delText(self):
        del self._text
    text = property(getText, setText, delText, "The player's name")

class Player(object):
    """Creates a player object to hold a player's data"""

    def __dict__(self):

        return {"name":self._name}

    def sopc(self):
        """Calculates the Sum of Progressive Scores on the player object"""

        sum = None

        return sum

    @staticmethod
    def sopc(playerObject):
        """Calculates the Sum of Progressive Scores on a passed in player object"""
        
        sum = None

        return sum

    def getName(self):
        return self_.name
    def setName(self, newValue):
        self._name = newValue
    def delName(self):
        del self._name
    name = property(getName, setName, delName, "The player's name")

class JSON_Class_Extracter(object):

    def __init__(self, newClassType, newJSON_Text):

        self.classType = newClassType
        self.JSON_Text = newJSON_Text

    def __dict__(self):

        return {"classType":self._classType, "JSON_Text":self._JSON_Text}

    def getClassType(self):
        return self._classType
    def setClassType(self, newClassType):
        self._classType = newClassType
    def delClassType(self):
        del self._classType
    classType = property(getClassType, setClassType, delClassType, "The class structure that the object was created from")

    def getJSON_Text(self):
        return self._JSON_Text
    def setJSON_Text(self, newJSON_Text):
        self._JSON_Text = newJSON_Text
    def delJSON_Text(self):
        del self._JSON_Text
    JSON_Text = property(getJSON_Text, setJSON_Text, delJSON_Text, "The jsonified object as a JSON sting")