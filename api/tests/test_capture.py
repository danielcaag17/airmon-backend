from django.test import TestCase
from datetime import datetime, timedelta
from django.db import IntegrityError
from django.core.exceptions import ValidationError

from .utils import *
from ..models import Capture, Airmon


class CaptureModelTest(TestCase):
    def setUp(self):
        self.capture = create_capture(create_user("User test"),
                                      create_airmon("Airmon test"),
                                      datetime.now(get_timezone()), 0)

    def test_capture_creation(self):
        self.assertEqual(self.capture.username.username, 'User test')
        self.assertEqual(self.capture.airmon.name, 'Airmon test')
        self.assertEqual(self.capture.attempts, 0)

        hora_actual = datetime.now(get_timezone())
        diferencia = abs(self.capture.date - hora_actual)
        # Definir una tolerancia petita, 1 segon
        tolerancia = timedelta(seconds=1)
        # Validar que la diferencia entre els dos temps es menor que la tolerancia
        self.assertLessEqual(diferencia, tolerancia)

    # Eliminar Capture simple
    def test_capture_destroy(self):
        captures_before = Capture.objects.count()  # Nombre de Captures que hi ha
        self.capture.delete()
        captures_after = Capture.objects.count()
        self.assertEqual(captures_after, captures_before - 1)

    # Modificar els atributs i PK de Capture simple
    def test_capture_update(self):
        user = create_user("User updated")
        airmon = create_airmon("Airmon updated")
        self.capture.username = user
        self.capture.airmon = airmon
        self.capture.attempts = 1
        self.capture.save()

        capture_updated = Capture.objects.get(username=user.id, airmon=airmon.name, date=self.capture.date)
        self.assertEqual(capture_updated.id, self.capture.id)
        self.assertEqual(capture_updated.attempts, 1)

    # Crear Caputre amb mateixa PK
    def test_capture_invalid1(self):
        try:
            Capture.objects.create(
                id=self.capture.id,
                username=create_user("User invalid"),
                airmon=create_airmon("Airmon invalid"),
                date=datetime.now(get_timezone()),
                attempts=10
            )
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            self.assertIn("UNIQUE constraint failed: api_capture.id", str(e))
        except Exception as e:
            self.fail("A IntegrityError exception was expected, but was raised: {}".format(e))

    # Crear una Capture amb un conjunt UNIQUE existent
    def test_capture_invalid2(self):
        try:
            user = User.objects.get(username=self.capture.username.username)
            airmon = Airmon.objects.get(name=self.capture.airmon.name)
            create_capture(user, airmon, self.capture.date, self.capture.attempts)
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            self.assertIn("UNIQUE constraint failed: api_capture.airmon_id, api_capture.username_id, api_capture.date", str(e))
        except Exception as e:
            self.fail("A IntegrityError exception was expected, but was raised: {}".format(e))

    # Crear Capture sense User
    def test_capture_invalid3(self):
        try:
            airmon = Airmon.objects.get(name=self.capture.airmon.name)
            create_capture(None, airmon, self.capture.date, self.capture.attempts)
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            self.assertIn("NOT NULL constraint failed: api_capture.username_id", str(e))
        except Exception as e:
            self.fail("A IntegrityError exception was expected, but was raised: {}".format(e))

    # Crear Capture sense Airmon
    def test_capture_invalid4(self):
        try:
            user = User.objects.get(username=self.capture.username.username)
            create_capture(user, None, self.capture.date, self.capture.attempts)
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            self.assertIn("NOT NULL constraint failed: api_capture.airmon_id", str(e))
        except Exception as e:
            self.fail("A IntegrityError exception was expected, but was raised: {}".format(e))

    # Crear Caputre amb date superior a actual
    def test_capture_invalid5(self):
        try:
            user = User.objects.get(username=self.capture.username.username)
            airmon = Airmon.objects.get(name=self.capture.airmon.name)
            create_capture(user, airmon, self.capture.date + timedelta(days=2), self.capture.attempts)
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
            self.assertIn("The date cannot be in the future.", str(e))
        except Exception as e:
            self.fail("A ValueError exception was expected, but was raised: {}".format(e))

    # Crear Capture amb attemps inferior a 0
    def test_capture_invalid6(self):
        try:
            user = User.objects.get(username=self.capture.username.username)
            airmon = Airmon.objects.get(name=self.capture.airmon.name)
            create_capture(user, airmon, datetime.now(get_timezone()), -100)
        except ValidationError as e:
            self.assertIsInstance(e, ValidationError)
            self.assertIn("The number of attempts must be a positive number.", str(e))
        except Exception as e:
            self.fail("A ValidationError exception was expected, but was raised: {}".format(e))


