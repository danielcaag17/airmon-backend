from django.db import models

from api.models.station import Station
from api.models.location import LocationGeohash


class SpawnPoint(models.Model):
    location = models.OneToOneField(LocationGeohash, primary_key=True, on_delete=models.PROTECT)
    station = models.ForeignKey(Station, on_delete=models.SET_NULL, null=True)
    minute = models.BigIntegerField()  # This should be between 0 and 59?
