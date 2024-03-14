from django.db import models

from airmon.api.models.measure import Measure
from airmon.api.models.pollutant import Pollutant


class PollutantMeasure(models.Model):
    pollutant_name = models.ForeignKey(Pollutant, on_delete=models.CASCADE)
    station_code = models.ForeignKey(Measure, on_delete=models.CASCADE, to_field='stationCode')
    date = models.ForeignKey(Measure, on_delete=models.CASCADE, to_field='date')
    hour = models.ForeignKey(Measure, on_delete=models.CASCADE, to_field='hour')
    quantity = models.FloatField()

    class Meta:
        unique_together = ('pollutant_name', 'station_code', 'date', 'hour')
