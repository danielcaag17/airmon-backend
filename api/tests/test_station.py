from django.test import TestCase
from django.db.utils import IntegrityError

from .utils import *


class StationModelTest(TestCase):
    def setUp(self):
        self.station = create_station(code=1, name='Test Station', location=create_location_geohash("u09tunqp3d08"))

    def test_station_creation(self):
        self.assertEqual(self.station.code, 1)
        self.assertEqual(self.station.name, "Test Station")
        self.assertEqual(self.station.location.geohash, "u09tunqp3d08")

    def test_station_destroy(self):
        stations_before = Station.objects.count()  # Nombre de Stations que hi ha
        self.station.delete()
        stations_after = Station.objects.count()
        self.assertEqual(stations_after, stations_before - 1)

    def test_station_update(self):
        self.station.code = 2
        self.station.name = "Station updated"
        self.station.location = create_location_geohash("dr5ru9pq8")
        self.station.save()
        self.assertEqual(self.station.code, 2)
        self.assertEqual(self.station.name, "Station updated")
        self.assertEqual(self.station.location.geohash, "dr5ru9pq8")

    def test_station_invalid1(self):
        try:
            Station.objects.create(
                code=1,
            )
            self.fail("It should raise an exception, station invalid1")
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            self.assertIn("NOT NULL constraint failed: api_station.location_id", str(e))

    def test_station_invalid2(self):
        try:
            Station.objects.create(
                code=2,
                name="Invalid station",
                location=self.station.location
            )
            self.fail("It should raise an exception, station invalid2")
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            self.assertIn("UNIQUE constraint failed: api_station.location_id", str(e))
