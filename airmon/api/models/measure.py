from django.db import models

from .station import Station


class Measure (models.Model):
    # Si s'elimina la estacio, per cascada s'elimina les mesures que estiguin relacionades
    station_code = models.ForeignKey(Station, on_delete=models.CASCADE, null=True)
    date = models.DateField()
    hour = models.TimeField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['station_code', 'date', 'hour'], name='measure_unique')
        ]
        # unique_together = ('station_code', 'date', 'hour')
