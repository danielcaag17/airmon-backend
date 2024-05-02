from rest_framework import serializers
from ..models import Airmon, RarityType, AirmonType


class AirmonSerializer(serializers.ModelSerializer):
    rarity = serializers.ChoiceField(choices=[(tag.value, tag.value) for tag in RarityType])
    type = serializers.ChoiceField(choices=[(tag.value, tag.value) for tag in AirmonType])

    class Meta:
        model = Airmon
        fields = ['name', 'description', 'rarity', 'type', 'image']
