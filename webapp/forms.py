from flask_wtf import FlaskForm #importing FlaskForm class to convert Python code in HTML forms
from wtforms import StringField, PasswordField, SubmitField, BooleanField  #allow us to use string fields and password fields in our forms
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError #allow us to verify if the field aren't empty, verify length and email
from webapp.models import User

class RegistrationForm(FlaskForm): #Creating a class inheriting FlaskForm class (it's our form)
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])	   #We need to instanciate imported classes to create each different fields, the 'Username' variable is the label in the HTML page
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')

	def validate_username(self, username):										#Verify if the username is already taken in the database
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('That username is already taken.')

	def validate_email(self, email): 											#Verify if the email is already taken in the database
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('That email is already taken.')


class LoginForm(FlaskForm): #Creating a class inheriting FlaskForm class (it's our form)
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember Me')		#Generate a cookie to remember the user account
	submit = SubmitField('Sign Up')