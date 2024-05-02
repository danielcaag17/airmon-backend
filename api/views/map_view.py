from rest_framework.response import Response
from rest_framework import viewsets
from ..models import Station, Measure, PollutantMeasure
import json

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from ..serializers import StationSerializer


# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
class MapViewSet(viewsets.ViewSet):
    """
    Endpoint: /api/map/
    """
    def list(self, request):
        stations = Station.objects.filter(measure__isnull=False)
        serializer = StationSerializer(stations, many=True)
        format_correcte = json.loads(json.dumps(serializer.data))
        return Response(format_correcte)
