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

