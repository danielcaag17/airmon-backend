# from django.utils import timezone
from rest_framework.response import Response
from rest_framework import viewsets
from ..models import Measure, PollutantMeasure, Station

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
        stations = Station.objects.all()
        serializer = StationSerializer(stations, many=True)
        return Response(serializer.data)

