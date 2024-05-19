from rest_framework import serializers

from ..models import Capture


class CaptureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capture
        fields = ['id', 'airmon', 'date', 'attempts']
        read_only_fields = ['id']
