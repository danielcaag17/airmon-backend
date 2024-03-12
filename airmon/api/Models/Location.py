from django.db import models
from rest_framework.exceptions import ValidationError


# RT11 garantida
def validate_longitude(value):
    if value < -180 or value > 180:
        raise ValidationError("Longitude must be between -180 and 180")


# RT12 garantida
def validate_latitude(value):
    if value < -90 or value > 90:
        raise ValidationError("Latitude must be between -90 and 90")


class Location (models.Model):
    longitude = models.DecimalField(max_digits=9, decimal_places=6, validators=[validate_longitude])
    latitude = models.DecimalField(max_digits=9, decimal_places=6, validators=[validate_latitude])

    class PK:
        unique_together = ('latitude', 'longitude')
