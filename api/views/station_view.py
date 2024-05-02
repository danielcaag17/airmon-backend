import json

from rest_framework import viewsets
from rest_framework.response import Response

from ..serializers import StationSerializer
from ..models import Station

from rest_framework import status

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class StationViewSet(viewsets.ViewSet):
    """
    Endpoint: /api/station/:code
    """
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
