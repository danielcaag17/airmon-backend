from django.db import models


class Item (models.Model):
    nom = models.CharField(max_length=100)
    # raresa = models.IntegerField()
    preu = models.IntegerField()
    descripcio = models.IntegerField()




