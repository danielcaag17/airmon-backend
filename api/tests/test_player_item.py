from django.db import IntegrityError
from django.test import TestCase

from .utils import *
from ..models import PlayerItem


class PlayerItemModelTest(TestCase):
    def setUp(self):
        self.player_item = PlayerItem.objects.create(
            item_name=create_item("item", 10, "description", "00:30:00"),
            user=create_user("user1"),
            quantity=100,
        )

    def test_player_item_creation(self):
        self.assertEqual(self.player_item.item_name.name, "item")
        self.assertEqual(self.player_item.user.username, "user1")
        self.assertEqual(self.player_item.quantity, 100)

    def test_player_item_destroy(self):
        player_items_before = PlayerItem.objects.count()  # Nombre de PlayerItems que hi ha
        self.player_item.delete()
        player_items_after = PlayerItem.objects.count()
        self.assertEqual(player_items_after, player_items_before - 1)

    def test_player_item_update(self):
        self.player_item.item_name = create_item("item updated",
                                                 100, "description", "00:30:00")
        self.player_item.username = create_user("user2")
        self.player_item.quantity = 2
        self.player_item.save()
        self.assertEqual(self.player_item.item_name.name, "item updated")
        self.assertEqual(self.player_item.username.username, "user2")
        self.assertEqual(self.player_item.quantity, 2)

    # Crear PlayerItem que violi la PK
    def test_player_item_invalid1(self):
        try:
            PlayerItem.objects.create(
                id=self.player_item.id,
                item_name=create_item("item2", 10, "Description", "00:30:00"),
                user=create_user("user2"),
                quantity=0,
            )
            self.fail("It should raise an exception, player_item invalid1")
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            self.assertIn("UNIQUE constraint failed: api_playeritem.id", str(e))

    # Crear PlayerItem que violi la restriccio UNIQUE
    def test_player_item_invalid2(self):
        try:
            PlayerItem.objects.create(
                item_name=self.player_item.item_name,
                user=self.player_item.user,
                quantity=0,
            )
            self.fail("It should raise an exception, player_item invalid2")
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            self.assertIn("UNIQUE constraint failed: api_playeritem.item_name_id, api_playeritem.user_id",
                          str(e))

    # Crear PlayerItem amb quantity negativa
    def test_player_item_invalid3(self):
        try:
            PlayerItem.objects.create(
                item_name=create_item("item2", 100, "Description", duration="00:30:00"),
                user=create_user("user2"),
                quantity=-123,
            )
            self.fail("It should raise an exception, player_item invalid3")
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            self.assertIn("CHECK constraint failed: quantity", str(e))

    # Crear PlayerItem sense User
    def test_player_item_invalid4(self):
        try:
            PlayerItem.objects.create(
                item_name=create_item("item2", 100, "Description", duration="00:30:00"),
                user=None,
                quantity=-123,
            )
            self.fail("It should raise an exception, player_item invalid4")
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            self.assertIn("NOT NULL constraint failed: api_playeritem.user_id", str(e))

