"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

#Imports---------------------------------------------------------------------------------------

import os
from Classes import *
from Functions import *
import datetime
from functools import wraps
from flask import Flask, render_template, url_for, redirect, session
from flask_sqlalchemy import SQLAlchemy

#Create app object-----------------------------------------------------------------------------

app = Flask(__name__)

#Connect to db---------------------------------------------------------------------------------

baseDir = os.path.abspath(os.path.dirname(__file__))

print("sqlite:///" + os.path.join(baseDir, os.path.join("databases", "testDB.sqlite")))

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(baseDir, os.path.join("databases", "testDB.sqlite"))

app.config["SQLALCHMEY_COMMIT_ON_TEARDOWN"] = True

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app) #Requires the db Variable from Classes\dbModels.py

if not os.path.exists(app.config["SQLALCHEMY_DATABASE_URI"]):
    with app.app_context():
        db.create_all()

# Make the WSGI interface available at the top level so wfastcgi can get it.-------------------

wsgi_app = app.wsgi_app

#Decorarors------------------------------------------------------------------------------------

def login_test(test):
    """Tests if a user is logged in."""

    @wraps(test)
    def wrap(*args, **kwargs):

        if "loggedIn" in session:

            return test(*args, loggedIn = True, **kwargs)

        else:

            return test(*args, loggedIn = False, **kwargs)

    return wrap

def login_required(test):
    """Ensures a user is logged in or returns them to the login page."""

    @wraps(test)
    def wrap(*args, **kwargs):

        if "loggedIn" in session:

            return test(*args, loggedIn = True, **kwargs)

        else:

            return redirect(url_for("LoginPage"))

    return wrap

#Routes----------------------------------------------------------------------------------------

@app.route('/')
@login_test
def SplashPage(loggedIn):
    """Renders the splash page that all users first encounter."""

    print(loggedIn)

    if not session:
        loggedIn = False
    else:
        loggedIn = True

    return  render_template("SplashPage.html", pageTitle = "Home", url = "/", loggedIn = loggedIn)

@app.route("/login", methods = ["GET", "POST"])
@login_test
def LoginPage(loggedIn):

    if loggedIn == True:

        return redirect(url_for("SplashPage"))

    else:

        if request.method == "GET":

            return render_template("LoginPage.html")

        else:
            
            session.add(loggedIn = True)

            return None

@app.route("/logout")
def LogoutPage():
    return None

@app.route("/acount")
def AccountPage():
    return None

@app.route("/watch")
def Spectate():
    return None

@app.route("/events")
def EventsPage():
    return None

@app.route('/mainPage')
@login_required
def Main_Page():
    """Renders the main page."""
    return  render_template("MainPage.html", pageTitle = "Main Page", url = "/mainPage")

@app.route("/data/news-bar")
def newsBar():
    """Returns the latest news in responce to an AJAX request"""
    time = datetime.datetime.now().time()
    return str(time.hour) + ":" + str(time.minute) #Return query to db as to lates news

#Run app if executed---------------------------------------------------------------------------

if __name__ == '__main__':

    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    #app.run(HOST, PORT, threaded = True, debug = False)

    """For being viewed by other people (navigate to {my ipV4 adress}:5555/)"""
    import socket
    print(socket.gethostbyname(socket.gethostname()))
    app.run(host = "0.0.0.0", port = 5555, threaded = True)