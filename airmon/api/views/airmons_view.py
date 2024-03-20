from rest_framework import viewsets
from ..models import Airmon
from ..serializers import AirmonSerializer


class AirmonsViewSet(viewsets.ModelViewSet):
    """
    Endpoint: /api/airmons/
    """
    queryset = Airmon.objects.all()
    serializer_class = AirmonSerializer
