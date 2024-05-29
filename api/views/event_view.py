from rest_framework import viewsets
from rest_framework.response import Response
from django.http import HttpResponse

from ..utils import event_api_util
from ..models import Event
from ..serializers import EventSerializer

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class EventViewSet(viewsets.ViewSet):
    def list(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def run_script_view(request):
    event_api_util.update_event_data()
    return HttpResponse("Script ejecutado correctamente")
