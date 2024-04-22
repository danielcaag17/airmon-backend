from rest_framework import serializers
from .pollutant_measure_serializer import PollutantMeasureSerializer
from ..models import Measure, PollutantMeasure


class MeasureSerializer(serializers.ModelSerializer):
    pollutants = serializers.SerializerMethodField()

    class Meta:
        model = Measure
        fields = ['date', 'hour', 'pollutants']

    def get_pollutants(self, obj):
        pollutants = PollutantMeasure.objects.filter(measure_id=obj.id)
        serializer = PollutantMeasureSerializer(pollutants, many=True)
        return serializer.data
