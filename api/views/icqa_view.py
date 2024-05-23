from rest_framework.views import APIView
from rest_framework.response import Response

from api.models.measure import Measure
from api.models.location import LocationGeohash
from api.utils.icqa_by_area import ICQA_VALORATION, get_stations_in_area


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
        locations_by_geohash = []
        for point in data["points"]:
            locations_by_geohash.append(
                LocationGeohash.objects.coords_to_geohash(
                    latitude=point["latitude"], longitude=point["longitude"]
                )
            )
        stations = get_stations_in_area(locations_by_geohash, coords_list)
        worse_icqa = 1
        for station in stations:
            measure = Measure.objects.get(station_code=station.code)
            if measure is None:
                continue
            worse_icqa = max(worse_icqa, measure.icqa)
        return Response(
            data={
                "code": "ICQA-01",
                "message": "The icqa was found for the specified area",
                "icqa": ICQA_VALORATION[worse_icqa],
            }
        )
