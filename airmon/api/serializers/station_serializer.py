from rest_framework import serializers
from .measure_serializer import MeasureSerializer
from ..models import Station, Measure
from ..models import LocationGeohash


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
        print(obj)
        return LocationGeohash.objects.geohash_to_coords(obj.location.geohash)['longitude']

    def get_latitude(self, obj):
        return LocationGeohash.objects.geohash_to_coords(obj.location.geohash)['latitude']

    def get_measure(self, obj):
        measures = Measure.objects.filter(station_code=obj.code)
        serializer = MeasureSerializer(measures, many=True)
        if bool(serializer.data):
            return serializer.data[0]
        else:
            return None
