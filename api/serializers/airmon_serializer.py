from rest_framework import serializers
from ..models import Airmon, RarityType, AirmonType


class AirmonSerializer(serializers.ModelSerializer):
    rarity = serializers.ChoiceField(choices=RarityType.choices)
    type = serializers.ChoiceField(choices=AirmonType.choices)

    class Meta:
        model = Airmon
        fields = ['name', 'description', 'rarity', 'type', 'image']
