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
from flask import Flask, render_template, url_for, redirect, session, request
from flask_sqlalchemy import SQLAlchemy

#Create app object-----------------------------------------------------------------------------

app = Flask(__name__)

#Configure secret key-------------------------------------------------------------------------

app.config["SECRET_KEY"] = "Random string"

#Connect to db---------------------------------------------------------------------------------

baseDir = os.path.abspath(os.path.dirname(__file__))

print("sqlite:///" + os.path.join(baseDir, os.path.join("databases", "testDB.sqlite")))

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(baseDir, os.path.join("databases", "shallowBlueDB.sqlite"))

app.config["SQLALCHMEY_COMMIT_ON_TEARDOWN"] = True

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app) #Requires the db Variable from Classes\dbModels.py

if __name__ == '__main__':

    if not os.path.exists(app.config["SQLALCHEMY_DATABASE_URI"]):
        with app.app_context():
            db.create_all()
            addEvent("eventName", datetime.datetime.now(), "info")

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

    return  render_template("SplashPage.html", pageTitle = "Home", url = "/", loggedIn = loggedIn)

@app.route("/login", methods = ["GET", "POST"])
@login_test
def LoginPage(loggedIn):

    form = LoginForm()

    if loggedIn == True:

        return redirect(url_for("SplashPage"))

    else:

        if form.validate_on_submit():

            #query db

            #if data matches
            
            session["loggedIn"] = True
            #session["userID"] =
            #session["userName"] =

            return redirect(url_for("SplashPage"))

        return render_template("LoginPage.html", pageTitle = "Login", form = form)

@app.route("/signup", methods = ["GET", "POST"])
@login_test
def SignupPage(loggedIn):

    form = SignupForm()

    if loggedIn == True:

        return redirect(url_for("SplashPage"))

    else:

        if form.validate_on_submit():

            #query db

            #if data dosen't conflict

            #add data to db
            
            session["loggedIn"] = True
            #session["userID"] =
            #session["userName"] =

            return redirect(url_for("SplashPage"))

        return render_template("SignupPage.html", pageTitle = "Login", form = form)

@app.route("/logout")
@login_test
def LogoutPage(loggedIn):
    
    if loggedIn == True:

        session.pop("loggedIn")
        #session.pop("userID")
        #session.pop("userName")

    return redirect(url_for("SplashPage"))

@app.route("/acount")
def AccountPage():
    return ""

@app.route("/watch")
def Spectate():
    return ""

@app.route("/events")
def EventsPage():
    return ""

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
    app.run(HOST, PORT, threaded = True, debug = False)

    """For being viewed by other people (navigate to {my ipV4 adress}:5555/)"""
    #import socket
    #print("http://" + socket.gethostbyname(socket.gethostname()) + ":5555/")
    #app.run(host = "0.0.0.0", port = 5555, threaded = True)