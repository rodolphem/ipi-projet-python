from flask import Flask, render_template, url_for		#importing Flask class from flask package to use flask function
app = Flask(__name__)			#instanciating imported flask class

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

@app.route('/home')				#this two décorator create 2 routes to return the same html code
@app.route('/')					#flask class object ("app") decorator to change de function and generate HTML
def hello():					#decorated function
	return render_template('home.html', posts=posts)

@app.route('/about')			
def about():					
	return render_template('about.html', title='About')


if __name__ == '__main__':		#Start the flask server when we do a "python __init__.py" ib the terminal (we don't need to export some variables)
	app.run(debug=True)
