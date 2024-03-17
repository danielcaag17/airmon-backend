from rest_framework import serializers

from .station_serializer import StationSerializer
from .pollutant_serializer import PollutantSerializer
from .pollutant_measure_serializer import PollutantMeasureSerializer
from .measure_serializer import MeasureSerializer


class MapSerializer(serializers.Serializer):
    class Meta:
        model_station = StationSerializer(many=True)
        model_pollutant = PollutantSerializer(many=True)
        model_pollutant_measure = PollutantMeasureSerializer(many=True)
        model_measure = MeasureSerializer(many=True)
