class Text(object):
    """An object with one property 'text' that contains a string value"""

    def __init__(self, newText):

        self.text = newText

    def __dict__(self):

        return {"text":self.text}

    @staticmethod
    def create_From_JSON(dictionary):

        return Text(dictionary["text"])

    def getText(self):
        return self.__text
    def setText(self, newValue):
        self.__text = newValue
    def delText(self):
        del self.__text
    text = property(getText, setText, delText, "The player's name")

class Query(Text):
    pass