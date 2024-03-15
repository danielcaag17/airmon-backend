from django.db import models

from .measure import Measure
from .pollutant import Pollutant


class PollutantMeasure(models.Model):
    pollutant_name = models.ForeignKey(Pollutant, on_delete=models.CASCADE)
    # measure conte station_code, date i hour de la measure associada
    measure = models.ForeignKey(Measure, on_delete=models.CASCADE)
    quantity = models.FloatField()

    class Meta:
        unique_together = ('pollutant_name', 'measure')
