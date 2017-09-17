"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

import requests

import os
from Classes import *
from Functions import *
import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

baseDir = os.path.abspath(os.path.dirname(__file__))

#dbFileName = input("Database file name:\n")

print("sqlite:///" + os.path.join(baseDir, os.path.join("databases", "testDB.sqlite")))

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(baseDir, os.path.join("databases", "testDB.sqlite"))

app.config["SQLALCHMEY_COMMIT_ON_TEARDOWN"] = True

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app) #Requires the db Variable from Classes\dbModels.py

if not os.path.exists(app.config["SQLALCHEMY_DATABASE_URI"]):
    with app.app_context():
        db.create_all()

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

@app.route('/')
def Main_Page():
    """Renders the main page."""
    return  render_template("MainPage.html", pageTitle = "Main Page", url = "/")

@app.route("/data/news-bar")
def newsBar():
    """Returns the latest news in responce to an AJAX request"""
    time = datetime.datetime.now().time()
    return str(time.hour) + ":" + str(time.minute) #Return query to db as to lates news

if __name__ == '__main__':

    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, threaded = True, debug = False)
