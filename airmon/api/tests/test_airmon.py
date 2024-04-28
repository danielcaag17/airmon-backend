from django.db import IntegrityError
from django.test import TestCase
from django.core.files import File
from django.core.files.uploadedfile import SimpleUploadedFile

from ..models import Airmon


class AirmonModelTest(TestCase):
    def setUp(self):
        Airmon.objects.create(
            name="Test airmon simple",
            description="Description simple",
        )
        image_path = 'airmon/api/tests/media-test/airmon-test.png'
        with open(image_path, 'rb') as f:
            image_file = File(f)
            self.uploaded_image = SimpleUploadedFile(image_file.name, image_file.read())

    # Crear un Airmon simple
    def test_airmon_creation(self):
        airmon = Airmon.objects.get(name="Test airmon simple")
        self.assertEqual(airmon.name, "Test airmon simple")
        self.assertEqual(airmon.description, "Description simple")
        self.assertEqual(airmon.rarity, "Common")
        self.assertEqual(airmon.type, "Lorem")
        self.assertEqual(airmon.image.name, "")

    # Crear airmon amb tots els atributs
    def test_airmon_creation2(self):
        airmon = Airmon.objects.create(
            name="Airmon creation2",
            description="Description",
            rarity="Legendary",
            type="Lorem",
            image=self.uploaded_image
        )
        self.assertEqual(airmon.name, "Airmon creation2")
        self.assertEqual(airmon.description, "Description")
        self.assertEqual(airmon.rarity, "Legendary")
        self.assertEqual(airmon.type, "Lorem")
        self.assertNotEquals(airmon.image.name, "")

    # Eliminar Airmon simple
    def test_airmon_destroy(self):
        airmons_before = Airmon.objects.count()  # Nombre de Airmons que hi ha
        airmon = Airmon.objects.get(name="Test airmon simple")
        airmon.delete()
        airmons_after = Airmon.objects.count()
        self.assertEqual(airmons_after, airmons_before - 1)

    # Modificar PK Airmon simple
    def test_airmon_update_PK(self):
        airmon = Airmon.objects.get(name="Test airmon simple")
        airmon.name = "Airmon renamed"
        airmon.save()
        airmon_updated = Airmon.objects.get(name="Airmon renamed")
        self.assertEqual(airmon_updated.name, "Airmon renamed")

    # Modificar atributs Airmon simple
    def test_airmon_update_attributes(self):
        airmon = Airmon.objects.get(name="Test airmon simple")
        airmon.description = "Description updated"
        airmon.rarity = "Legendary"
        airmon.type = "Lorem"
        airmon.image = self.uploaded_image
        airmon.save()
        airmon_updated = Airmon.objects.get(name="Test airmon simple")
        self.assertEqual(airmon_updated.description, "Description updated")
        self.assertEqual(airmon_updated.rarity, "Legendary")
        self.assertEqual(airmon_updated.type, "Lorem")
        self.assertNotEqual(airmon_updated.image.name, "")

    # Crear un Airmon amb un name que ja exiteix
    def test_airmon_invalid1(self):
        try:
            Airmon.objects.create(
                name="Test airmon simple"
            )
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            self.assertIn("UNIQUE constraint failed: api_airmon.name", str(e))
        except Exception as e:
            self.fail("A ValidationError exception was expected, but was raised: {}".format(e))

    # Crear Airmon amb len(name)>32
    def test_airmon_invalid2(self):
        try:
            Airmon.objects.create(
                name="Airmon amb nom de longitud superior a trenta-dos caracters",
                description="Description",
            )
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
            self.assertIn("The name must be 32 characters or less.", str(e))
        except Exception as e:
            self.fail("A ValidationError exception was expected, but was raised: {}".format(e))

    # Crear Airmon amb una raresa que no existeix
    def test_airmon_invalid3(self):
        try:
            Airmon.objects.create(
                name="Test airmon invalid",
                rarity="Rarity que no existeix",
            )
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
            self.assertIn("Invalid rarity value.", str(e))
        except Exception as e:
            self.fail("A ValidationError exception was expected, but was raised: {}".format(e))

    # Crear Airmon amb un tipus que no existeix
    def test_airmon_invalid4(self):
        try:
            Airmon.objects.create(
                name="Test airmon invalid",
                type="Tipus que no existeix",
            )
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
            self.assertIn("Invalid type value.", str(e))
        except Exception as e:
            self.fail("A ValidationError exception was expected, but was raised: {}".format(e))

    # Crear Airmon amb una imatge que no existeix
    def test_airmon_invalid5(self):
        try:
            # Per forçar l'excepció
            self.uploaded_image.close()
            a = Airmon.objects.create(
                name="Test airmon invalid",
                image=self.uploaded_image
            )
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
            self.assertIn("I/O operation on closed file.", str(e))
        except Exception as e:
            self.fail("A ValidationError exception was expected, but was raised: {}".format(e))

