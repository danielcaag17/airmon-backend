from django.db import models

from .location import Location


class Station (models.Model):
    code = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=64)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
