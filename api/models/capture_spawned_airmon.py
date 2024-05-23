from datetime import datetime
import pytz
from django.core.exceptions import ValidationError

from django.db import models

from .spawned_airmon import SpawnedAirmon
from .player import Player


class CaptureSpawnedAirmon (models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    spawned_airmon = models.ForeignKey(SpawnedAirmon, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('player', 'spawned_airmon')
