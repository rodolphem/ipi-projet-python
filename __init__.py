from flask import Flask 		#importing Flask class from flask package to use flask function
app = Flask(__name__)			#instanciating imported flask class

@app.route('/')					#flask class object ("app") decorator to change de function and generate HTML
def hello():					#decorated function
	return "Hello World"