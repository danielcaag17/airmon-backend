from rest_framework import viewsets
from rest_framework.response import Response

from ..models import Player, PlayerTrophy, Trophy
from ..serializers import TrophySerializer
from ..signals import get_relation

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class PlayerTrophyViewSet(viewsets.ViewSet):
    def list(self, request, username=None):
        all_trophies = Trophy.objects.all()
        serializer = TrophySerializer(all_trophies, many=True)
        for trophy in serializer.data:
            # Cas per defecte, user no te el trofeu
            trophy["data"] = None
            if PlayerTrophy.objects.filter(trophy_id=trophy["id"], user__username=username).exists():
                player_trophy = PlayerTrophy.objects.filter(trophy_id=trophy["id"], user__username=username).first()
                trophy["data"] = player_trophy.date

        return Response(serializer.data)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class PlayerTrophyInfoViewSet(viewsets.ViewSet):
    def retrieve(self, request, name=None):
        if name is None:
            return Response({"error": "Statistic field is required"}, status=400)

        n_trofeus = PlayerTrophy.objects.filter(user__username=request.user, trophy__name=name).count()
        player = Player.objects.get(user=request.user)
        player_field = get_relation()
        field_value = getattr(player, player_field[name])
        if n_trofeus == 0:  # Retornar Bronze
            trophy = Trophy.objects.filter(name=name, type="BRONZE").first()
        elif n_trofeus == 1:  # Retornar Plata
            trophy = Trophy.objects.filter(name=name, type="PLATA").first()
        elif n_trofeus == 2 or n_trofeus == 3:  # Retornar Or
            trophy = Trophy.objects.filter(name=name, type="OR").first()
        else:
            trophy = None
        serializer = TrophySerializer(trophy)
        serializer_data = serializer.data
        serializer_data['progress'] = field_value

        return Response(serializer_data)
