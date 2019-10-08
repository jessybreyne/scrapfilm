from django.db import models

# Create your models here.

class Movies(models.Model):
    name = models.CharField(max_length=50)
    img = models.URLField(max_length=200)
    rate = models.IntegerField(null=True)
    
    def __str__(self):
        return self.name
