from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from ..models import Trophy
from ..serializers import TrophySerializer

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class TrophyViewSet(viewsets.ViewSet):
    def retrieve(self, request, name=None):
        try:
            trophies = Trophy.objects.filter(name=name)
            serializer = TrophySerializer(trophies, many=True)
            return Response(serializer.data)
        except Trophy.DoesNotExist:
            return Response({"error": f"Trophy {name} does not exist"},
                            status=status.HTTP_400_BAD_REQUEST)
