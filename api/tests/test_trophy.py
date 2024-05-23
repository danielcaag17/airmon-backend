from django.test import TestCase
from django.db import IntegrityError

from ..models import Trophy


class TrophyModelTest(TestCase):
    def setUp(self):
        self.trophy = Trophy.objects.create(
            name='Test Trophy',
            type="Or",
            description="test description",
            requirement=3,
            xp=123
        )

    def test_trophy_creation(self):
        self.assertEqual(self.trophy.name, "Test Trophy")
        self.assertEqual(self.trophy.type, "Or")
        self.assertEqual(self.trophy.description, "test description")
        self.assertEqual(self.trophy.requirement, 3)
        self.assertEqual(self.trophy.xp, 123)

    def test_trophy_destroy(self):
        trophies_before = Trophy.objects.count()  # Nombre de Trophies que hi ha
        self.trophy.delete()
        trophies_after = Trophy.objects.count()
        self.assertEqual(trophies_after, trophies_before - 1)

    def test_trophy_update(self):
        self.trophy.name = "Trophy updated"
        self.trophy.type = "Plata"
        self.trophy.description = "new description"
        self.trophy.requirement = 10
        self.trophy.xp = 2
        self.trophy.save()
        self.assertEqual(self.trophy.name, "Trophy updated")
        self.assertEqual(self.trophy.type, "Plata")
        self.assertEqual(self.trophy.description, "new description")
        self.assertEqual(self.trophy.requirement, 10)
        self.assertEqual(self.trophy.xp, 2)

    # Crear Trophy que violi la PK
    def test_trophy_invalid1(self):
        try:
            Trophy.objects.create(
                id=self.trophy.id,
                name="Trophy name",
                type="Or",
                description="test description",
                requirement=3,
                xp=0,
            )
            self.fail("It should raise an exception, trophy invalid1")
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            self.assertIn("UNIQUE constraint failed: api_trophy.id", str(e))

    # Crear Trophy que violi la restriccio UNIQUE
    def test_trophy_invalid2(self):
        try:
            Trophy.objects.create(
                name=self.trophy.name,
                type=self.trophy.type,
                description=self.trophy.description,
                requirement=self.trophy.requirement,
                xp=0,
            )
            self.fail("It should raise an exception, trophy invalid2")
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            self.assertIn("UNIQUE constraint failed: api_trophy.name, api_trophy.type", str(e))

    # Crear Trophy amb type NULL
    def test_trophy_invalid3(self):
        try:
            Trophy.objects.create(
                name=self.trophy.name,
                type=None,
                description="test description",
                requirement=3,
                xp=0,
            )
            self.fail("It should raise an exception, trophy invalid3")
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            self.assertIn("NOT NULL constraint failed: api_trophy.type", str(e))

    # Crear Trophy amb xp negativa
    def test_trophy_invalid4(self):
        try:
            Trophy.objects.create(
                name=self.trophy.name,
                type=self.trophy.type,
                description="test description",
                requirement=3,
                xp=-123,
            )
            self.fail("It should raise an exception, trophy invalid4")
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            self.assertIn("CHECK constraint failed: xp", str(e))
