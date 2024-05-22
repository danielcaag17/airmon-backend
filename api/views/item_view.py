from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.response import Response

from ..models import Item, PlayerItem
from ..serializers import ItemSerializer, PlayerItemSerializer, PlayerActiveItemSerializer
from ..utils import item_util


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
        item = self.request.data.get('item_name')
        try:
            item = PlayerItem.objects.get(user=self.request.user, item_name=item)
            quantity = self.request.data.get('quantity')
            item.quantity += int(quantity)
            item.save()
        except PlayerItem.DoesNotExist:
            serializer.save(user=self.request.user)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class PlayerActiveItemViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerActiveItemSerializer

    def get_queryset(self):
        return item_util.get_active_items(self.request.user.id)

    def create(self, request, *args, **kwargs):
        item_name = request.data.get('item_name')

        try:
            item = PlayerItem.objects.get(user=request.user, item_name=item_name)
        except PlayerItem.DoesNotExist:
            return Response({"error": "You don't have this item"}, status=status.HTTP_400_BAD_REQUEST)

        if item.quantity <= 0:
            return Response({"error": "You don't have any more items left"}, status=status.HTTP_400_BAD_REQUEST)

        item.quantity -= 1
        item.save()
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        item_name = self.request.data.get('item_name')

        item = get_object_or_404(Item, pk=item_name)
        duration = item.duration

        active_items = item_util.get_active_items(self.request.user.id)

        searched = active_items.filter(item_name=item_name)
        if searched.exists():
            active_item = searched.first()
            active_item.expiration += timezone.timedelta(hours=duration.hour, minutes=duration.minute,
                                                         seconds=duration.second)
            active_item.save()
            serializer.validated_data['expiration'] = active_item.expiration
            return

        expiration = timezone.now() + timezone.timedelta(hours=duration.hour, minutes=duration.minute,
                                                         seconds=duration.second)

        serializer.save(user=self.request.user, expiration=expiration)
