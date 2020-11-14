app

################# LANCEMENT DE L'APPLICATION #######################

python run.py

si les lignes :

if __name__ == '__main__':
	app.run(debug=True)

ne sont pas présentes, alors faire les deux manipulation ci dessous :

pour démarer le serveur : export FLASK_APP=run.py

pour activer le debugger : export FLASK_DEBUG=1

###################################################################


installation de flask dans un environnement virtuel : pip install flask

installation de WT forms : pip install flask-wtf					(pour les formulaires)

installation de sqlalchemy : pip install flask-sqlalchemy			(Pour la base de données)

installation de email validator : pip install email_validator 		(pour la vérification des email)

installatiob de bcrypt : pip install flask-bcrypt					(pour le hashage de mot de passe)

installation de login : pip install flask-login						(pour la gestion des sessions des utilisateurs)

installastion de Pillow : pip install Pillow 						(pour la redimension des images)

###################### BDD ##################################

Création de la base de données : avoir l'environnement virtuel activé et etre dans le dossier de l'application, ensuite ouvrire le terminal et lancer python, utilisé la commande 'from webapp import db', et db.create_all()

pour supprimer la base de données : db.drop_all() dans le terminal après avoir importé la classe db

###################### Syntaxe ##################################

J'utilise sublime text, j'ai télécharger le package jinja2 pour avoir la coloration syntaxique des action dans les pages HTML


###################### Erreurs courante ##################################

Attention au circulare import avec le fichier webapp.py quand on essaye d/ importé un fichier aui lui même import le fichier dans lequel on souhaite l'importé (en gros les deux fichier s'importe l'un et l'autre), c'est une source de bug lorsque l'ont lance notre application avec python
(Le problème est du au fait que python appel le fichier que l'ont lance, donc webapp.py en __main__ donc quand il voit import from webapp il tourne en rond): la solution est de faire remplacer webapp dans l'import par __main__ exemple : from __main__ import db, et de bouger les déclaration en fonction de leurs ordre d'éxecution