import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'airmon.settings')
django.setup()

from api.models.station import Station
from api.models.measure import Measure

# Get all possible airmons
stations = Station.objects.all()

# Print all information about each airmon
for station in stations:
    measures = Measure.objects.filter(station_code=station)
    for measure in measures:
        print(f'Station {station.code} - {measure.icqa} ')

print(len(stations))
