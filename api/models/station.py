from django.db import models

from .location import LocationGeohash


class Station (models.Model):
    code = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=64)
    location = models.ForeignKey(LocationGeohash, on_delete=models.SET_NULL, null=True, unique=True)
    # location = models.OneToOneField(LocationGeohash, on_delete=models.SET_NULL)
