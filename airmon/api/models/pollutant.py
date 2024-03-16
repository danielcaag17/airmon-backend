from django.db import models

from .unit_type import UnitType


class Pollutant (models.Model):
    name = models.CharField(max_length=32, primary_key=True)
    measure_unit = models.CharField(max_length=32, choices=[(tag, tag.value) for tag in UnitType])
    recommended_limit = models.FloatField()
