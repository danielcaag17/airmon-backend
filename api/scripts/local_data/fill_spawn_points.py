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
catalonia_geohashes_lvl_4 = [
    "sp2x",
    "sp2z",
    "sp2q",
    "sp2w",
    "sp2y",
    "sp2m",
    "sp2t",
    "sp2v",
    "sp2k",
    "sp2s",
    "sp2u",
    "sp27",
    "sp2e",
    "sp2g",
    "sp26",
    "sp2d",
    "sp2f",
    "sp23",
    "sp29",
    "sp21",
    "sp20",
    "sp22",
    "sp28",
    "sp2c",
    "sp8b",
    "sp88",
    "sp8d",
    "sp8e",
    "sp8f",
    "sp89",
    "sp8c",
    "sp91",
    "sp90",
    "sp93",
    "sp91",
    "sp99",
    "sp98",
    "sp9b",
    "spd1",
    "spd0",
    "sp6p",
    "sp6n",
    "sp3p",
    "sp3r",
    "sp3x",
    "sp3z",
    "sp3n",
    "sp3q",
    "sp3w",
    "sp3y",
    "sp3j",
    "sp3m",
    "sp3t",
    "sp3v",
    "sp3h",
    "sp3k",
    "sp3s",
    "sp35",
    "sp37",
]
catalonia_geohashes_lvl_5 = [
    "sp6jb",
    "sp6jc",
    "sp6jf",
    "sp6jg",
    "sp6ju",
    "sp6jv",
    "sp6j8",
    "sp6j9",
    "sp6jd",
    "sp6je",
    "sp6j3",
    "sp6j2",
    "sp6j6",
    "sp6qb",
    "sp6q8",
    "sp6q2",
    "sp6r0",
    "sp6r2",
    "spd2b",
    "spd2c",
    "spd2f",
    "spd28",
    "spd29",
    "spd2d",
    "spd22",
    "spd23",
    "spd26",
    "sp3ub",
    "sp3uc",
    "sp3uf",
    "sp3ug",
    "sp3uu",
    "sp3uv",
    "sp3u8",
    "sp3u9",
    "sp3ud",
    "sp3eb",
    "sp3ec",
    "sp3ef",
    "sp3eg",
    "sp3e8",
    "sp3e9",
    "sp3ed",
    "sp3e2",
    "sp3e3",
    "sp3e0",
    "sp36b",
    "sp36c",
    "sp36f",
    "sp36g",
    "sp36u",
    "sp36v",
    "sp36y",
    "sp36z",
    "sp368",
    "sp369",
    "sp36u",
    "sp34b",
    "sp34c",
    "sp34f",
    "sp34g",
    "sp34u",
    "sp34v",
    "sp34y",
    "sp34z",
    "sp348",
    "sp349",
    "sp34d",
    "sp34e",
    "sp34s",
    "sp34t",
    "sp34w",
    "sp34x",
    "sp342",
    "sp343",
    "sp346",
    "sp347",
    "sp34k",
    "sp34m",
    "sp34q",
    "sp340",
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


def populate_barcelona_spawn_points():
    import random

    from api.models.station import Station
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
