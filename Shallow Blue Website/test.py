import datetime
import app
from Functions.dbFunctions import *
addEvent(app.app, "Event Name", datetime.datetime.now(), "Info")
