from abc import abstractmethod
from typing import Dict
import geohash

from django.db import models
from rest_framework.exceptions import ValidationError
from django.core.validators import RegexValidator


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

    class Meta:
        unique_together = ("latitude", "longitude")


class GeohashValidator(RegexValidator):

    REGEX = r"^[0-9b-hj-km-np-zB-HJ-KM-NP-Z]+$"
    MESSAGE = "The geohash has some non-permitted characters."

    def __init__(self):
        super().__init__(regex=self.REGEX, message=self.MESSAGE)


class LocationGeohashManager(models.Manager):
    """
    This is the manager for the LocationGeohash model.

    """

    @abstractmethod
    def coords_to_geohash(
        latitude: float, longitude: float, precision: int = 12
    ) -> str:
        return geohash.encode(latitude, longitude, precision=precision)

    @abstractmethod
    def geohash_to_coords(geohash_: str) -> Dict[str, float]:
        lat, lon = geohash.decode(geohash_)
        return {"latitude": lat, "longitude": lon}
    
    def create(self, **kwargs):
        new_location = LocationGeohash(**kwargs)
        new_location.full_clean()
        new_location.save()
        return new_location

    def get_starting_by(self, geohash: str):
        return super().filter(geohash__istartswith=geohash)

    def insert_by_coords(self, latitude: float, longitude: float):
        geohash_ = geohash.encode(latitude, longitude)
        return super().create(geohash=geohash_)


# Location refactor with geohashes.
class LocationGeohash(models.Model):
    """
    This model stores locationes based on the geohash encoding.
    A geohash is a string from 1 to 12 base32 characters that represent a fixed area on a map.
    For more information see: https://medium.com/@bkawk/geohashing-20b282fc9655
    """

    geohash = models.CharField(
        max_length=12, primary_key=True, validators=[GeohashValidator()]
    )

    objects = LocationGeohashManager()

    def __str__(self):
        return self.geohash

    # Lowercase geohash
    def save(self, *args, **kwargs):
        self.geohash = self.geohash.lower()
        super(LocationGeohash, self).save(*args, **kwargs)
