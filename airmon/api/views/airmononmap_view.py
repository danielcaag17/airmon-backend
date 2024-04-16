from django.http import JsonResponse
from ..models import AirmonOnMap
from rest_framework.views import APIView

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class AirmonOnMapView(APIView):
    """
    Endpoint: /api/airmons/
    """
    def get(self, request):
        # Example response data
        queryset = AirmonOnMap.objects.all().values()
        return JsonResponse({'airmon-map': list(queryset)})
