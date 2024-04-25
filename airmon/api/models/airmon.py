from django.db import models

from .airmon_type import AirmonType
from .rarity_type import RarityType


class Airmon(models.Model):
    name = models.CharField(max_length=32, primary_key=True)
    description = models.TextField()
    rarity = models.CharField(max_length=32, choices=[(tag, tag.value) for tag in RarityType])
    type = models.CharField(max_length=32, choices=[(tag, tag.value) for tag in AirmonType])
    image = models.ImageField(upload_to='airmons/')
