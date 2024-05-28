from rest_framework import serializers

from ..models import Event, LocationGeohash


class EventSerializer(serializers.ModelSerializer):
    longitude = serializers.SerializerMethodField()
    latitude = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ['codi', 'data_ini', 'data_fi', 'longitude', 'latitude', 'espai']

    def get_longitude(self, obj):
        return LocationGeohash.objects.geohash_to_coords(obj.geohash.geohash)['longitude']

    def get_latitude(self, obj):
        return LocationGeohash.objects.geohash_to_coords(obj.geohash.geohash)['latitude']
