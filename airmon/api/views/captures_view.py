from django.core import serializers
from django.http import JsonResponse
from rest_framework import viewsets
from ..models import Capture
from ..serializers import CaptureSerializer


class CaptureViewSet(viewsets.ModelViewSet):
    """
    Endpoint: /api/capture/
    """
    queryset = Capture.objects.all()
    serializer_class = CaptureSerializer


class PlayerCaptureViewSet(viewsets.ModelViewSet):
    """
    Endpoint: /api/capture/player/:username/captures
    """
    serializer_class = CaptureSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        return Capture.objects.filter(airmon__capture__username=username)

