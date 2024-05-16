from django.db import models

from .trophy import Trophy
from django.contrib.auth.models import User


class PlayerTrophy(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    trophy = models.ForeignKey(Trophy, on_delete=models.CASCADE)
    date = models.DateTimeField()

    class Meta:
        unique_together = ('username', 'trophy')
