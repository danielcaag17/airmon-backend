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
        measures = Measure.objects.get(station_code=code)
        icqa = 1
        for measure in measures:
            if measure.icqa > icqa:
                icqa = measure.icqa

        return icqa

    def list(self, request):
        stations = Station.objects.filter(measure__isnull=False)
        result = []
        for station in stations:
            station_obj_serialized = {
                'code': station.code,
                'name': station.name,
                'icqa': self.get_icqa(station.code)
            }
            result.append(station_obj_serialized)
        return Response(result)

    def retrieve(self, request, code=None):
        try:
            station = Station.objects.get(code=code)
            if station.measure is None:
                return Response({"error": f"Station {code} does not have any measure"},
                            status=status.HTTP_404_NOT_FOUND)
            serializer = StationSerializer(station)
            correct_format = json.loads(json.dumps(serializer.data))
            return Response(correct_format)
        except Station.DoesNotExist:
            return Response({"error": f"Station {code} does not exist"},
                            status=status.HTTP_404_NOT_FOUND)
