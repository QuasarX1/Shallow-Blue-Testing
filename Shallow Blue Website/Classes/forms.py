from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, IntegerField, SubmitField
from wtforms.validators import Required, EqualTo

class NameForm(Form):

    name = StringField("What is your name", validators = [Required()])

    submit = SubmitField("Submit")

class LoginForm(Form):

    userName = StringField("Username", validators = [Required()])

    password = PasswordField("Password", validators = [Required()])

    loginButton = SubmitField("Login")

class SignupForm(Form):

    userName = StringField("Username", validators = [Required()])

    password = PasswordField("Password", validators = [Required()])

    passwordRepeat = PasswordField("Repeat Password", validators = [Required(), EqualTo("password", message='Passwords must match')])

    signupButton = SubmitField("Signup")

class SpectateForm(Form):

    eventID = IntegerField("Event ID", validators = [Required()])