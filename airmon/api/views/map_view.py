from django.core import serializers
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import viewsets
from ..serializers import MapSerializer
from ..models import Station


class MapViewSet(viewsets.ModelViewSet):
    """
    Endpoint: /api/map/
    """

    # Una estacio en concret identificada per code
    def get(self, request, code):
        station = Station.objects.all(pk=code)
        serializer_class = MapSerializer(station, many=True)
        return Response(serializer_class.data)
