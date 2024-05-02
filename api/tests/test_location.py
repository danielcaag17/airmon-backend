from django.test import TestCase
from rest_framework.test import APIClient
from decimal import Decimal

from ..models import LocationGeohash, Location


class LocationModelTest(TestCase):
    def setUp(self):
        # self.client = APIClient()
        LocationGeohash.objects.create(
            geohash='1'
        )
        Location.objects.create(
            id=1,
            longitude=123.123,
            latitude=123.123
        )

    def test_geohash_creation(self):
        geohash = LocationGeohash.objects.get(geohash='1')
        self.assertEqual(geohash.geohash, '1')

    def test_location_creation(self):
        location = Location.objects.get(id=1)
        self.assertEqual(location.longitude, Decimal('123.123'))
        self.assertEqual(location.latitude, Decimal('123.123'))
