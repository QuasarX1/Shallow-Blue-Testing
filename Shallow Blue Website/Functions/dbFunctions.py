from Classes.dbModels import *

def newTestTable(nameFeild):
    return TestTable(name = nameFeild)

def newTestTable2(TestTable_id, nameFeild):
    return TestTable2(otherTableID = TestTable_id, name = nameFeild)

def addPlayer(profile = False):
    if profile == True:
        #Get users account identifier id? and email
        #store request to join
        #email user with sign up web link
        #when user uses link, POST request sent to app
        #In POST request:
        #if it matches stored request, request db data from server with transaction key (inc. expiry dateTime) and player id
        #if player returned, add to db and send conirmation email
        pass #(other db not on site. users db is)
    else:
        pass

"""
addNewPlayer
importPlayerProfile - email? - flask module?
"""