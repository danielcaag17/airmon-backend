from django.db import models

from .airmon import Airmon


class AirmonOnMap(models.Model):
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    airmon = models.ForeignKey(Airmon, on_delete=models.CASCADE)
    expiry_date = models.BigIntegerField()

    class Meta:
        unique_together = ("latitude", "longitude")
