from datetime import datetime
import pytz
from django.core.exceptions import ValidationError

from django.db import models

from .airmon import Airmon
from django.contrib.auth.models import User


class Capture (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    airmon = models.ForeignKey(Airmon, on_delete=models.CASCADE)
    date = models.DateTimeField()
    attempts = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ('airmon', 'user', 'date')

    def save(self, *args, **kwargs):
        timezone = pytz.timezone("Europe/Madrid")
        if self.date > datetime.now(timezone):
            raise ValueError("The date cannot be in the future.")
        if self.attempts < 0:
            raise ValidationError("The number of attempts must be a positive number.")
        else:
            super().save(*args, **kwargs)
