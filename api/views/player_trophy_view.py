from rest_framework import viewsets
from rest_framework.response import Response

from ..models import PlayerTrophy, Trophy
from ..serializers import TrophySerializer


class PlayerTrophyViewSet(viewsets.ViewSet):
    def list(self, request, username=None):
        all_trophies = Trophy.objects.all()
        serializer = TrophySerializer(all_trophies, many=True)
        for trophy in serializer.data:
            # Cas per defecte, user no te el trofeu
            trophy["data"] = None
            trophies_obtained = PlayerTrophy.objects.filter(trophy=trophy["id"])
            for trophy_obtained in trophies_obtained:
                if trophy_obtained.username.username == username:
                    # Si user te el trofeu, es posa la data
                    trophy["data"] = trophy_obtained.date

        return Response(serializer.data)
