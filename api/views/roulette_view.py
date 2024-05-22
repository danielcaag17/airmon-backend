from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.response import Response

from ..models import Player


class RouletteView(viewsets.ViewSet):

    def create(self, request, *args, **kwargs):
        player = get_object_or_404(Player, user=request.user)

        date = timezone.now().date()
        player.last_roulette_spin = date

        return Response({'last_spin': date}, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        player = get_object_or_404(Player, user=request.user)

        return Response({'last_spin': player.last_roulette_spin}, status=status.HTTP_200_OK)
