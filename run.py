from webapp import app 									#import from __init__.py file in webapp package the app variable who is an instance of Flask class
from webapp import create_db

if __name__ == '__main__':								#Start the flask server when we do a "python run.py" ib the terminal (we don't need to export some variables)
	app.run(debug=True)