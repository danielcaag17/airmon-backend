from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes

from ..models import Item, PlayerItem, PlayerActiveItem
from ..serializers import ItemSerializer, PlayerItemSerializer


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class PlayerItemViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerItemSerializer

    def get_queryset(self):
        return PlayerItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class PlayerActiveItemViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerItemSerializer

    def get_queryset(self):
        return PlayerActiveItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        item = self.request.data.get('item')

        item = get_object_or_404(Item, pk=item)
        expiration = timezone.now() + item.duration

        serializer.save(user=self.request.user, expiration=expiration)
