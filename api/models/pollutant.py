from django.db import models

from .unit_type import UnitType


class Pollutant (models.Model):
    name = models.CharField(max_length=32, primary_key=True)
    measure_unit = models.CharField(max_length=32, choices=UnitType.choices)

    def save(self, *args, **kwargs):
        if self.measure_unit not in [choice[0] for choice in UnitType.choices]:
            raise ValueError("Invalid unit value.")
        else:
            super().save(*args, **kwargs)
