from api.scripts.django_setup import setup_django

setup_django()

from functools import reduce
from operator import or_
from api.models.station import Station
from polygon_geohasher.polygon_geohasher import (
    polygon_to_geohashes,
    geohashes_to_polygon,
)
from shapely import geometry
from django.db.models import Q
import geohash


def longestCommonPrefix(my_str):
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


coords_list = [[41.408433, 2.167609], [41.408497, 2.181246], [41.397649, 2.173533]]
locations_by_geohash = []
for point in coords_list:
    locations_by_geohash.append(geohash.encode(latitude=point[0], longitude=point[1]))
common_geohash = longestCommonPrefix(locations_by_geohash)
inverted_coords_list = [[p[1], p[0]] for p in coords_list]
bbox = geometry.Polygon(inverted_coords_list)
outer_covered_geohashes = polygon_to_geohashes(bbox, len(common_geohash) + 1, False)
query = reduce(
    or_, (Q(location__geohash__startswith=item) for item in outer_covered_geohashes)
)
stations = Station.objects.filter(query)
