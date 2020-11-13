from flask import Flask									#importing Flask class from flask package to use flask function and class
from flask_sqlalchemy import SQLAlchemy 				#importing SQLAlchemy to manage our database
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)									#instanciating imported flask class
app.config['SECRET_KEY'] = '51790f49aa35845942c29ff82df9f8c8'  #Secret key to secure our app like modifying cookies etc
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'	   # specify the relative route of the database
db = SQLAlchemy(app) 										   #Creating SQLAlchemy instance
bcrypt = Bcrypt(app)										#Creating Bcrypt instance to manage hashing password
login_manager = LoginManager(app)							# to manage user's session
login_manager.login_view = 'login'							#allow us to force the user to login before access to different pages
login_manager.login_message_category = 'info'				#change the apparence of different info message 

from webapp import routes