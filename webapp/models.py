from datetime import datetime 							# to use datetime functions
from webapp import db, login_manager 								#importing some instance from __init__.py
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(user_id)


class User(db.Model, UserMixin):									#Create a Table named 'user' (in lowercase) inheriting from db.Model
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)
	points = db.Column(db.Integer, default=0)
	questions = db.relationship('Questions', backref='author', lazy=True)					#Define the relationship with the post (to make a foreign key in Post table)

	def __repr__(self):
		return f"User('{self.username}', '{self.email}', '{self.image_file}')"				#return the user's atributes
	

class Questions(db.Model):									#Create a Table named 'post' (in lowercase) inheriting from db.Model
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(20), nullable=False)
	points = db.Column(db.Integer, nullable=False)
	response = db.Column(db.String(50), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return f"Post('{self.nom_hero}', '{self.results}')"				#return the user's atributes