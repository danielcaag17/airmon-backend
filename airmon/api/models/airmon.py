from django.db import models

from .airmon_type import AirmonType
from .rarity_type import RarityType


class Airmon (models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    rarity = models.CharField(max_length=32, choices=[(tag, tag.value) for tag in RarityType])
    type = models.CharField(max_length=32, choices=[(tag, tag.value) for tag in AirmonType])
    image = models.ImageField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'rarity', 'type'], name='airmon_unique')
        ]
        # unique_together = ('name', 'rarity', 'type')
