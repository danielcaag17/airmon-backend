from datetime import datetime, timedelta
from django.test import TestCase
from django.db.utils import IntegrityError

from .utils import *


class MeasureModelTest(TestCase):
    def setUp(self):
        station = create_station(1, "station1", create_location_geohash("u09tunqp3d08"))
        self.measure = create_measure(station, datetime.now().date(), datetime.now().time())

    def test_measure_creation(self):
        self.assertEqual(self.measure.date, datetime.now().date())
        self.assertEqual(self.measure.station_code.code, 1)

        hora_actual = datetime.now()
        hora = datetime.combine(datetime.today(), self.measure.hour)
        diferencia = abs(hora_actual - hora)
        # Definir una tolerancia petita, 1 segon
        tolerancia = timedelta(seconds=1)
        # Validar que la diferencia entre els dos temps es menor que la tolerancia
        self.assertLessEqual(diferencia, tolerancia)

    def test_measure_destroy(self):
        measures_before = Measure.objects.count()  # Nombre de Measures que hi ha
        self.measure.delete()
        measures_after = Measure.objects.count()
        self.assertEqual(measures_after, measures_before - 1)

    def test_measure_update(self):
        station = create_station(2, "station2", create_location_geohash("dr5ru9pq8"))
        self.measure.station_code = station
        self.measure.save()
        self.assertEqual(self.measure.station_code.code, 2)

    def test_station_invalid1(self):
        try:
            Measure.objects.create(
                id=self.measure.id,
                station_code=create_station(2, "station2", create_location_geohash("dr5ru9pq8")),
                date=datetime.now().date(),
                hour=datetime.now().time()
            )
            self.fail("It should raise an exception, measure invalid1")
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            self.assertIn("UNIQUE constraint failed: api_measure.id", str(e))

    def test_station_invalid2(self):
        try:
            Measure.objects.create(
                station_code=self.measure.station_code,
                date=self.measure.date,
                hour=self.measure.hour,
            )
            self.fail("It should raise an exception, measure invalid2")
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            self.assertIn("UNIQUE constraint failed: api_measure.station_code_id, api_measure.date, api_measure.hour",
                          str(e))

    # Crear Measure sense station
    def test_station_invalid3(self):
        try:
            Measure.objects.create(
                id=self.measure.id,
                date=datetime.now().date(),
                hour=datetime.now().time()
            )
            self.fail("It should raise an exception, measure invalid1")
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            self.assertIn("NOT NULL constraint failed: api_measure.station_code_id", str(e))
