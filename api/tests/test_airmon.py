from django.db import IntegrityError
from django.test import TestCase
from django.core.files import File
from django.core.files.uploadedfile import SimpleUploadedFile

from ..models import Airmon


class AirmonModelTest(TestCase):
    def setUp(self):
        image_path = 'api/tests/media-test/airmon-test.png'
        with open(image_path, 'rb') as f:
            image_file = File(f)
            self.uploaded_image = SimpleUploadedFile(image_file.name, image_file.read())
        self.airmon = Airmon.objects.create(
            name="Test airmon simple",
            description="Description simple",
            rarity="Llegendari",
            type="Lorem",
        )

    # Crear un Airmon
    def test_airmon_creation(self):
        self.assertEqual(self.airmon.name, "Test airmon simple")
        self.assertEqual(self.airmon.description, "Description simple")
        self.assertEqual(self.airmon.rarity, "Llegendari")
        self.assertEqual(self.airmon.type, "Lorem")
        self.assertEqual(self.airmon.image.name, "")

    # Eliminar un Airmon
    def test_airmon_destroy(self):
        airmons_before = Airmon.objects.count()  # Nombre de Airmons que hi ha
        self.airmon.delete()
        airmons_after = Airmon.objects.count()
        self.assertEqual(airmons_after, airmons_before - 1)

    # Modificar PK Airmon simple
    def test_airmon_update_PK(self):
        self.airmon.name = "Airmon renamed"
        self.airmon.save()
        self.assertEqual(self.airmon.name, "Airmon renamed")

    # Modificar atributs Airmon simple
    def test_airmon_update_attributes(self):
        self.airmon.description = "Description updated"
        self.airmon.rarity = "Llegendari"
        self.airmon.type = "Lorem"
        self.airmon.image = self.uploaded_image
        self.airmon.save()

        self.assertEqual(self.airmon.description, "Description updated")
        self.assertEqual(self.airmon.rarity, "Llegendari")
        self.assertEqual(self.airmon.type, "Lorem")
        self.assertNotEqual(self.airmon.image.name, "")

    # Crear un Airmon amb un name que ja exiteix
    def test_airmon_invalid1(self):
        try:
            Airmon.objects.create(
                name="Test airmon simple"
            )
            self.fail("It should raise an exception, airmon invalid1")
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            self.assertIn("UNIQUE constraint failed: api_airmon.name", str(e))

    # Crear Airmon amb len(name)>32
    def test_airmon_invalid2(self):
        try:
            Airmon.objects.create(
                name="Airmon amb nom de longitud superior a trenta-dos caracters",
                description="Description",
            )
            self.fail("It should raise an exception, airmon invalid2")
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
            self.assertIn("The name must be 32 characters or less.", str(e))

    # Crear Airmon amb una raresa que no existeix
    def test_airmon_invalid3(self):
        try:
            Airmon.objects.create(
                name="Test airmon invalid",
                rarity="Rarity que no existeix",
            )
            self.fail("It should raise an exception, airmon invalid3")
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
            self.assertIn("Invalid rarity value.", str(e))

    # Crear Airmon amb un tipus que no existeix
    def test_airmon_invalid4(self):
        try:
            Airmon.objects.create(
                name="Test airmon invalid",
                type="Tipus que no existeix",
            )
            self.fail("It should raise an exception, airmon invalid 4")
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
            self.assertIn("Invalid type value.", str(e))

    # Crear Airmon amb una imatge que no existeix
    def test_airmon_invalid5(self):
        try:
            # Per forçar l'excepció
            self.uploaded_image.close()
            Airmon.objects.create(
                name="Test airmon invalid",
                image=self.uploaded_image
            )
            self.fail("It should raise an exception, airmon invalid5")
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
            self.assertIn("I/O operation on closed file.", str(e))
