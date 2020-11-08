from flask import Flask 				#import class Flask from flask package


app = Flask(__name__)					#instanciation of the Flask class in a variable named app

@app.route('/')							#this decorator make the simply function a flask function who return html
def hello_world():						#this function can return html with the decorator
    return 'Hello, World!'



if __name__ == '__main__':				#if the file is executed then do app.run() (to start the flask server)
	app.run()