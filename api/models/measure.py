from django.db import models

from .station import Station


class Measure (models.Model):
    station_code = models.ForeignKey(Station, on_delete=models.CASCADE)
    date = models.DateField()
    hour = models.TimeField()
    icqa = models.SmallIntegerField(default=1)
    nom_pollutant = models.CharField(max_length=32, default="No pollutant")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['station_code', 'date', 'hour'], name='measure_unique')
        ]
