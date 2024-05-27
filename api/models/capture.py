from django.utils.timezone import now
from django.db import models

from .airmon import Airmon
from django.contrib.auth.models import User


class Capture (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    airmon = models.ForeignKey(Airmon, on_delete=models.CASCADE)
    date = models.DateTimeField(default=now, editable=False)

    class Meta:
        unique_together = ('airmon', 'username', 'date')
