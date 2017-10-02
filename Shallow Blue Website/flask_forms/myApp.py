# all the imports

import os

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

from forms import ContactForm

app = Flask(__name__) # create the application instance :)

app.secret_key = 'YourSuperSecreteKey'

#####################################################################################################
#added to fix problem of my css not refreshing in cache and associated problem with overriding bootstrap
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)
######################################################################################################


@app.route('/', methods=['GET', 'POST'])
def home():
	form = ContactForm()
	scroll=""

	if request.method == 'POST':
		if form.validate_on_submit():
			flash("Thanks, I'll be in touch.")
			return redirect(url_for('home')+'#contact')
			
		else:
			flash('All fields must be completed correctly.')
			scroll='contact'

	return render_template('home.html', scroll=scroll, form = form)