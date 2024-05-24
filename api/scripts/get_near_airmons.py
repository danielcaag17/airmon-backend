from api.scripts.django_setup import setup_django

setup_django()

import geohash
import datetime

from django.db.models import Q

from api.models.spawned_airmon import SpawnedAirmon


latitude = 41.387296
longitude = 2.159478
# TODO: refactor
geohash_ = geohash.encode(latitude=latitude, longitude=longitude, precision=6)
neighbors = geohash.neighbors(geohash_)
current_hour = datetime.datetime.now().hour
prev_hour = current_hour - 1 if current_hour > 0 else 23
minute = datetime.datetime.now().minute
geohash_queries = Q()
for hash in neighbors:
    geohash_queries |= Q(spawn_point__location__geohash__startswith=hash)
spawned_airmons = SpawnedAirmon.objects.filter(geohash_queries, hour__in=[current_hour, prev_hour])
processed_airmons = []
for airmon in spawned_airmons:
    if airmon.spawn_point.minute > minute and airmon.hour == prev_hour or airmon.spawn_point.minute <= minute and airmon.hour == current_hour:
        continue
    latitude, longitude = geohash.decode(airmon.spawn_point.location.geohash)
    processed_airmons.append({'name': airmon.airmon.name, 'capture_id': airmon.id,'location': {'latitude': latitude, 'longitude': longitude}})
print({'airmons': processed_airmons})
