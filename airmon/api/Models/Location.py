from django.contrib.auth.hashers import make_password, check_password
from django.db import models

from airmon.api.Models.Language import Language


class Location (models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    class PK:
        unique_together = ('latitude', 'longitude')
