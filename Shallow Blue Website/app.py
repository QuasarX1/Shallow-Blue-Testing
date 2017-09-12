"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from Classes import *
import datetime
from flask import Flask, render_template
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


#@app.route('/')
#def hello():
#    """Renders a sample page."""
#    return "Hello World!"

@app.route('/')
def Main_Page():
    """Renders a test page."""
    return  render_template("MainPage.html", pageTitle = "Main Page", url = "/")

@app.route("/data/news-bar")
def newsBar():
    """Returns the latest news in responce to an AJAX request"""
    time = datetime.datetime.now().time()
    return str(time.hour) + ":" + str(time.minute) #Return query to db as to lates news

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, threaded = True, debug = True)
