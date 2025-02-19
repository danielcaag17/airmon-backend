from django.test import TestCase
from django.db import IntegrityError
from datetime import datetime, timedelta

from .utils import *
from ..models import Player, PlayerTrophy


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



"""
class PlayerTrophySignalTest(TestCase):
    def setUp(self):
        self.user = create_user('test user1')
        self.player = Player.objects.get(user=self.user)
        self.item = create_item("item test", 1, "description", None, "00:30:00")
        create_trophies()
        create_airmons()

    def test_player_trophy_none(self):
        n_player_trophies = PlayerTrophy.objects.filter(user=self.user).count()
        self.assertEqual(n_player_trophies, 0)

    def test_coins_copper_trophy(self):
        self.player.coins += 15
        self.player.save()
        trophy = Trophy.objects.get(name="trophy11", type="BRONZE")
        player_trophy = PlayerTrophy.objects.filter(user=self.user, trophy=trophy).exists()
        self.assertTrue(player_trophy)

    def test_coins_gold_trophy(self):
        self.player.coins += 100
        self.player.save()
        n_player_trophy = PlayerTrophy.objects.filter(user=self.user, trophy__name="trophy11").count()
        self.assertEqual(n_player_trophy, 3)

    def test_purchases_copper_trophy(self):
        self.player.coins += 15
        self.player.save()
        create_player_item(self.user, self.item, 10)
        trophy = Trophy.objects.get(name="trophy10", type="BRONZE")
        player_trophy = PlayerTrophy.objects.filter(user=self.user, trophy=trophy).exists()
        self.assertTrue(player_trophy)

    def test_captures_copper_trophy(self):
        airmons = Airmon.objects.all()
        primers_airmons = airmons[:10]
        for airmon in primers_airmons:
            create_capture(self.user, airmon)
        trophy = Trophy.objects.get(name="trophy1", type="BRONZE")
        player_trophy = PlayerTrophy.objects.filter(user=self.user, trophy=trophy).exists()
        self.assertTrue(player_trophy)

    def test_captures_gold_trophy(self):
        airmons = Airmon.objects.all()
        primers_airmons = airmons[:10]
        for i in range(5):
            for airmon in primers_airmons:
                create_capture(self.user, airmon)
        n_player_trophy = PlayerTrophy.objects.filter(user=self.user, trophy__name="trophy1").count()
        self.assertEqual(n_player_trophy, 3)

    def test_realeses_copper_trophy(self):
        airmons = Airmon.objects.all()
        primers_airmons = airmons[:5]
        for airmon in primers_airmons:
            capture = create_capture(self.user, airmon)
            capture.delete()
        trophy = Trophy.objects.get(name="trophy2", type="BRONZE")
        player_trophy = PlayerTrophy.objects.filter(user=self.user, trophy=trophy).exists()
        self.assertTrue(player_trophy)
"""