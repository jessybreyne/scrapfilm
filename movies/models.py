from django.db import models
from datetime import datetime
import http.client

import requests
from bs4 import BeautifulSoup

from dateutil import parser
# Create your models here.

# Class Movie récupéré via du scrapping
class Movies(models.Model):
    name = models.CharField(max_length=50)
    img = models.URLField(null=True)
    rate = models.FloatField(null=True)
    years = models.DateField(null=True,auto_now=False, auto_now_add=False)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name+" "+self.years.strftime("%Y-%m-%d")

    def get_actors(self):
        return self.movie_has_actor_set.all()

    def get_commentaires(self):
        return self.commentaire_set.all()

# Class Actor qui sera lié à Movie via une troisième class

class Actor(models.Model):
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    img = models.URLField(null=True)

    def __str__(self):
        return self.first_name+" "+self.surname

#Un acteur est lié à un film, 
#un film peut avoir plusieurs acteurs, un acteur peut avoir plusieurs film

class Movie_has_Actor(models.Model):
    movie = models.ForeignKey("Movies", on_delete=models.CASCADE)
    acteur = models.ForeignKey("Actor", on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.name + " : " + self.acteur.first_name
#URL_IMG = "https://image.tmdb.org/t/p/w500/"
class ScrappingLoader():
    @staticmethod
    def scrap(nbPages):
        listeDesFilms = []

        # 500 pags au total, on parcours les pages, ici on fait seulement nbPages pages
        for page in range(1,nbPages+1):
            url = requests.get('https://www.themoviedb.org/movie?page={}'.format(page))
            soup = BeautifulSoup(url.text, "lxml")
            div = soup.select("div.item.poster.card")

            # On parcours les films de la page
            for i in range(20):
                titre = div[i].findAll("a", {"class": "title"})
                note = div[i].findAll("div", {"class": "user_score_chart"})
                dateNiveauUn = div[i].findAll("div", {"class":"flex"})
                date = dateNiveauUn[0].findAll("span")
                img = div[i].findAll("img", {"class": "poster"})
                resume = div[i].findAll("p", {"class": "overview"})
                
                # La donnée propre
                titreDuFilm = titre[0].get_text()
                print("-> "+titreDuFilm)
                noteDuFilm = note[0]["data-percent"]
                dateDuFilm = date[0].get_text()
                if img:
                        imageDuFilm = img[0]["data-src"]
                else:
                        imageDuFilm = None
                resumeDuFilm = resume[0].get_text()

                lien = titre[0]['href']
                url2 = requests.get('https://www.themoviedb.org{}'.format(lien))
                soup2 = BeautifulSoup(url2.text, "lxml")
                acteurs = soup2.select("ol.people.scroller")
                if acteurs:
                        li = acteurs[0].findAll('li')
                
                ListActeurs = []

                # On parcours les acteurs
                for nb in range(len(li)):
                        
                        imgacteur = li[nb].findAll("img")
                        nomacteur = li[nb].findAll("a")
                        roleacteur = li[nb].findAll("p", {"class": "character"})

                        if imgacteur:
                                imageDeActeur = imgacteur[0]['data-src']
                        else:
                                imageDeActeur = None
                        nomDeActeur = nomacteur[1].get_text()
                        roleDeActeur = roleacteur[0].get_text()

                        DicoActeur = {
                                "nom": nomDeActeur,
                                "role": roleDeActeur,
                                "image": imageDeActeur,

                        }
                        ListActeurs.append(DicoActeur)
                video = soup2.select("a.no_click.play_trailer")
                if video:
                        keyvideo = video[0]['data-id']
                else:
                        keyvideo = None

                film = {
                        "titre": titreDuFilm, 
                        "note": noteDuFilm,
                        "date": dateDuFilm,
                        "image": imageDuFilm,
                        "resume": resumeDuFilm,
                        "video": keyvideo,
                        "acteurs": ListActeurs
                }
                
                listeDesFilms.append(film)
        return listeDesFilms
    @staticmethod
    def toDb(nbPages):
        listeDesFilms = ScrappingLoader().scrap(nbPages)
        for film in listeDesFilms:
                leFilm = Movies.objects.create(name=film["titre"],img=film["image"],rate=film["note"],years=parser.parse(film["date"]),description=film["resume"])
                for acteur in film["acteurs"]:
                        leActeur = Actor.objects.create(first_name=acteur["nom"], surname=acteur["role"], img=acteur["image"])
                        Movie_has_Actor.objects.create(movie=leFilm,acteur=leActeur)

class Commentaire(models.Model):
    username = models.CharField(max_length=50)
    commentaire = models.TextField(null=True)
    movie_id = models.ForeignKey("Movies", on_delete=models.CASCADE)