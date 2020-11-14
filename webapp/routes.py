import os 					#we use that to grab files extension
import secrets 				# to generate a random token
from PIL import Image		# to resize Image
from flask import render_template, url_for, flash, redirect, request # import from flask some used
from webapp import app, db, bcrypt
from webapp.forms import RegistrationForm, LoginForm, UpdateAccountForm			#importing form classes created in forms.py file in this same directory
from webapp.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required			# to manage connexion 


posts = [
	{
		'author': 'Corey schafer',
		'title': 'Blog post 1',
		'content': 'first post content',
		'date': 'April 20, 2018'
	},
	{
		'author': 'Jane Doe',
		'title': 'Blog post 2',
		'content': 'second post content',
		'date': 'April 21, 2018'
	}
]


@app.route('/home')										#this two décorator create 2 routes to return the same html code
@app.route('/')											#flask class object ("app") decorator to change de function and generate HTML
def home():												#decorated function
	return render_template('home.html', posts=posts)    #return home.html and give it a variable posts


@app.route('/about')			
def about():					
	return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])			
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = RegistrationForm()																		#instanciating form class created in forms.py
	if form.validate_on_submit():																	#to know if the account is created or not
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')			#hashing the password
		user = User(username=form.username.data, email=form.email.data, password=hashed_password)	#Creating a User instaciation who contain information enter in the form variable
		db.session.add(user)																		#Adding the user to be ready to be commit in the database
		db.session.commit()																			#Add the data to the database
		flash('Your account has been created! You are now able to log in', 'success')								#if the form is correctly validate then show this message "account created..."
		return redirect (url_for('login'))															#and redirect to home page
	return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])			
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()											#Check if the email is present in the database
		if user and bcrypt.check_password_hash(user.password, form.password.data):							#Check if the user variable is present and if the password in the database is equal to the form password
			login_user(user, remember=form.remember.data) 													#check if the user want the webapp to remember his password or no and connect him
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('home')) 							#redirect automaticaly to the page we wanted to access after login if we can't access this page before
		else:
			flash('Login Unsuccessful. Please check your email and password', 'danger')

	return render_template('login.html', title='Login', form=form)


@app.route('/logout')																						#to disconnect the user and redirect to home page
def logout():
	logout_user()
	return redirect(url_for('home'))


def save_picture(form_picture): 															# function to save picture
	random_hex = secrets.token_hex(8) 												#make a random token to use this as a name
	_, f_ext = os.path.splitext(form_picture.filename) 								# grab the extension of the picture in parameter
	picture_fn = random_hex + f_ext 												#make a filename for the picture with the random token and the file extension
	picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)  # path to save picture : static/profile_pics directory
	output_size = (125, 125) 			# choose a size
	i = Image.open(form_picture)		# create an instance to resize the picture
	i.thumbnail(output_size)			#resize the picture with the selected size

	i.save(picture_path) 				#save the picture

	return picture_fn  					# return the path name


@app.route('/account', methods=['GET', 'POST'])
@login_required																								# login is required to acces this page																		
def account():
	form = UpdateAccountForm()
	if form.validate_on_submit():
		if form.picture.data:     							#if a data is in the picture field
			picture_file = save_picture(form.picture.data) #using the save_picture function coded before to save picture
			current_user.image_files = picture_file        # /!\ supposed to change the image file in the database but don't work I don't know why  
		current_user.username = form.username.data
		current_user.email = form.email.data
		db.session.commit()
		flash('Your account has been updated', 'success')
		return redirect(url_for('account'))
	elif request.method == 'GET':								#to write current user's informations when we go to the profile page
		form.username.data = current_user.username
		form.email.data = current_user.email
	image_file = url_for('static', filename='profile_pics/' + current_user.image_file) 						# Create a variable containing the profile pic of the user
	return render_template('account.html', title='Account', image_file=image_file, form=form)

