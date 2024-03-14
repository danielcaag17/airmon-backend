from rest_framework import serializers

from ..models import Capture


class CaptureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capture
        fields = ['username', 'airmon_name', 'rarity', 'type', 'date', 'attempts']

