from django.contrib.auth.models import User
import pytz

from ..models import Airmon, Capture, Chat, Item, Pollutant, Measure, Station, Location, LocationGeohash


def create_user(username):
    return User.objects.create_user(username=username)


def create_airmon(name):
    return Airmon.objects.create(name=name)


def create_capture(user, airmon, date, attempts):
    return Capture.objects.create(username=user, airmon=airmon, date=date, attempts=attempts)


def create_chat(user1, user2):
    return Chat.objects.create(user1=create_user(user1), user2=create_user(user2))


def create_item(name, rarity, price, description):
    return Item.objects.create(name=name, rarity=rarity, price=price, description=description)


def create_location(lng, lat):
    return Location.objects.create(longitude=lat, latitude=lng)


def create_location_geohash(geohash):
    return LocationGeohash.objects.create(geohash=geohash)


def create_measure(code, date, hour):
    return Measure.objects.create(station_code=code, date=date, hour=hour)


def create_pollutant(name, measure_unit, recommended_limit):
    return Pollutant.objects.create(name=name, measure_unit=measure_unit, recommended_limit=recommended_limit)


def create_station(code, name, location):
    return Station.objects.create(code=code, name=name, location=location)


def get_timezone():
    return pytz.timezone("Europe/Madrid")
