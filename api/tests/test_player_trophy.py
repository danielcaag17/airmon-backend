from django.test import TestCase
from django.db import IntegrityError
from datetime import datetime, timedelta

from ..models import PlayerTrophy
from .utils import *
from ..models import PlayerTrophy


class PlayerTrophyModelTest(TestCase):
    def setUp(self):
        self.player_trophy = PlayerTrophy.objects.create(
            user=create_user('test user1'),
            trophy=create_trophy("test trophy", "Or", "test description", 3, 123),
            date=datetime.now(get_timezone()),
        )

    def test_player_trophy_creation(self):
        self.assertEqual(self.player_trophy.user.username, "test user1")
        self.assertEqual(self.player_trophy.trophy.name, "test trophy")
        self.assertEqual(self.player_trophy.trophy.type, "Or")
        self.assertEqual(self.player_trophy.trophy.description, "test description")
        self.assertEqual(self.player_trophy.trophy.requirement, 3)
        self.assertEqual(self.player_trophy.trophy.xp, 123)

        hora_actual = datetime.now(get_timezone())
        diferencia = abs(self.player_trophy.date - hora_actual)
        # Definir una tolerancia petita, 1 segon
        tolerancia = timedelta(seconds=1)
        # Validar que la diferencia entre els dos temps es menor que la tolerancia
        self.assertLessEqual(diferencia, tolerancia)

    def test_player_trophy_destroy(self):
        player_trophies_before = PlayerTrophy.objects.count()  # Nombre de PlayerTrophies que hi ha
        self.player_trophy.delete()
        player_trophies_after = PlayerTrophy.objects.count()
        self.assertEqual(player_trophies_after, player_trophies_before - 1)

    def test_trophy_update(self):
        self.player_trophy.user = create_user('user2')
        self.player_trophy.trophy = create_trophy("trophy2", "Or", "new description",
                                                  10, 123)
        self.player_trophy.save()
        self.assertEqual(self.player_trophy.user.username, "user2")
        self.assertEqual(self.player_trophy.trophy.name, "trophy2")

    # Crear PlayerTrophy que violi la PK
    def test_player_trophy_invalid1(self):
        try:
            PlayerTrophy.objects.create(
                id=self.player_trophy.id,
                user=create_user('test user2'),
                trophy=create_trophy("test trophy2", "Or", "description invalid", 10, 123),
                date=datetime.now(get_timezone()),
            )
            self.fail("It should raise an exception, player_trophy invalid1")
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            self.assertIn("UNIQUE constraint failed: api_playertrophy.id", str(e))

    # Crear PlayerTrophy que violi la restriccio UNIQUE
    def test_player_trophy_invalid2(self):
        try:
            PlayerTrophy.objects.create(
                user=self.player_trophy.user,
                trophy=self.player_trophy.trophy,
                date=datetime.now(get_timezone()),
            )
            self.fail("It should raise an exception, player_trophy invalid2")
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            self.assertIn("UNIQUE constraint failed: api_playertrophy.user_id, api_playertrophy.trophy_id",
                          str(e))

    # Crear PlayerTrophy amb trophy NULL
    def test_player_trophy_invalid3(self):
        try:
            PlayerTrophy.objects.create(
                user=create_user('test user2'),
                trophy=None,
                date=datetime.now(get_timezone()),
            )
            self.fail("It should raise an exception, player_trophy invalid3")
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            self.assertIn("NOT NULL constraint failed: api_playertrophy.trophy_id", str(e))

