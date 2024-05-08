from django.db import models

from .trophy_type import TrophyType


class Trophy(models.Model):
    name = models.CharField(max_length=32)
    type = models.CharField(max_length=32, choices=TrophyType.choices, default=TrophyType.BRONZE)
    xp = models.PositiveIntegerField()

    class Meta:
        unique_together = ('name', 'type')
