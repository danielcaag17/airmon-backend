from rest_framework import serializers

from ..models import PollutantMeasure


class PollutantMeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollutantMeasure
        fields = ['pollutant_name_id', 'measure_id', 'quantity']
