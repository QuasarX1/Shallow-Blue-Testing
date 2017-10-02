from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField, ValidationError
from wtforms.validators import EqualTo, Email, InputRequired, Required

class NameForm(FlaskForm):

    name = StringField("What is your name", validators = [InputRequired()])

    submit = SubmitField("Submit")

class LoginForm(FlaskForm):

    userName = StringField("Username", validators = [Required(message="This is a required field")])

    password = PasswordField("Password", validators = [Required(message="This is a required field")])

    loginButton = SubmitField("Login")

class SignupForm(FlaskForm):

    userName = StringField("Username", validators = [InputRequired(message="This is a required field")])

    email = StringField("Email", validators = [InputRequired(message="This is a required field"), Email()])

    password = PasswordField("Password", validators = [InputRequired(message="This is a required field")])

    passwordRepeat = PasswordField("Repeat Password", validators = [InputRequired(message="This is a required field"), EqualTo("password", message='Passwords must match')])

    signupButton = SubmitField("Signup")

class SpectateForm(FlaskForm):

    eventID = IntegerField("Event ID", validators = [InputRequired()])