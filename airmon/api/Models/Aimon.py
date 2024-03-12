from django.db import models


class Airmon(models.Model):
    nom = models.CharField(max_length=100)
    description = models.IntegerField()
    raresa = models.IntegerField()
    tipus = models.CharField(max_length=100)
    imatge = models