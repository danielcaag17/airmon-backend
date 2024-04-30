from rest_framework import serializers

from ..models import PollutantMeasure


class PollutantMeasureSerializer(serializers.ModelSerializer):
    pollutant_name = serializers.SerializerMethodField()
    measure_unit = serializers.SerializerMethodField()

    class Meta:
        model = PollutantMeasure
        fields = ['pollutant_name', 'measure_unit', 'quantity']

    def get_pollutant_name(self, obj):
        return obj.pollutant_name.name

    def get_measure_unit(self, obj):
        return obj.pollutant_name.measure_unit

