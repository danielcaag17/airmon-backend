from django.test import TestCase

from ..models import Airmon


class AirmonModelTest(TestCase):
    def setUp(self):
        Airmon.objects.create(
            name="Test airmon simple",
            description="Description simple",
        )

    # Crear un Airmon simple
    def test_airmon_creation(self):
        airmon = Airmon.objects.get(name="Test airmon simple")
        self.assertEqual(airmon.name, "Test airmon simple")
        self.assertEqual(airmon.description, "Description simple")
        self.assertEqual(airmon.rarity, "")
        self.assertEqual(airmon.type, "")
        # Canviar model si es necessari
        # self.assertEqual(airmon.image, None)

    # Crear airmon amb tots els atributs TODO
    def test_airmon_creation2(self):
        airmon = Airmon.objects.create(
            name="Airmon creation2",
            description="Description",
            rarity="Llegendari",
            type="Lorem",
            image=None
        )
        self.assertEqual(airmon.name, "Airmon creation2")
        self.assertEqual(airmon.description, "Description")
        self.assertEqual(airmon.rarity, "Llegendari")
        self.assertEqual(airmon.type, "Lorem")
        self.assertEqual(airmon.image, None)



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
        except Exception as e:
            print("Type:", type(e))
            print("Error:", e)

    # Crear Airmon amb len(name)>32
    def test_airmon_invalid2(self):
        try:
            Airmon.objects.create(
                name="Airmon amb nom de longitud superior a trenta-dos caracters",
                description="Description",
            )
        except Exception as e:
            print("Type:", type(e))
            print("Error:", e)


