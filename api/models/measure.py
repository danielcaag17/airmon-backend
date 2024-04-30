from django.db import models

from .station import Station


class Measure (models.Model):
    # Si s'elimina la estacio, per cascada s'elimina les mesures que estiguin relacionades
    station_code = models.ForeignKey(Station, on_delete=models.CASCADE)
    date = models.DateField()
    hour = models.TimeField()
    val_color = models.SmallIntegerField(default=0)
    nom_pollutant = models.CharField(max_length=32, default="No pollutant")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['station_code', 'date', 'hour'], name='measure_unique')
        ]
        # unique_together = ('station_code', 'date', 'hour')
