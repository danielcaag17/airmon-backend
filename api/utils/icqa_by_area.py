from typing import List
from shapely import geometry
from django.db.models import Q
from functools import reduce
from operator import or_
from polygon_geohasher.polygon_geohasher import polygon_to_geohashes

from api.models.station import Station

ICQA_VALORATION = {
    1: "Bona",
    2: "Raonablement bona",
    3: "Regular",
    4: "Desfavorable",
    5: "Molt desfavorable",
    6: "Extremadament desfavorable",
}


def longest_common_prefix(my_str):
    if my_str == []:
        return ""
    if len(my_str) == 1:
        return my_str[0]
    my_str.sort()
    shortest = my_str[0]
    prefix = ""
    for i in range(len(shortest)):
        if my_str[len(my_str) - 1][i] == shortest[i]:
            prefix += my_str[len(my_str) - 1][i]
        else:
            break
    return prefix


def get_stations_in_area(locations: List[str], coords_list):
    common_geohash = longest_common_prefix(locations)
    inverted_coords_list = [[p[1], p[0]] for p in coords_list]
    bbox = geometry.Polygon(inverted_coords_list)
    outer_covered_geohashes = polygon_to_geohashes(bbox, len(common_geohash) + 1, False)
    query = reduce(
        or_,
        (Q(location__geohash__startswith=item) for item in outer_covered_geohashes),
    )
    return Station.objects.filter(query)


def get_nearest_station(location: str):
    station = Station.objects.get(location__geohash="sp3e902j1c3z")  # Mocked station
    return station
