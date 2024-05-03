from django.db import IntegrityError
from django.test import TestCase
from datetime import datetime, timedelta

from ..models import PollutantMeasure
from .utils import *


class PollutantMeasureModelTest(TestCase):
    def setUp(self):
        self.station = create_station(1, "station1", create_location_geohash("u09tunqp3d08"))
        measure = create_measure(self.station, datetime.now().date(), datetime.now().time())
        self.pollutant_measure = PollutantMeasure.objects.create(
            pollutant_name=create_pollutant("CO2", "Micrograms/m3", 2),
            measure=measure,
            quantity=100,
        )

    def test_pollutant_measure_creation(self):
        self.assertEqual(self.pollutant_measure.pollutant_name.name, "CO2")
        self.assertEqual(self.pollutant_measure.measure.station_code.code, 1)
        self.assertEqual(self.pollutant_measure.quantity, 100)

    def test_pollutant_measure_destroy(self):
        pollutant_measures_before = PollutantMeasure.objects.count()  # Nombre de PollutantMeasure que hi ha
        self.pollutant_measure.delete()
        pollutant_measures_after = PollutantMeasure.objects.count()
        self.assertEqual(pollutant_measures_after, pollutant_measures_before - 1)

    def test_pollutant_measure_update(self):
        self.pollutant_measure.pollutant_name = create_pollutant("pollutant updated", "Micrograms/m3",
                                                                 10)
        station = Station.objects.create(code=2, name="station2", location_id=create_location_geohash("dr5ru9pq8"))
        measure = create_measure(station, datetime.now().date(), datetime.now().time())
        self.pollutant_measure.measure = measure
        self.pollutant_measure.quantity = 2
        self.pollutant_measure.save()
        self.assertEqual(self.pollutant_measure.pollutant_name.name, "pollutant updated")
        self.assertEqual(self.pollutant_measure.measure.station_code.code, 2)
        self.assertEqual(self.pollutant_measure.quantity, 2)

    # Crear PollutantMeasure que violi la PK
    def test_pollutant_measure_invalid1(self):
        try:
            PollutantMeasure.objects.create(
                id=self.pollutant_measure.id,
                pollutant_name=create_pollutant("pollutant2", "Micrograms/m3", 10),
                measure=self.pollutant_measure.measure,
                quantity=0,
            )
            self.fail("It should raise an exception, pollutant_measure invalid1")
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            self.assertIn("UNIQUE constraint failed: api_pollutantmeasure.id", str(e))

    # Crear PollutantMeasure que violi la restriccio UNIQUE
    def test_pollutant_measure_invalid2(self):
        try:
            PollutantMeasure.objects.create(
                pollutant_name=self.pollutant_measure.pollutant_name,
                measure=self.pollutant_measure.measure,
                quantity=10
            )
            self.fail("It should raise an exception, pollutant_measure invalid2")
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            self.assertIn(
                "UNIQUE constraint failed: api_pollutantmeasure.pollutant_name_id, api_pollutantmeasure.measure_id",
                str(e)
            )

    # Crear PollutantMeasure amb measure None
    def test_pollutant_measure_invalid3(self):
        try:
            PollutantMeasure.objects.create(
                pollutant_name=self.pollutant_measure.pollutant_name,
                measure=None,
                quantity=10,
            )
            self.fail("It should raise an exception, pollutant_measure invalid3")
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            self.assertIn("NOT NULL constraint failed: api_pollutantmeasure.measure_id", str(e))
