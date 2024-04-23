from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from ..models import Player
from ..serializers.player_serializer import PlayerSerializer


class Endpoint1View(ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
