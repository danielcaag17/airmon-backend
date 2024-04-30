from datetime import time

from rest_framework import serializers
from .pollutant_measure_serializer import PollutantMeasureSerializer
from ..models import Measure, PollutantMeasure


class MeasureSerializer(serializers.ModelSerializer):
    pollutants = serializers.SerializerMethodField()
    hour = serializers.SerializerMethodField()

    class Meta:
        model = Measure
        fields = ['date', 'hour', 'val_color', 'nom_pollutant', 'pollutants']

    def get_hour(self, obj):
        if obj.hour is None:
            return time(hour=0, minute=0, second=0).strftime('%H:%M:%S')
        else:
            return obj.hour.strftime('%H:%M:%S')

    def get_pollutants(self, obj):
        pollutants = PollutantMeasure.objects.filter(measure_id=obj.id)
        serializer = PollutantMeasureSerializer(pollutants, many=True)
        return serializer.data
