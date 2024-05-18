from rest_framework import serializers

from ..models import Item, PlayerItem


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'price', 'description', 'image', 'duration']


class PlayerItemSerializer(serializers.ModelSerializer):
    model = PlayerItem

    class Meta:
        fields = ['item_name', 'quantity']


class PlayerActiveItemSerializer(serializers.ModelSerializer):
    model = PlayerItem

    class Meta:
        fields = ['item_name', 'expiration']
