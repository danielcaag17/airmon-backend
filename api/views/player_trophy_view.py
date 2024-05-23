from rest_framework import viewsets
from rest_framework.response import Response

from ..models import PlayerTrophy, Trophy
from ..serializers import TrophySerializer

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
