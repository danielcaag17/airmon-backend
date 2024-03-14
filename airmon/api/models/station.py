from django.db import models

from airmon.api.models.location import Location


class Station (models.Model):
    code = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=32)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL)
