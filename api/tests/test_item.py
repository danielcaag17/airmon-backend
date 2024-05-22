import datetime
from decimal import Decimal
from django.db import IntegrityError
from django.test import TestCase

from ..models import Item


class ItemModelTest(TestCase):
    def setUp(self):
        self.item = Item.objects.create(
            name='coin_booster',
            price=100,
            description='30% more coins earned for 30 minutes',
            image='items/coin_booster.png',
            duration='00:30:00'
        )

    def test_item_creation(self):
        self.assertEqual(self.item.name, "coin_booster")
        self.assertEqual(self.item.duration, "00:30:00")
        self.assertEqual(self.item.price, 100)
        self.assertEqual(self.item.description, "30% more coins earned for 30 minutes")

    def test_item_destroy(self):
        items_before = Item.objects.count()  # Nombre de Items que hi ha
        self.item.delete()
        items_after = Item.objects.count()
        self.assertEqual(items_after, items_before - 1)

    def test_item_update(self):
        self.item.name = "Item updated"
        self.item.rarity = "Epic"
        self.item.price = 200
        self.item.description = "Description updated"
        self.item.save()
        self.assertEqual(self.item.name, "Item updated")
        self.assertEqual(self.item.rarity, "Epic")
        self.assertEqual(self.item.price, 200)
        self.assertEqual(self.item.description, "Description updated")

    # Modificar el preu d'un item amb més de dos decimals
    def test_item_update2(self):
        self.item.price = 123
        self.item.save()
        self.assertEqual(self.item.price, 123)

        self.item.price = 34871273
        self.item.save()
        self.assertEqual(self.item.price, 34871273)

    def test_item_invalid1(self):
        try:
            Item.objects.create(
                name="coin_booster",
                price=10392,
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
                price=-1,
                description="Description invalid"
            )
            self.fail("It should raise an exception, item invalid2")
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
