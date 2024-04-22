from rest_framework import viewsets
from rest_framework.response import Response

from ..serializers import StationSerializer, MeasureSerializer
from ..models import Measure
from ..models import PollutantMeasure
from ..models import Station
from django.http import JsonResponse

from rest_framework import status

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
class StationViewSet(viewsets.ViewSet):
    """
    Endpoint: /api/station/:code
    """
    def retrieve(self, request, code=None):
        try:
            station = Station.objects.get(code=code)
            serializer = StationSerializer(station)
            return Response(serializer.data)
        except Station.DoesNotExist:
            return Response({"error": f"Estation {code} does not exist"},
                            status=status.HTTP_404_NOT_FOUND)
