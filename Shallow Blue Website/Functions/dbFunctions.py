from Classes.dbModels import *

#def addPlayer(profile = False):
#    if profile == True:
#        #Get users account identifier id? and email
#        #store request to join
#        #email user with sign up web link
#        #when user uses link, POST request sent to app
#        #In POST request:
#        #if it matches stored request, request db data from server with transaction key (inc. expiry dateTime) and player id
#        #if player returned, add to db and send conirmation email
#        pass #(other db not on site. users db is)
#    else:
#        pass

"""
addNewPlayer
importPlayerProfile - email? - flask module?
"""

def addEvent(eventName, startDate, info):
    
    db.session.add(Events(event_name = eventName, event_start_date = startDate, event_info = info))

    db.session.commit()

def deleteEvent(event_id):

    event = Events.query.filter_by(id = event_id)

    db.session.delete(event)

    db.session.commit()

def addPlayer(first_name, last_name, account_password, dob, chess_rating):

    db.session.add(Players(first_name = first_name, last_name = last_name, account_password = account_password, dob = dob, chess_rating = chess_rating))

    db.session.commit()

def deleteEvent(player_id):

    player = Players.query.filter_by(id = player_id)

    db.session.delete(player)

    db.session.commit()

def joinEvent(player_id, event_id):

    db.session.add(PlayersToEvents(player_id = player_id, event_id = event_id))

    db.session.commit()

def deleteEvent(pair_id):

    link = PlayersToEvents.query.filter_by(pair_id = pair_id)

    db.session.delete(link)

    db.session.commit()