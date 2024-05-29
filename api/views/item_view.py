from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.response import Response

from ..models import Item, PlayerItem, Player
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

    def create(self, request, *args, **kwargs):
        item_name = request.data.get('item_name')
        quantity = int(request.data.get('quantity'))
        free = request.query_params.get('free', False)

        item = get_object_or_404(Item, pk=item_name)
        player = get_object_or_404(Player, user=request.user)

        if player.coins < item.price * quantity:
            return Response({"error": "You don't have enough coins"}, status=status.HTTP_400_BAD_REQUEST)

        if not free:
            player.coins -= item.price * quantity
            player.save()

        # Get the serializer
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            player_item = PlayerItem.objects.get(user=request.user, item_name=item_name)
            player_item.quantity += quantity
            player_item.save()
            serializer.validated_data['quantity'] = player_item.quantity
        except PlayerItem.DoesNotExist:
            serializer.save(user=request.user)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class PlayerActiveItemViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerActiveItemSerializer

    def get_queryset(self):
        return item_util.get_active_items(self.request.user)

    def create(self, request, *args, **kwargs):
        item_name = request.data.get('item_name')

        try:
            player_item = PlayerItem.objects.get(user=request.user, item_name=item_name)
        except PlayerItem.DoesNotExist:
            return Response({"error": "You don't have this item"}, status=status.HTTP_400_BAD_REQUEST)

        if player_item.quantity <= 0:
            return Response({"error": "You don't have any more items left"}, status=status.HTTP_400_BAD_REQUEST)

        player_item.quantity -= 1

        if player_item.quantity == 0:
            player_item.delete()
        else:
            player_item.save()

        # Get the serializer
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # The code from perform_create() starts here
        item = get_object_or_404(Item, pk=item_name)
        duration = timezone.timedelta(hours=item.duration.hour, minutes=item.duration.minute,
                                      seconds=item.duration.second)

        active_items = item_util.get_active_items(self.request.user)

        searched = active_items.filter(item_name=item_name)
        if searched.exists():
            active_item = searched.first()
            active_item.expiration += duration
            active_item.save()
            serializer.validated_data['expiration'] = active_item.expiration
        else:
            instant = timezone.now()
            if instant != instant + duration:
                # Means the duration is not 0, so we save the item with an expiration date
                expiration = timezone.now() + duration
                serializer.save(user=self.request.user, expiration=expiration)

        result = item_util.handle_specific_action(self.request.user, item_name)

        headers = self.get_success_headers(serializer.data)

        if result is not None:
            data = {**serializer.data, **result}
        else:
            data = serializer.data

        return Response(data, status=status.HTTP_201_CREATED, headers=headers)
