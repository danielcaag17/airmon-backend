# from django.utils import timezone
from rest_framework.response import Response
from rest_framework import viewsets
from ..models import Measure
from ..models import PollutantMeasure
from ..models import Pollutant
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

    def list(self, request):
        # self.afegir()
        measure = Measure.objects.all()
        pollutant_measure = PollutantMeasure.objects.all()
        pollutant = Pollutant.objects.all()
        station = Station.objects.all()

        measure_serializer = []
        # i = measure.first().station_code.code
        for obj in measure:
            obj_serialized = {
                'station_code': obj.station_code.code,
                'date': obj.date.strftime('%Y-%m-%d'),
                'hour': obj.date.strftime('%H:%M:%S'),
            }
            measure_serializer.append(obj_serialized)

        pollutant_measure_serializer = []
        for obj in pollutant_measure:
            obj_serialized = {
                'pollutant_name': obj.pollutant_name.name,
                # 'measure': obj.measure.station_code.code,
                'measure': obj.measure.id,
                'quantity': obj.quantity,
            }
            pollutant_measure_serializer.append(obj_serialized)

        pollutant_serializer = []
        for obj in pollutant:
            obj_serialized = {
                'name': obj.name,
                'measure_unit': obj.measure_unit,
                'recommended_limit': obj.recommended_limit,
            }
            pollutant_serializer.append(obj_serialized)

        station_serializer = []
        for obj in station:
            obj_serialized = {
                'code': obj.code,
                'name': obj.name,
                'longitude': obj.location.longitude,
                'latitude': obj.location.latitude
            }
            station_serializer.append(obj_serialized)

        combined_data = {
            'measure': measure_serializer,
            'pollutant_measure': pollutant_measure_serializer,
            'pollutant': pollutant_serializer,
            'station': station_serializer,
        }
        return Response(combined_data)

