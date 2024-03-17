from rest_framework import serializers

from ..models import Measure


class MeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measure
        fields = ['station_code', 'date', 'hour']
