"""
Holds class definitions used in multiple files.

To get access to all of the contence of this package, use 'from Classes import *'
To get only a single object use 'from Classes.<fileName> import <objectName>'

Property snipet - use Ctrl + F to replace <propertyname> with the property name:

def __get<propertyname>(self):
    return self.__<propertyname>
def __set<propertyname>(self, newValue):
    self.__<propertyname> = newValue
def __del<propertyname>(self):
    del self.__<propertyname>
<propertyname> = property(__get<propertyname>, __set<propertyname>, __del<propertyname>, "<propertyinfo>")
"""

from .assortedClasses import *
from .comunicationClasses import *
from .dbModels import *
from .entityClasses import *
from .forms import *
