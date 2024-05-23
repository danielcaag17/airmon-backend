from django.contrib.auth.models import User
from rest_framework import viewsets, status
from ..models import Player
from rest_framework.response import Response
from django.utils import timezone
from django.shortcuts import get_object_or_404


from ..serializers import PlayerSerializer, PlayerPublicSerializer

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class PlayerViewSet(viewsets.ViewSet):
    def list(self, request):
        players = Player.objects.all()
        serializer = PlayerPublicSerializer(players, many=True)
        return Response(serializer.data)

    def retrieve(self, request, username=None):
        try:
            auth_user = request.user
            user = User.objects.get(username=username)
            player = Player.objects.get(user=user.id)
            if auth_user.id == user.id:   # Privat
                serializer = PlayerSerializer(player)
            else:   # Public
                serializer = PlayerPublicSerializer(player)
            return Response(serializer.data)
        except Player.DoesNotExist:
            return Response({"error": f"Player {username} does not exist"},
                            status=status.HTTP_400_BAD_REQUEST)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class RouletteView(viewsets.ViewSet):

    def create(self, request, *args, **kwargs):
        player = get_object_or_404(Player, user=request.user)

        date = timezone.now().date()
        player.last_roulette_spin = date
        player.save()

        return Response({'last_spin': date}, status=status.HTTP_200_OK)

    def retrieve(self, request):
        player = get_object_or_404(Player, user=request.user)

        return Response({'last_spin': player.last_roulette_spin}, status=status.HTTP_200_OK)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class ExpView(viewsets.ViewSet):

    def retrieve(self, request):
        player = get_object_or_404(Player, user=request.user)

        return Response({'exp': player.xp_points}, status=status.HTTP_200_OK)

    def partial_update(self, request):
        player = get_object_or_404(Player, user=request.user)
        exp = int(request.data['exp'])
        player.xp_points += exp
        player.save()
        return Response({'exp': player.xp_points}, status=status.HTTP_200_OK)
