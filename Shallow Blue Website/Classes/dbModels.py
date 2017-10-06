"""
Each class represents a table

Layout:

class <className>(db.Model):

    __tablename__ = "<tableName>"
    <idFeildName> = db.Column(db.Integer, primary_key = True)
    <otherTextFeildName> = db.Column(db.Text(64))

    <relationshipVarName> = db.relationship("<tableName_of_table_with_foreign_key>", backref = "<reference_variable_name>, uselist = <True for 1toMany, False for 1to1")

    def __repr__(self):
        return "<<tableName> %r>" % self.<feildName_of_feild_to_be_returned>
"""

import json

#The folowing import nessessary. Add any models after it.
from CommonDependencies.sqlalchemy_db_object import db
#---------------------------------------------------------------------

class PlayersToEvents(db.Model):

    __tablename__ = "players-to-events"
    pair_id = db.Column(db.Integer, primary_key = True)
    player_id = db.Column(db.Integer, db.ForeignKey("players.id"), index = True)
    event_id = db.Column(db.Integer, db.ForeignKey("events.id"), index = True)
    score = db.Column(db.Integer, default = 0)
    oponent_ids = db.Column(db.String, default = json.dumps([])) #Use import json json.dumps(list) and json.loads(json) to create and read string from db
    results = db.Column(db.String, default = []) #Use "..." with arrays of ["W", "D", "L"]

    def __repr__(self):
        return "<PlayersToEvents %r %r>" % self.player_id, self.event_id

class Events(db.Model):

    __tablename__ = "events"
    id = db.Column(db.Integer, primary_key = True)
    event_name = db.Column(db.String)
    event_start_date_time = db.Column(db.DateTime)
    event_info = db.Column(db.Text(64))

    players_link_reference = db.relationship("PlayersToEvents", backref = "link_table_reference_events")
   
    def __repr__(self):
        return "<Events %r>" % self.id

class Players(db.Model):

    __tablename__ = "players"
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String, index = True)
    last_name = db.Column(db.String, index = True)
    account_password = db.Column(db.String, nullable = True)
    dob = db.Column(db.Date)
    chess_rating = db.Column(db.Integer)

    events_link_reference = db.relationship("PlayersToEvents", backref = "link_table_reference_players")

    def __repr__(self):
        return "<Players %r>" % self.id