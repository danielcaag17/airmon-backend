from django.contrib.auth.models import User
from rest_framework import viewsets
from ..models import Player
from rest_framework.response import Response
from rest_framework import status

from ..serializers import PlayerSerializer, PlayerPublicSerializer


from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class PlayerViewSet(viewsets.ViewSet):
    def list(self, request):
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)

    def retrieve(self, request, username=None):
        try:
            username = request.user.username
            user = User.objects.get(username=username)
            player = Player.objects.get(user=user.id)
            if username == user.username:   # Privat
                serializer = PlayerSerializer(player)
            else:   # Public
                serializer = PlayerPublicSerializer(player)
            return Response(serializer.data)
        except Player.DoesNotExist:
            return Response({"error": f"Player {username} does not exist"},
                            status=status.HTTP_400_BAD_REQUEST)
