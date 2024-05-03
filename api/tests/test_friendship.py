from datetime import datetime, timedelta

from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.db import IntegrityError
from django.test import TestCase

from .utils import *
from ..models import Friendship


class FriendshipModelTest(TestCase):
    def setUp(self):
        self.friend = Friendship.objects.create(
            user1=create_user("user1"),
            user2=create_user("user2"),
            date=datetime.now(get_timezone())
        )

    def test_friendship_creation(self):
        self.assertEqual(self.friend.user1.username, "user1")
        self.assertEqual(self.friend.user2.username, "user2")

        hora_actual = datetime.now(get_timezone())
        diferencia = abs(self.friend.date - hora_actual)
        # Definir una tolerancia petita, 1 segon
        tolerancia = timedelta(seconds=1)
        # Validar que la diferencia entre els dos temps es menor que la tolerancia
        self.assertLessEqual(diferencia, tolerancia)

    def test_friendship_destroy(self):
        friendships_before = Friendship.objects.count()  # Nombre de Friendships que hi ha
        self.friend.delete()
        friendships_after = Friendship.objects.count()
        self.assertEqual(friendships_after, friendships_before - 1)

    def test_friendship_update(self):
        self.friend.user1 = create_user("user3")
        self.friend.user2 = create_user("user4")
        self.friend.save()
        self.assertEqual(self.friend.user1.username, "user3")
        self.assertEqual(self.friend.user2.username, "user4")

    # Crear un friendship amb PK existent
    def test_friendship_invalid1(self):
        try:
            Friendship.objects.create(
                id=self.friend.id,
                user1=create_user("user3"),
                user2=create_user("user4"),
                date=datetime.now(get_timezone())
            )
            self.fail("It should raise an exception, friendship invalid1")
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            self.assertIn("UNIQUE constraint failed: api_friendship.id", str(e))

    # Crear un friendship violant la restricció UNIQUE
    def test_friendship_invalid2(self):
        try:
            Friendship.objects.create(
                user1=self.friend.user1,
                user2=self.friend.user2,
                date=datetime.now(get_timezone())
            )
            self.fail("It should raise an exception, friendship invalid2")
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            self.assertIn("UNIQUE constraint failed: api_friendship.user1_id, api_friendship.user2_id", str(e))

    # Crear un friendship amb una data futura
    def test_friendship_invalid3(self):
        try:
            Friendship.objects.create(
                user1=create_user("user3"),
                user2=create_user("user4"),
                date=datetime.now(get_timezone()) + timedelta(days=2)
            )
            self.fail("It should raise an exception, friendship invalid3")
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
            self.assertIn("The date cannot be in the future.", str(e))

    # Crear un friendship amb els user intercanviats
    def test_friendship_invalid4(self):
        try:
            Friendship.objects.create(
                user1=self.friend.user2,
                user2=self.friend.user1,
                date=datetime.now(get_timezone())
            )
            self.fail("It should raise an exception, friendship invalid4")
        except ValidationError as e:
            self.assertIsInstance(e, ValidationError)
            self.assertIn("The friendship already exists.", str(e))

    # Crear un friendship amb el mateix user
    def test_friendship_invalid5(self):
        try:
            Friendship.objects.create(
                user1=self.friend.user1,
                user2=self.friend.user1,
                date=datetime.now(get_timezone())
            )
            self.fail("It should raise an exception, friendship invalid5")
        except ValidationError as e:
            self.assertIsInstance(e, ValidationError)
            self.assertIn("Users cannot be the same.", str(e))

    # Crear una amistat amb només un usuari
    def test_friendship_invalid6(self):
        try:
            Friendship.objects.create(
                user1=None,
                user2=self.friend.user2,
                date=datetime.now(get_timezone())
            )
            self.fail("It should raise an exception, friendship invalid6")
        except ObjectDoesNotExist as e:
            self.assertIsInstance(e, ObjectDoesNotExist)
            self.assertIn("Friendship has no user1.", str(e))

