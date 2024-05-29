from django.db import models

from .airmon import Airmon
from .spawn_point import SpawnPoint


class SpawnedAirmon(models.Model):
    spawn_point = models.ForeignKey(SpawnPoint, on_delete=models.CASCADE)
    airmon = models.ForeignKey(Airmon, on_delete=models.CASCADE)
    hour = models.BigIntegerField()  # This should be between 1 and 24?
    variable_latitude = models.FloatField()
    variable_longitude = models.FloatField()

    class Meta:
        unique_together = ("spawn_point", "airmon", "hour")
