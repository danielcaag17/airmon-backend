from django.db import IntegrityError
from django.test import TestCase
from datetime import datetime, timedelta
import time

from .utils import *
from ..models import ChatMessage


def create_chat_message(from_user, to_user, message, read):
    return ChatMessage.objects.create(
            chat=create_chat(from_user, to_user),
            message=message,
            date=datetime.now(get_timezone()),
            from_user=User.objects.get(username=from_user),
            to_user=User.objects.get(username=to_user),
            read=False,
        )


class ChatMessageModelTest(TestCase):
    def setUp(self):
        self.chat_message = create_chat_message("user1", "user2", "Message", False)

    # Crear un ChatMessage
    def test_chat_message_creation(self):
        self.assertEqual(self.chat_message.message, "Message")
        self.assertEqual(self.chat_message.from_user.username, "user1")
        self.assertEqual(self.chat_message.to_user.username, "user2")
        self.assertFalse(self.chat_message.read)

        hora_actual = datetime.now(get_timezone())
        diferencia = abs(self.chat_message.date - hora_actual)
        # Definir una tolerancia petita, 1 segon
        tolerancia = timedelta(seconds=1)
        # Validar que la diferencia entre els dos temps es menor que la tolerancia
        self.assertLessEqual(diferencia, tolerancia)

    # Crear diversos ChatMessages amb el mateix Chat
    def test_chat_message_creation2(self):
        messages = ["hola", "hola", "aixo es una conversa"]
        for message in messages:
            time.sleep(1)
            ChatMessage.objects.create(
                chat=self.chat_message.chat,
                from_user=self.chat_message.from_user,
                to_user=self.chat_message.to_user,
                message=message,
                date=datetime.now(get_timezone())
            )
        self.assertEqual(ChatMessage.objects.count(), 1+len(messages))

    # Eliminar un ChatMessage
    def test_chat_message_destroy(self):
        chat_messages_before = ChatMessage.objects.count()  # Nombre de ChatMessages que hi ha
        self.chat_message.delete()
        chat_messages_after = ChatMessage.objects.count()
        self.assertEqual(chat_messages_after, chat_messages_before - 1)

    # Modificar un ChatMessage
    def test_chat_message_update(self):
        self.chat_message.chat = create_chat("user3", "user4")
        self.chat_message.from_user = User.objects.get(username="user3")
        self.chat_message.to_user = User.objects.get(username="user4")
        self.chat_message.message = "Message updated"
        self.chat_message.read = True
        self.chat_message.save()

        self.assertEqual(self.chat_message.from_user.username, 'user3')
        self.assertEqual(self.chat_message.to_user.username, 'user4')
        self.assertEqual(self.chat_message.message, "Message updated")
        self.assertTrue(self.chat_message.read)

    # Crear ChatMessage amb una PK existent
    # TODO: canviar la PK perque tampoc es pot crear mes d'un missatge al mateix chat
    def test_chat_message_invalid1(self):
        try:
            ChatMessage.objects.create(
                chat=self.chat_message.chat,
                from_user=self.chat_message.from_user,
                to_user=create_user("user3"),
                date=datetime.now(get_timezone()) + timedelta(minutes=1)
            )
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            self.assertIn("UNIQUE constraint failed: api_chatmessage.chat_id", str(e))
        except Exception as e:
            self.fail("A IntegrityError exception was expected, but was raised: {}".format(e))

    '''
    # Crear ChatMessage amb dos Users que no son els del Chat
    def test_chat_message_invalid2(self):
        try:
            ChatMessage.objects.create(
                chat=create_chat("user3", "user4"),
                from_user=self.chat_message.from_user,  # user1
                to_user=self.chat_message.to_user,      # user2
                date=datetime.now(get_timezone()) + timedelta(minutes=1),
                message="Invalid message",
            )
            self.fail("Un chat de dos usuaris que no son el from_ i el to_")
        except IntegrityError as e:
            self.assertIsInstance(e, IntegrityError)
            self.assertIn("UNIQUE constraint failed: api_chatmessage.chat_id", str(e))
        except Exception as e:
            self.fail("A IntegrityError exception was expected, but was raised: {}".format(e))
    '''


