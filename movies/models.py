from django.db import models
from datetime import datetime
# Create your models here.

# Class Movie récupéré via du scrapping
class Movies(models.Model):
    name = models.CharField(max_length=50)
    img = models.URLField(max_length=200)
    rate = models.IntegerField(null=True)
    years = models.DateField(null=True,auto_now=False, auto_now_add=False)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name+" "+self.years.strftime("%Y-%m-%d")

# Class Actor qui sera lié à Movie via une troisième class

class Actor(models.Model):
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    img = models.URLField(max_length=200)

    def __str__(self):
        return self.first_name+" "+self.surname
        
#Un acteur est lié à un film, 
#un film peut avoir plusieurs acteurs, un acteur peut avoir plusieurs film

class Movie_has_Actor(models.Model):
    movie = models.ForeignKey("Movies", on_delete=models.CASCADE)
    acteur = models.ForeignKey("Actor", on_delete=models.CASCADE)
