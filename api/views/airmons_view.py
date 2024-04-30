from rest_framework import viewsets
from ..models import Airmon
from ..serializers import AirmonSerializer

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class AirmonsViewSet(viewsets.ModelViewSet):
    """
    Endpoint: /api/airmons/
    """
    queryset = Airmon.objects.all()
    serializer_class = AirmonSerializer
