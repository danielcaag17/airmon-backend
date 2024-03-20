# from django.utils import timezone
from rest_framework.response import Response
from rest_framework import viewsets
from ..models import Measure
from ..models import PollutantMeasure
from ..models import Station


class MapViewSet(viewsets.ViewSet):
    """
    Endpoint: /api/map/
    """

    '''
    def afegir(self):
        nueva_instancia = Measure(
            station_code=Station.objects.get(code=1),
            date=timezone.now().date(),
            hour=timezone.now().time()
        )
        nueva_instancia.save()
    '''

    def get_pollutants(self, measure_id):
        pollutant_measure = PollutantMeasure.objects.filter(measure_id=measure_id)
        pollutant_measure_serializer = []
        for objPM in pollutant_measure:
            pollutant_measure_obj_serialized = {
                'pollutant_name': objPM.pollutant_name.name,
                'measure_unit': objPM.pollutant_name.measure_unit,
                'quantity': objPM.quantity,
                'recommended_limit': objPM.pollutant_name.recommended_limit,
            }
            pollutant_measure_combined_data = {
                'pollutant': pollutant_measure_obj_serialized
            }
            pollutant_measure_serializer.append(pollutant_measure_combined_data)
        return pollutant_measure_serializer

    def get_measures(self, code):
        measure = Measure.objects.filter(station_code=code)
        measure_serializer = []
        for objM in measure:
            measure_obj_serialized = {
                'date': objM.date.strftime('%Y-%m-%d'),
                'hour': objM.date.strftime('%H:%M:%S'),
                'pollutants': self.get_pollutants(objM.id)
            }
            measure_data = {
                'measure': measure_obj_serialized
            }
            measure_serializer.append(measure_data)
        return measure_serializer

    def list(self, request):
        # self.afegir()
        result = []
        station_serializer = []
        station = Station.objects.all()
        stations_data = {}
        for objS in station:
            station_obj_serialized = {
                'code_station': objS.code,
                'name': objS.name,
                'longitude': objS.location.longitude,
                'latitude': objS.location.latitude,
                'measures': self.get_measures(objS.code),
            }
            station_serializer.append(station_obj_serialized)
            stations_data = {
                'station': station_serializer,
            }
        result.append(stations_data)
        return Response(result)

