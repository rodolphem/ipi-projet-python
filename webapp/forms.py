from flask_wtf import FlaskForm #importing FlaskForm class to convert Python code in HTML forms
from wtforms import StringField, PasswordField, SubmitField, BooleanField  #allow us to use string fields and password fields in our forms
from wtforms.validators import DataRequired, Length, Email, EqualTo #allow us to verify if the field aren't empty, verify length and email

class RegistrationForm(FlaskForm): #Creating a class inheriting FlaskForm class (it's our form)
	username = StringField('Username', 
							validators=[DataRequired(), Length(min=2, max=20)])	   #We need to instanciate imported classes to create each different fields, the 'Username' variable is the label in the HTML page
	email = StringField('Email',
						 validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password',
									 validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')


class LoginForm(FlaskForm): #Creating a class inheriting FlaskForm class (it's our form)
	email = StringField('Email',
						 validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember Me')		#Generate a cookie to remember the user account
	submit = SubmitField('Sign Up')