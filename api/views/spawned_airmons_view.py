import geohash
import datetime

from django.http import HttpResponseBadRequest, JsonResponse
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from api.models.capture_spawned_airmon import CaptureSpawnedAirmon
from api.models.spawned_airmon import SpawnedAirmon


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class SpawnedAirmonsView(APIView):
    """
    Endpoint: /api/spawned_airmons/
    """

    def get(self, request):
        latitude = float(request.query_params.get("latitude"))
        longitude = float(request.query_params.get("longitude"))
        if not latitude or not longitude:
            return HttpResponseBadRequest("Latitude and/or longitude missing.")
        geohash_ = geohash.encode(latitude=latitude, longitude=longitude, precision=6)
        neighbors = geohash.neighbors(geohash_)
        current_hour = datetime.datetime.now().hour
        prev_hour = current_hour - 1 if current_hour > 0 else 23
        minute = datetime.datetime.now().minute
        geohash_queries = Q()
        for hash in neighbors:
            geohash_queries |= Q(spawn_point__location__geohash__startswith=hash)
        spawned_airmons = SpawnedAirmon.objects.filter(
            geohash_queries, hour__in=[current_hour, prev_hour]
        )
        daily_captures = CaptureSpawnedAirmon.objects.filter(player__user=request.user)
        daily_captures_ids = [capture.spawned_airmon.id for capture in daily_captures]
        print(daily_captures_ids)
        processed_airmons = []
        for airmon in spawned_airmons:
            if airmon.id in daily_captures_ids or (
                airmon.spawn_point.minute > minute
                and airmon.hour == prev_hour
                or airmon.spawn_point.minute <= minute
                and airmon.hour == current_hour
            ):
                continue
            latitude, longitude = geohash.decode(airmon.spawn_point.location.geohash)
            processed_airmons.append(
                {
                    "name": airmon.airmon.name,
                    "spawned_airmon_id": airmon.id,
                    "location": {"latitude": latitude, "longitude": longitude},
                }
            )
        return JsonResponse({"airmons": processed_airmons})
