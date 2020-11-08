from flask import Flask 		#importing Flask class from flask package to use flask function
app = Flask(__name__)			#instanciating imported flask class


@app.route('/home')	
@app.route('/')					#flask class object ("app") decorator to change de function and generate HTML
def hello():					#decorated function
	return "Hello World"

@app.route('/about')			
def about():					
	return "<h1>About Page</h1>"


if __name__ == '__main__':		#Start the flask server when we do a "python __init__.py" ib the terminal (we don't need to export some variables)
	app.run(debug=True)
