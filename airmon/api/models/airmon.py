from django.db import models

from airmon.api.models.airmon_type import AirmonType
from airmon.api.models.rarity_type import RarityType


class Airmon (models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    rarity = models.CharField(max_length=32, choices=[(tag, tag.value) for tag in RarityType])
    type = models.CharField(max_length=32, choices=[(tag, tag.value) for tag in AirmonType])
    image = models.ImageField()

    class Meta:
        unique_together = ('nom', 'rarity', 'type')
