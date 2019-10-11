# ScrapFilm

Une application web permettant de visualiser des films

Installation
======

- Cr�er une virtual env avec la commande : 
	virtualenv venv -p python3
	
- Activer le venv :
	source {path}/venv/bin/activate

- Installer les packages :
	pip install -r requirements.txt

- Installer les fichiers static :
	yarn install

- Cr�ation de la BD :
	./manage.py migrate
	
Lancement de l'application
======

- Cr�ation d'un superUser :
	./manage.py createsuperuser
	
- Dans le dossier scrapfilm lancer le serveur:
	./manage.py runserver