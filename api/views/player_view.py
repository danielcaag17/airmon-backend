from django.contrib.auth.models import User
from rest_framework import viewsets, status
from ..models import Player
from rest_framework.response import Response
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.core.exceptions import FieldError

from ..serializers import PlayerSerializer, PlayerPublicSerializer, PlayerStatisticsSerializer

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class PlayerViewSet(viewsets.ViewSet):
    def list(self, request):
        # TODO: canviar la info a publica
        players = Player.objects.all()
        serializer = PlayerPublicSerializer(players, many=True)
        return Response(serializer.data)

    def retrieve(self, request, username=None):
        # TODO: fer-ho be el public i el privat, vigilar amb quin username es fa el if
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

    def update(self, request):
        try:
            player = Player.objects.get(user__username=request.user.username)
            if request.data['coins'] != "":
                player.coins += int(request.data['coins'])
            player.save()
            return Response(status=status.HTTP_200_OK)
        except Player.DoesNotExist:
            return Response({"error": f"Player {request.user.username} does not exist"},
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


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class PlayerStatisticsViewSet(viewsets.ViewSet):
    def list(self, request, username=None):
        player = Player.objects.get(user__username=username)
        serializer = PlayerStatisticsSerializer(player)
        return Response(serializer.data)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class RankingViewSet(viewsets.ViewSet):
    def list(self, request, statistic=None):
        if statistic is None:
            return Response({"error": "Statistic field is required"}, status=400)

        try:
            # Ordenar per ordre descendent
            players = Player.objects.all().order_by(f'-{statistic}')
        except FieldError:
            return Response({"error": "Invalid statistic field"}, status=400)

        serializer = PlayerPublicSerializer(players, many=True)
        for player in serializer.data:
            player_instance = Player.objects.get(user__username=player['username'])
            player['statistic'] = getattr(player_instance, statistic, None)
            player.pop('avatar', None)
        return Response(serializer.data)
