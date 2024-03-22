from django.http import JsonResponse
from ..models import AirmonOnMap
from rest_framework.views import APIView


class AirmonOnMapView(APIView):
    """
    Endpoint: /api/airmons/
    """
    def get(self, request):
        # Example response data
        queryset = AirmonOnMap.objects.all().values()
        return JsonResponse({'airmon-map': list(queryset)})
