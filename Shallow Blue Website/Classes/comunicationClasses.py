import json

class JSON_Class_Extracter(object):

    def __init__(self, newClassType, newJSON_Text):

        self.classType = newClassType
        self.JSON_Text = newJSON_Text

    def __dict__(self):

        return {"classType":self.classType, "JSON_Text":self.JSON_Text}

    def getClassType(self):
        return self.__classType
    def setClassType(self, newClassType):
        self.__classType = newClassType
    def delClassType(self):
        del self.__classType
    classType = property(getClassType, setClassType, delClassType, "The class structure that the object was created from")

    def getJSON_Text(self):
        return self.__JSON_Text
    def setJSON_Text(self, newJSON_Text):
        self.__JSON_Text = newJSON_Text
    def delJSON_Text(self):
        del self.__JSON_Text
    JSON_Text = property(getJSON_Text, setJSON_Text, delJSON_Text, "The jsonified object as a JSON sting")