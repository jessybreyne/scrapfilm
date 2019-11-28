# ScrapFilm

Une application web permettant de visualiser des films

Installation
======

- Créer une virtual env avec la commande : 
	virtualenv venv -p python3
	
- Activer le venv :
	source {path}/venv/bin/activate

- Installer les packages :
	pip install -r requirements.txt

- Installer les fichiers static :
	cd static
	yarn install

- Création de la BD :
	./manage.py migrate
	
Lancement de l'application
======

- Création d'un superUser :
	./manage.py createsuperuser
	
- Dans le dossier scrapfilm lancer le serveur:
	./manage.py runserver

Features importantes
======

- Ajout / Modification / Supprimer Movies via Admin
- Ajout / Modification / Supprimer Actor via Admin
- Ajout / Modification / Supprimer Movie_has_Actor via Admin (FOREIGN KEY)

- Scrapping directement depuis l'admin via une interface ( nombre de page à scrap + submit )

- Ajout / Supprimer un commentaire via l'interface utilisateur
- Chaque film peut avoir des commentaires ( FOREIGN KEY )

- Recherche rapide , films ou acteurs

- Liste des films
- Liste des acteurs

- Details des films
- Details des acteurs