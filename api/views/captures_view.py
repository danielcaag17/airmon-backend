from django.http import HttpResponseBadRequest
from rest_framework import viewsets
from ..models import Capture, CaptureSpawnedAirmon, SpawnedAirmon, Player
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

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            return HttpResponseBadRequest(e)

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        spawned_airmon = SpawnedAirmon.objects.get(id=self.request.data['spawned_airmon_id'])
        if CaptureSpawnedAirmon.objects.filter(player__user=self.request.user, spawned_airmon=spawned_airmon).exists():
            raise Exception('You already captured this airmon')
        serializer.validated_data['airmon'] = spawned_airmon.airmon
        serializer.save()
        CaptureSpawnedAirmon.objects.create(
            player=Player.objects.get(user=self.request.user),
            spawned_airmon=SpawnedAirmon.objects.get(id=self.request.data['spawned_airmon_id'])
        )


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class PlayerCaptureViewSet(viewsets.ModelViewSet):
    """
    Endpoint: /api/player/:username/captures
    """
    serializer_class = CaptureSerializer

    def get_queryset(self):
        return Capture.objects.filter(user=self.request.user)
