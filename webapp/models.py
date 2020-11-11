from datetime import datetime 							# to use datetime functions
from webapp import db 								# __main__ represent webapp file to avoid circulare import

class User(db.Model):									#Create a Table named 'user' (in lowercase) inheriting from db.Model
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)
	posts = db.relationship('Post', backref='author', lazy=True)					#Define the relationship with the post (to make a foreign key in Post table)

	def __repr__(self):
		return f"User('{self.username}', '{self.email}', '{self.image_file}')"				#return the user's atributes
	

class Post(db.Model):									#Create a Table named 'post' (in lowercase) inheriting from db.Model
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100),nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return f"Post('{self.title}', '{self.date_posted}')"				#return the user's atributes