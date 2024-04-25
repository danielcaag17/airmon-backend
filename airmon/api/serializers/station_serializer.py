from rest_framework import serializers
from .measure_serializer import MeasureSerializer
from ..models import Station, Measure


class StationSerializer(serializers.ModelSerializer):
    longitude = serializers.SerializerMethodField()
    latitude = serializers.SerializerMethodField()
    measure = serializers.SerializerMethodField()
    code_station = serializers.SerializerMethodField()

    class Meta:
        model = Station
        fields = ['code_station', 'name', 'longitude', 'latitude', 'measure']

    def get_code_station(self, obj):
        return obj.code

    def get_longitude(self, obj):
        return float(obj.location.longitude)

    def get_latitude(self, obj):
        return float(obj.location.latitude)

    def get_measure(self, obj):
        measures = Measure.objects.filter(station_code=obj.code)
        serializer = MeasureSerializer(measures, many=True)
        if bool(serializer.data[0]):
            return serializer.data[0]
        else:
            return None
