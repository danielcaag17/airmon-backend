from django.db import models


class Pollutant (models.Model):
    name = models.CharField(max_length=32, primary_key=True)
    measureUnit = models.CharField(max_length=32, choices=[(tag, tag.value) for tag in UnitType])
    recommendedLimit = models.FloatField()
