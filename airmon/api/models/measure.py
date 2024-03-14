from django.db import models

from airmon.api.models.station import Station


class Measure (models.Model):
    # Si s'elimina la estacio, per cascada s'elimina les mesures que estiguin relacionades
    station_code = models.ForeignKey(Station, on_delete=models.CASCADE)
    date = models.DateField()
    hour = models.TimeField()

    class Meta:
        unique_together = ('station_code', 'date', 'hour')
