from rest_framework.response import Response
from rest_framework import viewsets
from ..serializers import PollutantSerializer, PollutantMeasureSerializer, StationSerializer, MeasureSerializer
from ..models import Measure
from ..models import PollutantMeasure
from ..models import Pollutant
from ..models import Station
from django.core import serializers


class MapViewSet(viewsets.ViewSet):
    """
    Endpoint: /api/map/
    """
    def list(self, request):
        '''
        combined_data = {
            # 'measure': serializers.serialize('json', Measure.objects.all()),
            'pollutant_measure': serializers.serialize('json', PollutantMeasure.objects.filter(id=1)),
            'pollutant': serializers.serialize('json', Pollutant.objects.filter(name="CO2")),
            'station': serializers.serialize('json', Station.objects.filter(code=1)),
        }
        # serializer_class = MapSerializer(combined_data)
        # return Response(serializer_class.data)
        '''

    def list(self, request):
        # measure = Measure.objects.filter(id=1)
        pollutant_measure = PollutantMeasure.objects.all()
        pollutant = Pollutant.objects.all()
        station = Station.objects.all()

        # measure_serializer = MeasureSerializer(measure)
        pollutant_measure_serializer = PollutantMeasureSerializer(pollutant_measure)
        pollutant_serializer = PollutantSerializer(pollutant)
        station_serializer = StationSerializer(station)

        combined_data = {
            # 'measure': measure_serializer.data,
            'pollutant_measure': pollutant_measure_serializer.data,
            'pollutant': pollutant_serializer.data,
            'station': station_serializer.data,
        }
        return Response(combined_data)

