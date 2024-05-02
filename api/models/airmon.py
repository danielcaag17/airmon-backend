from django.db import models

from .airmon_type import AirmonType
from .rarity_type import RarityType


class Airmon(models.Model):
    name = models.CharField(max_length=32, primary_key=True)
    description = models.TextField()
    rarity = models.CharField(max_length=32, choices=RarityType.choices, default=RarityType.COMMON)
    type = models.CharField(max_length=32, choices=AirmonType.choices, default=AirmonType.LOREM)
    image = models.ImageField(upload_to='airmons/')

    def save(self, *args, **kwargs):
        # El max length no es valida perque name es PK
        if len(self.name) >= 32:
            raise ValueError("The name must be 32 characters or less.")
        elif self.rarity not in [choice[0] for choice in RarityType.choices]:
            raise ValueError("Invalid rarity value.")
        elif self.type not in [choice[0] for choice in AirmonType.choices]:
            raise ValueError("Invalid type value.")
        else:
            super().save(*args, **kwargs)

