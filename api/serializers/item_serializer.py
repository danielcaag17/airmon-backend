from rest_framework import serializers

from ..models import Item, PlayerItem, PlayerActiveItem


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'price', 'description', 'image', 'duration']


class PlayerItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerItem
        fields = ['item_name', 'quantity']


class PlayerActiveItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlayerActiveItem
        fields = ['item_name', 'expiration']
        read_only_fields = ['expiration']
