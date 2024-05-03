from django.test import TestCase
from django.db import IntegrityError

from ..models import Chat
from .utils import *


class ChatModelTest(TestCase):
    def setUp(self):
        self.chat = Chat.objects.create(
            user1=create_user('user1'),
            user2=create_user('user2')
        )

    # Crear un Chat
    def test_chat_creation(self):
        self.assertEqual(self.chat.user1.username, 'user1')
        self.assertEqual(self.chat.user2.username, 'user2')

    # Eliminar un Chat
    def test_chat_destroy(self):
        chats_before = Chat.objects.count()  # Nombre de Chats que hi ha
        self.chat.delete()
        chats_after = Chat.objects.count()
        self.assertEqual(chats_after, chats_before - 1)

    # Modificar un Chat
    def test_chat_update(self):
        self.chat.user1 = create_user('user3')
        self.chat.user2 = User.objects.get(username='user1')
        self.chat.save()
        self.assertEqual(self.chat.user1.username, 'user3')
        self.assertEqual(self.chat.user2.username, 'user1')

    # Crear un chat amb un conjunt UNIQUE existent
    def test_chat_invalid1(self):
        try:
            Chat.objects.create(user1=self.chat.user1, user2=self.chat.user2)
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            self.assertIn("UNIQUE constraint failed: api_chat.user1_id, api_chat.user2_id", str(e))
        except Exception as e:
            self.fail("A IntegrityError exception was expected, but was raised: {}".format(e))

    # Crear un Chat sense user1
    def test_chat_invalid2(self):
        try:
            Chat.objects.create(user1=None, user2=self.chat.user2)
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            self.assertIn("NOT NULL constraint failed: api_chat.user1_id", str(e))
        except Exception as e:
            self.fail("A IntegrityError exception was expected, but was raised: {}".format(e))

    # Crear un Chat sense user2
    def test_chat_invalid3(self):
        try:
            Chat.objects.create(user1=self.chat.user1, user2=None)
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            self.assertIn("NOT NULL constraint failed: api_chat.user2_id", str(e))
        except Exception as e:
            self.fail("A IntegrityError exception was expected, but was raised: {}".format(e))

    # Crear un Chat amb el mateix User
    def test_chat_invalid4(self):
        try:
            Chat.objects.create(user1=self.chat.user1, user2=self.chat.user1)
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            self.assertIn("CHECK constraint failed: different_users_chat", str(e))
        except Exception as e:
            self.fail("A IntegrityError exception was expected, but was raised: {}".format(e))

    '''
    # Crear un Chat amb dos users que ja tenien un Chat, pero intercanviats
    def test_chat_invalid5(self):
        try:
            Chat.objects.create(user1=self.chat.user2, user2=self.chat.user1)
            self.fail("It should raise an exception")
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            print(e)
            # self.assertIn("", str(e))
        except Exception as e:
            self.fail("A IntegrityError exception was expected, but was raised: {}".format(e))
    '''
