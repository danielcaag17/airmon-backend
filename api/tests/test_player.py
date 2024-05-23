from django.db import IntegrityError
from django.test import TestCase
from datetime import datetime
from django.core.files import File
from django.core.files.uploadedfile import SimpleUploadedFile

from ..models import Player, Friendship
from .utils import *


class PlayerModelTest(TestCase):
    def setUp(self):
        image_path = 'api/tests/media-test/avatar-test.png'
        with open(image_path, 'rb') as f:
            image_file = File(f)
            self.uploaded_image = SimpleUploadedFile(image_file.name, image_file.read())
        create_user("user1")
        self.player = Player.objects.get(user__username="user1")
        self.player.language="Catala"
        self.player.xp_points=10
        self.player.coins=0

    def test_player_creation(self):
        self.assertEqual(self.player.user.username, "user1")
        self.assertEqual(self.player.language, "Catala")
        self.assertEqual(self.player.xp_points, 10)
        self.assertEqual(self.player.coins, 0)
        # self.assertIsNone(self.player.avatar.name)

    '''
    def test_player_creation_with_avatar(self):
        player = Player.objects.create(
            user=create_user("user2"),
            language="Catala",
            xp_points=10,
            coins=0,
            avatar=self.uploaded_image,
        )
        self.assertNotEqual(player.avatar.name, "")
    '''

    def test_player_destroy(self):
        players_before = Player.objects.count()  # Nombre de Players que hi ha
        self.player.delete()
        players_after = Player.objects.count()
        self.assertEqual(players_after, players_before - 1)

    # Eliminar Player que té amistat, captura i chat
    def test_player_destroy2(self):
        user2 = create_user("user2")
        Friendship.objects.create(
            user1=self.player.user,
            user2=user2,
            date=datetime.now(get_timezone())
        )
        create_capture(self.player.user, create_airmon("Airmon"), datetime.now(get_timezone()), 0)
        Chat.objects.create(user1=self.player.user, user2=user2)

        players_before = Player.objects.count()  # Nombre de Players que hi ha
        friends_before = Friendship.objects.count()
        capture_before = Capture.objects.count()
        chat_before = Chat.objects.count()

        user = self.player.user
        user.delete()

        players_after = Player.objects.count()
        friends_after = Friendship.objects.count()
        capture_after = Capture.objects.count()
        chat_after = Chat.objects.count()

        self.assertEqual(players_after, players_before - 1)
        self.assertEqual(friends_after, friends_before - 1)
        self.assertEqual(capture_after, capture_before - 1)
        self.assertEqual(chat_after, chat_before - 1)

    def test_player_update(self):
        avatar_name_before = self.player.avatar.name
        image_path = 'api/tests/media-test/airmon-test.png'
        # with open(image_path, 'rb') as f:
        # image_file = File(f)
        # updated_image = SimpleUploadedFile(image_file.name, image_file.read())
        self.player.user = create_user("user2")
        self.player.language = "Castella"
        self.player.xp_points = 50
        self.player.coins = 100
        # self.player.avatar = updated_image
        self.player.save()

        self.assertEqual(self.player.user.username, "user2")
        self.assertEqual(self.player.language, "Castella")
        self.assertEqual(self.player.xp_points, 50)
        self.assertEqual(self.player.coins, 100)
        # self.assertNotEqual(self.player.avatar.name, avatar_name_before)

    # Crear Player amb un username existent
    def test_player_invalid1(self):
        try:
            Player.objects.create(
                user=User.objects.get(username=self.player.user.username)
            )
            self.fail("It should raise an exception, player invalid1")
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            self.assertIn("UNIQUE constraint failed: api_player.user", str(e))

    '''
    def test_player_invalid2(self):
        try:
            # Per forçar l'excepció
            self.uploaded_image.close()
            Player.objects.create(
                user=create_user("user2"),
                language="Catala",
                xp_points=10,
                coins=0,
                avatar=self.uploaded_image,
            )
            self.fail("It should raise an exception, player invalid2")
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
            self.assertIn("I/O operation on closed file.", str(e))
    '''

    # Crear player amb xp negatiu
    def test_player_invalid3(self):
        try:
            Player.objects.create(
                user=create_user("user2"),
                xp_points=-10,
            )
            self.fail("It should raise an exception, player invalid3")
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            self.assertIn("CHECK constraint failed: xp_points", str(e))

    # Crear player amb coins negatius
    def test_player_invalid4(self):
        try:
            Player.objects.create(
                user=create_user("user2"),
                coins=-10,
            )
            self.fail("It should raise an exception, player invalid4")
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            self.assertIn("CHECK constraint failed: coins", str(e))

    # Modificar player per tenir coins negatives
    def test_player_invalid5(self):
        self.player.coins = -10
        try:
            self.player.save()
            self.fail("It should raise an exception, player invalid5")
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            self.assertIn("CHECK constraint failed: coins", str(e))

    # Crear Player amb un llenguatge no valid
    def test_player_invalid6(self):
        try:
            Player.objects.create(
                user=create_user("user2"),
                language="Language inexistent",
            )
            self.fail("It should raise an exception, player invalid6")
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
            self.assertIn("Invalid language value.", str(e))
