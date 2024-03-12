from django.db import models

from airmon.api.Models.Station import Station


class Measure (models.Model):
    # Si s'elimina la estacio, per cascada s'elimina les mesures que estiguin relacionades
    stationCode = models.ForeignKey(Station, on_delete=models.CASCADE)
    date = models.DateField()
    hour = models.TimeField()

    class Meta:
        unique_together = ('stationCode', 'date', 'hour')
