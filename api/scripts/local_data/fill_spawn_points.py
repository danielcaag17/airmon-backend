import random
from api.scripts.django_setup import setup_django

setup_django()

from api.models.location import LocationGeohash
from api.models.spawn_point import SpawnPoint
from api.utils.icqa_by_area import get_nearest_station

barcelona_geohashes = [
    "sp3ef",
    "sp3e8",
    "sp3e9",
    "sp3ed",
    "sp3e2",
    "sp3e3",
    "sp3e0",
    "sp37r",
    "sp37p",
]
geohash_characters = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "j",
    "k",
    "m",
    "n",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

locations = []
spawn_points = []
for base_geohash in barcelona_geohashes:
    for c1 in geohash_characters:
        for c2 in geohash_characters:
            final_geohash = f"{base_geohash}{c1}{c2}"
            location = LocationGeohash(geohash=final_geohash)
            locations.append(location)
            station = get_nearest_station(location)
            minute = random.randint(0, 59)
            spawn_points.append(SpawnPoint(location=location, station=station, minute=minute))
LocationGeohash.objects.bulk_create(locations, ignore_conflicts=True)
SpawnPoint.objects.bulk_create(spawn_points, ignore_conflicts=True)
