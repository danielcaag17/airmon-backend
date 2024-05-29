from django.db import IntegrityError
from django.test import TestCase

from .utils import *
from ..models import Pollutant


class PollutantModelTest(TestCase):
    def setUp(self):
        self.pollutant = Pollutant.objects.create(
            name='Pollutant',
            measure_unit="Micrograms/m3",
        )

    def test_pollutant_creation(self):
        self.assertEqual(self.pollutant.name, "Pollutant")
        self.assertEqual(self.pollutant.measure_unit, "Micrograms/m3")

    def test_pollutant_destroy(self):
        pollutants_before = Pollutant.objects.count()  # Nombre de Pollutants que hi ha
        self.pollutant.delete()
        pollutants_after = Pollutant.objects.count()
        self.assertEqual(pollutants_after, pollutants_before - 1)

    def test_pollutant_update(self):
        self.pollutant.name = "CO2"
        self.pollutant.measure_unit = "Miligrams/m3"
        self.pollutant.save()
        self.assertEqual(self.pollutant.name, "CO2")
        self.assertEqual(self.pollutant.measure_unit, "Miligrams/m3")

    # Crear PlayerItem que violi la PK
    def test_pollutant_invalid1(self):
        try:
            Pollutant.objects.create(
                name=self.pollutant.name,
                measure_unit=self.pollutant.measure_unit,
            )
            self.fail("It should raise an exception, pollutant invalid1")
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            self.assertIn("UNIQUE constraint failed: api_pollutant.name", str(e))

    def test_pollutant_invalid2(self):
        try:
            Pollutant.objects.create(
                name="CO2",
                measure_unit="Unit inexistent",
            )
            self.fail("It should raise an exception, pollutant invalid2")
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
            self.assertIn("Invalid unit value.", str(e))
