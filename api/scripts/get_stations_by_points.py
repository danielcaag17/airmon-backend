from api.scripts.django_setup import setup_django

setup_django()

import geohash
from api.models.measure import Measure
from api.utils.icqa_by_area import ICQA_VALORATION, get_stations_in_area


coords_list = [[41.423828, 2.150207], [41.428185, 2.187357], [41.387296, 2.159478]]
locations_by_geohash = []
for point in coords_list:
    locations_by_geohash.append(geohash.encode(latitude=point[0], longitude=point[1]))
stations = get_stations_in_area(locations_by_geohash, coords_list)
worse_icqa = 1
for station in stations:
    measure = Measure.objects.get(station_code=station.code)
    if measure is None:
        continue
    worse_icqa = max(worse_icqa, measure.icqa)
print(
    {
        "code": "ICQA-01",
        "message": "The icqa was found for the specified area",
        "icqa": ICQA_VALORATION[worse_icqa],
    }
)
