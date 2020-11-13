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


@app.route('/account', methods=['GET', 'POST'])
@login_required																								# login is required to acces this page																		
def account():
	form = UpdateAccountForm()
	if form.validate_on_submit():
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

