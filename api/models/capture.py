from datetime import datetime
import pytz
from django.core.exceptions import ValidationError

from django.db import models

from .airmon import Airmon
from django.contrib.auth.models import User


class Capture (models.Model):
    # En cas que s'elimini l'Airmon o l'Usuari s'elimen totes les captures que es relacionen
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    # airmon conte name, rarity i type de l'airmon associat
    airmon = models.ForeignKey(Airmon, on_delete=models.CASCADE)
    date = models.DateTimeField()
    attempts = models.PositiveSmallIntegerField()

    # Clau primaria User+Data o User+Airmon
    class Meta:
        unique_together = ('airmon', 'username', 'date')

    def save(self, *args, **kwargs):
        timezone = pytz.timezone("Europe/Madrid")
        if self.date > datetime.now(timezone):
            raise ValueError("The date cannot be in the future.")
        if self.attempts < 0:
            raise ValidationError("The number of attempts must be a positive number.")
        else:
            super().save(*args, **kwargs)
