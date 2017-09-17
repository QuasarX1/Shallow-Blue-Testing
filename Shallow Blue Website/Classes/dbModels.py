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

#The folowing import nessessary. Add any models after it.
from CommonDependencies.sqlalchemy_db_object import db
#---------------------------------------------------------------------

class TestTable(db.Model):

    __tablename__ = "test"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text(64))

    t2 = db.relationship("testTable2", backref = "otherTableID_reference")

    def __repr__(self):
        return "<testTable %r>" % self.name

class TestTable2(db.Model):

    __tablename__ = "test2"
    id = db.Column(db.Integer, primary_key = True)
    otherTableID = db.Column(db.Integer, db.ForeignKey("test.id"))
    name = db.Column(db.Text(64))

    def __repr__(self):
        return "<test2 %r>" % self.name

class Events(db.Model):

    __tablename__ = "events"
    id = db.Column(db.Integer, primary_key = True)
    event_name = db.Column(db.String)
    event_info = db.Column(db.Text(64))
    players_link = db.relationship("players", backref = "players_reference")

class Players(db.Model):

    __tablename__ = "players"
    id = db.Column(db.Integer, primary_key = True)
    #profile_id = db.Column(db.Integer, db.ForeignKey("othertable.id"))
    event_id = db.Column(db.Integer, db.ForeignKey("events.id"))
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    dob = db.Column(db.Date)
    chess_rating = db.Column(db.Integer)