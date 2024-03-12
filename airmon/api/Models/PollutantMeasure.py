from django.db import models

from airmon.api.Models.Measure import Measure
from airmon.api.Models.Pollutant import Pollutant


class PollutantMeasure(models.Model):
    pollutantName = models.ForeignKey(Pollutant, on_delete=models.CASCADE)
    stationCode = models.ForeignKey(Measure, on_delete=models.CASCADE, to_field='stationCode')
    date = models.ForeignKey(Measure, on_delete=models.CASCADE, to_field='date')
    hour = models.ForeignKey(Measure, on_delete=models.CASCADE, to_field='hour')
    quantity = models.FloatField()

    class Meta:
        unique_together = ('pollutantName', 'stationCode', 'date', 'hour')
