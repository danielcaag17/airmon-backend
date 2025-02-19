from django.db import models

from .location import LocationGeohash


class Event(models.Model):
    codi = models.CharField(primary_key=True, max_length=32)
    denominacio = models.CharField(max_length=256, default="")
    data_ini = models.DateTimeField()
    data_fi = models.DateTimeField()
    geohash = models.ForeignKey(LocationGeohash, on_delete=models.CASCADE)
    espai = models.TextField()
