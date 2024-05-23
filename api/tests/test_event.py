from django.test import TestCase
from django.db import IntegrityError
from datetime import datetime, timedelta

from .utils import *


class EventModelTest(TestCase):
    def setUp(self):
        data_ini = datetime.today() - timedelta(days=2)
        data_fi = datetime.today() + timedelta(days=2)
        geohash = LocationGeohash.objects.coords_to_geohash(latitude=41.1231, longitude=0.12312)
        self.loc = LocationGeohash.objects.create(geohash=geohash)
        self.event = create_event(1, "denominacio", data_ini, data_fi, self.loc, "espai")

    def test_event_creation(self):
        self.assertEqual(self.event.codi, 1)
        self.assertEqual(self.event.denominacio, "denominacio")
        self.assertEqual(self.event.geohash, self.loc)
        self.assertEqual(self.event.espai, "espai")

    def test_event_destroy(self):
        events_before = Event.objects.count()  # Nombre de Events que hi ha
        self.event.delete()
        events_after = Event.objects.count()
        self.assertEqual(events_after, events_before - 1)

    def test_event_update(self):
        self.event.codi = 2
        self.event.denominacio = "denominacio updated"
        self.event.espai = "espai updated"
        self.event.save()
        self.assertEqual(self.event.codi, 2)
        self.assertEqual(self.event.denominacio, "denominacio updated")
        self.assertEqual(self.event.espai, "espai updated")

    # Crear Event que violi la PK
    def test_event_invalid1(self):
        try:
            create_event(codi=self.event.codi, denominacio="denominacio erro", data_ini=self.event.data_ini,
                         data_fi=self.event.data_fi, geohash=self.event.geohash, espai="espai error")
            self.fail("It should raise an exception, event invalid2")
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            self.assertIn("UNIQUE constraint failed: api_event.codi", str(e))
