"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from Classes import *
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

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, threaded = True, debug = True)
