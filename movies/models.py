from django.db import models

# Create your models here.

# Class Movie récupéré via du scrapping
class Movies(models.Model):
    name = models.CharField(max_length=50)
    img = models.URLField(max_length=200)
    rate = models.IntegerField(null=True)

    def __str__(self):
        return self.name

# Class Actor qui sera lié à Movie via une troisième class

class Actor(models.Model):
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)