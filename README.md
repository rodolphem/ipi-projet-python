app

################# LANCEMENT DE L'APPLICATION #######################

si les lignes :

if __name__ == '__main__':
	app.run(debug=True)

ne sont pas présentes, alors faire les deux manipulation ci dessous :

pour démarer le serveur : export FLASK_APP=__init__.py

pour activer le debugger : export FLASK_DEBUG=1

###################################################################


installation de flask dans un environnement virtuel : pip install flask

installation de WT forms : pip install flask-wtf

installation de sqlalchemy : pip install flask-sqlalchemy

installation de flask login : pip install flask-login

###################### Syntaxe ##################################

J'utilise sublime text, j'ai télécharger le package jinja2 pour avoir la coloration syntaxique des action dans les pages HTML