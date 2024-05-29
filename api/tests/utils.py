from django.contrib.auth.models import User
import pytz


from ..models import (Airmon, Capture, Chat, Event, Item, Location, LocationGeohash, Measure, Pollutant,
                      Station, Trophy, PlayerItem)


def create_user(username):
    return User.objects.create_user(username=username)


def create_airmon(name):
    return Airmon.objects.create(name=name)


def create_capture(user, airmon):
    return Capture.objects.create(user=user, airmon=airmon)


def create_chat(user1, user2):
    return Chat.objects.create(user1=create_user(user1), user2=create_user(user2))


def create_event(codi, denominacio, data_ini, data_fi, geohash, espai):
    return Event.objects.create(codi=codi, denominacio=denominacio, data_ini=data_ini,
                                data_fi=data_fi, geohash=geohash, espai=espai)


def create_item(name, price, description, image, duration):
    return Item.objects.create(name=name, price=price, description=description, image=image, duration=duration)


def create_location(lng, lat):
    return Location.objects.create(longitude=lat, latitude=lng)


def create_location_geohash(geohash):
    return LocationGeohash.objects.create(geohash=geohash)


def create_measure(code, date, hour):
    return Measure.objects.create(station_code=code, date=date, hour=hour)


def create_player_item(user, item, quantity):
    return PlayerItem.objects.create(user=user, item_name=item, quantity=quantity)


def create_pollutant(name, measure_unit):
    return Pollutant.objects.create(name=name, measure_unit=measure_unit)


def create_station(code, name, location):
    return Station.objects.create(code=code, name=name, location=location)


def create_trophy(name, tipus, description, requirement, xp):
    return Trophy.objects.create(name=name, type=tipus, description=description, requirement=requirement, xp=xp)


def get_timezone():
    return pytz.timezone("Europe/Madrid")
