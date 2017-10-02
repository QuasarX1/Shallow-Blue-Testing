
from flask_wtf import Form
from wtforms import TextField 
from wtforms import TextAreaField
from wtforms import SubmitField
from wtforms import validators, ValidationError
 
class ContactForm(Form):
  name = TextField("Name",[validators.Required('Please enter your name.')])

  email = TextField("Email",[validators.Email('Please enter a valid email address.')])

  subject = TextField("Subject", [validators.Required('Please enter a subject.')])

  message = TextAreaField("Message", [validators.Required('Please enter your message.')])
  
  submit=SubmitField("submit")

  
