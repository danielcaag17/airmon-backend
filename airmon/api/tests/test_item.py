from django.db import IntegrityError
from django.test import TestCase

from ..models import Item


class ItemModelTest(TestCase):
    def setUp(self):
        self.item = Item.objects.create(
            name="Item test",
            rarity="Legendary",
            price=29.99,
            description="Description"
        )

    def test_item_creation(self):
        self.assertEqual(self.item.name, "Item test")
        self.assertEqual(self.item.rarity, "Legendary")
        self.assertEqual(self.item.price, 29.99)
        self.assertEqual(self.item.description, "Description")

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

    def test_item_invalid1(self):
        try:
            Item.objects.create(
                name="Item test",
                rarity="Epic",
                price=10.50,
                description="Description invalid"
            )
            self.fail("It should raise an exception")
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            self.assertIn("UNIQUE constraint failed: api_item.name", str(e))

