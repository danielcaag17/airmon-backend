from rest_framework import serializers
from ..models import Airmon


class AirmonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airmon
        fields = ['id', 'name', 'description', 'rarity', 'type', 'image']

