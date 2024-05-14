from rest_framework import viewsets
from ..models import Capture
from ..serializers import CaptureSerializer

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class CaptureViewSet(viewsets.ModelViewSet):
    """
    Endpoint: /api/capture/
    """
    queryset = Capture.objects.all()
    serializer_class = CaptureSerializer


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class PlayerCaptureViewSet(viewsets.ModelViewSet):
    """
    Endpoint: /api/player/:username/captures
    """
    serializer_class = CaptureSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        return Capture.objects.filter(airmon__capture__username=username)
