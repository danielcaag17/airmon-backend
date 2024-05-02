import json
from typing import Dict, List

from rest_framework.views import APIView
from rest_framework.response import Response

from ..models import LocationGeohash
from ..models import Station

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from polygon_geohasher.polygon_geohasher import polygon_to_geohashes
from shapely import geometry
from django.db.models import Q
from functools import reduce
from operator import or_


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


# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
class ICQAView(APIView):
    """
    Endpoint: /api/icqa/
    Body example:
    {
        "points": [
            {"latitude": 41.408433, "longitude": 2.167609},
            {"latitude": 41.408497, "longitude": 2.181246},
            {"latitude": 41.397649, "longitude": 2.173533}
        ]
    }
    """

    def post(self, request, format=None):
        data = request.data
        coords_list = [
            [point["latitude"], point["longitude"]] for point in data["points"]
        ]
        locations_by_geohash: List[str] = []
        for point in data["points"]:
            locations_by_geohash.append(
                LocationGeohash.objects.coords_to_geohash(
                    latitude=point["latitude"], longitude=point["longitude"]
                )
            )
        common_geohash = longestCommonPrefix(locations_by_geohash)
        inverted_coords_list = [[p["longitude"], p["latitude"]] for p in coords_list]
        bbox = geometry.Polygon(inverted_coords_list)
        outer_covered_geohashes = polygon_to_geohashes(
            bbox, len(common_geohash) + 1, False
        )
        query = reduce(
            or_,
            (Q(location__geohash__startswith=item) for item in outer_covered_geohashes),
        )
        stations = Station.objects.filter(query)
        if not stations:
            return Response(
                data={
                    "code": "ICQA-02",
                    "message": "There are no stations in this area",
                }
            )
        for station in stations:
            # Get the worse air quality?
            pass
        icqa_valoration = "Bona"
        return Response(
            data={
                "code": "ICQA-01",
                "message": "The icqa was found for the specified area",
                "icqa": icqa_valoration,
            }
        )
