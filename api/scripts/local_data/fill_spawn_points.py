from .geohash_data import (get_barcelona_geohashes, get_geohash_characters, get_catalonia_geohashes_lvl_4,
                           get_catalonia_geohashes_lvl_5)

barcelona_geohashes = get_barcelona_geohashes()
geohash_characters = get_geohash_characters()
catalonia_geohashes_lvl_4 = get_catalonia_geohashes_lvl_4()
catalonia_geohashes_lvl_5 = get_catalonia_geohashes_lvl_5()


def populate_barcelona_spawn_points():
    import random

    from api.models.location import LocationGeohash
    from api.models.spawn_point import SpawnPoint
    from api.utils.icqa_by_area import get_nearest_station_v2

    locations = []
    spawn_points = []
    for base_geohash in barcelona_geohashes:
        for c1 in geohash_characters:
            for c2 in geohash_characters:
                final_geohash = f"{base_geohash}{c1}{c2}"
                location = LocationGeohash(geohash=final_geohash)
                locations.append(location)
                station = get_nearest_station_v2(location)
                minute = random.randint(0, 59)
                spawn_points.append(
                    SpawnPoint(location=location, station=station, minute=minute)
                )
    LocationGeohash.objects.bulk_create(locations, ignore_conflicts=True)
    SpawnPoint.objects.bulk_create(spawn_points, ignore_conflicts=True)


def populate_catalonia_spawn_points():
    import random

    from api.models.station import Station
    from api.models.location import LocationGeohash
    from api.models.spawn_point import SpawnPoint
    from api.utils.icqa_by_area import get_nearest_station

    locations = []
    spawn_points = []
    stations = Station.objects.all()
    for base_geohash in catalonia_geohashes_lvl_4:
        for c1 in geohash_characters:
            for c2 in geohash_characters:
                for c3 in geohash_characters:
                    final_geohash = f"{base_geohash}{c1}{c2}{c3}"
                    location = LocationGeohash(geohash=final_geohash)
                    locations.append(location)
                    station = get_nearest_station(location, stations)
                    minute = random.randint(0, 59)
                    spawn_points.append(
                        SpawnPoint(location=location, station=station, minute=minute)
                    )
    for base_geohash in catalonia_geohashes_lvl_5:
        for c1 in geohash_characters:
            for c2 in geohash_characters:
                final_geohash = f"{base_geohash}{c1}{c2}"
                location = LocationGeohash(geohash=final_geohash)
                locations.append(location)
                station = get_nearest_station(location, stations)
                minute = random.randint(0, 59)
                spawn_points.append(
                    SpawnPoint(location=location, station=station, minute=minute)
                )
    LocationGeohash.objects.bulk_create(locations, ignore_conflicts=True)
    SpawnPoint.objects.bulk_create(spawn_points, ignore_conflicts=True)


if __name__ == "__main__":
    from api.scripts.django_setup import setup_django

    setup_django()

    populate_barcelona_spawn_points()
