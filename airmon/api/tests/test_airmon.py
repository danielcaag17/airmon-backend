from django.test import TestCase
from django.db.utils import IntegrityError

from ..models import Airmon


class AirmonModelTest(TestCase):
    def setUp(self):
        Airmon.objects.create(
            name="Test airmon simple",
            description="Description simple"
        )

    # Crear un Airmon simple
    def test_airmon_creation(self):
        airmon = Airmon.objects.get(name="Test airmon simple")
        self.assertEqual(airmon.name, "Test airmon simple")
        self.assertEqual(airmon.description, "Description simple")
        self.assertEqual(airmon.type, "")
        self.assertEqual(airmon.type, "")
        # Canviar model si es necessari
        # self.assertEqual(airmon.image, None)

    # Eliminar Airmon simple
    def test_aimon_destroy(self):
        airmons_before = Airmon.objects.count() # Nombre de Airmons
        airmon = Airmon.objects.get(name="Test airmon simple")
        airmon.delete()
        airmons_after = Airmon.objects.count()
        self.assertEqual(airmons_after, airmons_before - 1)

    # Modificar PK Airmon simple
    def test_airmon_update_attributes(self):
        airmon = Airmon.objects.get(name="Test airmon simple")
        airmon.name = "Airmon renamed"
        airmon.save()
        self.assertEqual(airmon.name, "Airmon renamed")

    # Modificar atributs Airmon simple
    def test_airmon_update_attributes(self):
        airmon = Airmon.objects.get(name="Test airmon simple")
        airmon.description = "Description updated"
        airmon.save()
        self.assertEqual(airmon.description, "Description updated")

    # Crear un Airmon amb un name que ja exiteix
    def test_airmon_invalid1(self):
        try:
            Airmon.objects.create(
                name="Test airmon simple"
            )
        except IntegrityError as e:
            print("Type:", type(e))
            print("Error:", e)



