from rest_framework.viewsets import ModelViewSet
from ..models import Player
from ..serializers.player_serializer import PlayerSerializer


class PlayerViewSet(ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
