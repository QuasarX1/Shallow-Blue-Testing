from Classes import *
import json
import importlib

def serialise_To_JSON_Data(objectArray):

    dataArray = []
    
    for object in objectArray:

        testDict = object.__dict__()

        dataArray.append(JSON_Class_Extracter(str(type(object).__name__), json.dumps(testDict)).__dict__())

    return json.dumps(dataArray)

def read_JSON_Data(rawData):

    dataList = json.loads(rawData)

    #dict_List = []

    for JSON_Object in dataList:

        JSON_Object["JSON_Text"] = json.loads(JSON_Object["JSON_Text"])

        #dict_List.append(json.loads(JSON_Object["JSON_Text"]))

    objectList = []

    for dictionary in dataList:

        dictClass = getattr(importlib.import_module("Classes"), dictionary["classType"])

        objectList.append(dictClass.create_From_JSON(dictionary["JSON_Text"]))

    return objectList