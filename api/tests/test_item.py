from decimal import Decimal
from django.db import IntegrityError
from django.test import TestCase

from ..models import Item


class ItemModelTest(TestCase):
    def setUp(self):
        self.item = Item.objects.create(
            name="Item test",
            rarity="Llegendari",
            price=29.99,
            description="Description"
        )

    def test_item_creation(self):
        self.assertEqual(self.item.name, "Item test")
        self.assertEqual(self.item.rarity, "Llegendari")
        self.assertEqual(self.item.price, 29.99)
        self.assertEqual(self.item.description, "Description")

    # Crear un item amb més de dos decimals
    def test_item_creation2(self):
        item = Item.objects.create(
            name="Item",
            rarity="Epic",
            price=10.529424782,
            description="Description"
        )
        self.assertEqual(item.price, 10.53)

        item2 = Item.objects.create(
            name="Item2",
            rarity="Epic",
            price=10.52111,
            description="Description"
        )
        self.assertEqual(item2.price, 10.52)

    def test_item_destroy(self):
        items_before = Item.objects.count()  # Nombre de Items que hi ha
        self.item.delete()
        items_after = Item.objects.count()
        self.assertEqual(items_after, items_before - 1)

    def test_item_update(self):
        self.item.name = "Item updated"
        self.item.rarity = "Epic"
        self.item.price = 19.99
        self.item.description = "Description updated"
        self.item.save()
        self.assertEqual(self.item.name, "Item updated")
        self.assertEqual(self.item.rarity, "Epic")
        self.assertEqual(self.item.price, 19.99)
        self.assertEqual(self.item.description, "Description updated")

    # Modificar el preu d'un item amb més de dos decimals
    def test_item_update2(self):
        self.item.price = 32.2498324
        self.item.save()
        self.assertEqual(self.item.price, 32.25)

        self.item.price = 32.24111
        self.item.save()
        self.assertEqual(self.item.price, 32.24)

    def test_item_invalid1(self):
        try:
            Item.objects.create(
                name="Item test",
                rarity="Epic",
                price=10.50,
                description="Description invalid"
            )
            self.fail("It should raise an exception, item invalid1")
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            self.assertIn("UNIQUE constraint failed: api_item.name", str(e))

    # Crear item amb una raresa que no existeix
    def test_item_invalid2(self):
        try:
            Item.objects.create(
                name="Item invalid",
                rarity="Rarity que no existeix",
                price=10.50,
                description="Description invalid"
            )
            self.fail("It should raise an exception, item invalid2")
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
            self.assertIn("Invalid rarity value.", str(e))

