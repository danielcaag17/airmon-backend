from rest_framework import serializers

from ..models import Pollutant


class PollutantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pollutant
        fields = ['name', 'measure_unit', 'recommended_limit']
