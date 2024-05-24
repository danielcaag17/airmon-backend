from decimal import Decimal, ROUND_DOWN
from django.apps import apps

from ..models import LocationGeohash


def get_geohash(element):
    longitude = round_decimal(Decimal(element["longitud"]), 6)
    latitude = round_decimal(Decimal(element["latitud"]), 6)

    # Transformar coordenades a geohash
    geohash = LocationGeohash.objects.coords_to_geohash(latitude=latitude, longitude=longitude)

    if (loc := _check_model_exists("LocationGeohash", geohash=geohash)) is None:
        loc = LocationGeohash.objects.create(geohash=geohash)
    return loc


def round_decimal(value, decimal_places):
    return value.quantize(Decimal(10) ** -decimal_places, rounding=ROUND_DOWN)


def _check_model_exists(model_name, **kwargs):
    """
    Checks if a model exists in the database
    """
    model = apps.get_model('api', model_name)
    res = model.objects.filter(**kwargs).first()
    return res