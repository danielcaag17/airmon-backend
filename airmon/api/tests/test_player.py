from django.db import IntegrityError
from django.test import TestCase
from django.core.files import File
from django.core.files.uploadedfile import SimpleUploadedFile

from ..models import Player
from .utils import *


class PlayerModelTest(TestCase):
    def setUp(self):
        image_path = 'airmon/api/tests/media-test/avatar-test.png'
        with open(image_path, 'rb') as f:
            image_file = File(f)
            self.uploaded_image = SimpleUploadedFile(image_file.name, image_file.read())
        self.player = Player.objects.create(
            user=create_user("user1"),
            language="Catala",
            xp_points=10,
            coins=0,
            avatar=self.uploaded_image,
        )

    def test_player_creation(self):
        self.assertEqual(self.player.user.username, "user1")
        self.assertEqual(self.player.language, "Catala")
        self.assertEqual(self.player.xp_points, 10)
        self.assertEqual(self.player.coins, 0)
        self.assertNotEqual(self.player.avatar.name, "")

    def test_player_destroy(self):
        players_before = Player.objects.count()  # Nombre de Players que hi ha
        self.player.delete()
        players_after = Player.objects.count()
        self.assertEqual(players_after, players_before - 1)

    def test_player_update(self):
        avatar_name_before = self.player.avatar.name
        image_path = 'airmon/api/tests/media-test/airmon-test.png'
        with open(image_path, 'rb') as f:
            image_file = File(f)
            updated_image = SimpleUploadedFile(image_file.name, image_file.read())
        self.player.user = create_user("user2")
        self.player.language = "Castella"
        self.player.xp_points = 50
        self.player.coins = 100
        self.player.avatar = updated_image
        self.player.save()

        self.assertEqual(self.player.user.username, "user2")
        self.assertEqual(self.player.language, "Castella")
        self.assertEqual(self.player.xp_points, 50)
        self.assertEqual(self.player.coins, 100)
        self.assertNotEqual(self.player.avatar.name, avatar_name_before)

    def test_player_invalid1(self):
        try:
            Player.objects.create(
                user=User.objects.get(username=self.player.user.username)
            )
            self.fail("It should raise an exception")
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            self.assertIn("UNIQUE constraint failed: api_player.user", str(e))
