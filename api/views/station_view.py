import json

from rest_framework import viewsets
from rest_framework.response import Response

from ..serializers import StationSerializer
from ..models import Station, Measure

from rest_framework import status

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class StationViewSet(viewsets.ViewSet):

    def get_icqa(self, code):
        measure = Measure.objects.get(station_code=code)
        return measure.icqa

    def list(self, request):
        stations = Station.objects.filter(measure__isnull=False)
        if stations.count() == 1:
            station_serializer = StationSerializer(stations.first())
            station_data = station_serializer.data
            station_data.pop('measure')
            station_data['icqa'] = self.get_icqa(station_data['code_station'])
            return Response(station_data)
        else:
            station_serializer = StationSerializer(stations, many=True)
            for station in station_serializer.data:
                station.pop('measure')
                station['icqa'] = self.get_icqa(station['code_station'])
            return Response(station_serializer.data)

    def retrieve(self, request, code=None):
        try:
            station = Station.objects.get(code=code)
            serializer = StationSerializer(station)
            correct_format = json.loads(json.dumps(serializer.data))
            return Response(correct_format)
        except Station.DoesNotExist:
            return Response({"error": f"Station {code} does not exist"},
                            status=status.HTTP_404_NOT_FOUND)
