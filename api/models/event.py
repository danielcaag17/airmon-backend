from django.db import models

from .location import LocationGeohash

class Event(models.Model):
    codi = models.CharField(primary_key=True, max_length=32)
    denominacio = models.TextField()
    # descripcio = models.TextField()
    data_ini = models.DateTimeField()
    data_fi = models.DateTimeField()
    geohash = models.ForeignKey(LocationGeohash, on_delete=models.CASCADE)
    imatge = models.ImageField(upload_to='events/')
    espai = models.TextField()
