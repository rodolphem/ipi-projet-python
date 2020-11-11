from flask import render_template, url_for, flash, redirect # import from flask some used
from webapp import app
from webapp.forms import RegistrationForm, LoginForm			#importing form classes created in forms.py file in this same directory
from webapp.models import User, Post 								#under db instanciation to avoid circulare import


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
	form = RegistrationForm()							#instanciating form class created in forms.py
	if form.validate_on_submit():						#to know if the account is created or not
		flash(f'Account created for {form.username.data}!', 'success')	#if the form is correctly validate then show this message "account created..."
		return redirect (url_for('home'))								#and redirect to home page
	return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])			
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com' and form.password.data == 'password':
			flash('You have been logged in!', 'success')
			return redirect (url_for('home'))
		else:
			flash('Login Unsuccessful. Please check username and password', 'danger')

	return render_template('login.html', title='Login', form=form)

