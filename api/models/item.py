from django.db import models

from .rarity_type import RarityType


class Item (models.Model):
    name = models.CharField(max_length=32, primary_key=True)
    rarity = models.CharField(max_length=32, choices=[(tag, tag.value) for tag in RarityType])
    price = models.DecimalField(decimal_places=2, max_digits=7)
    description = models.TextField()
