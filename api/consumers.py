import json

from channels.db import database_sync_to_async
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from api.models import Chat, ChatMessage
from django.contrib.auth.models import User


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        print(self.scope["url_route"]["kwargs"])
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        self.send(text_data=json.dumps({"message": message}))


class AsyncChatConsumer(AsyncWebsocketConsumer):
    """
    Please note that this consumer is ASYNC, so we need to take into account that
    we can't use blocking calls like calling to ORM methods, etc.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.chat_name = None
        self.chat_id = None
        self.users = []

    async def connect(self):
        self.chat_id = self.scope["url_route"]["kwargs"]["chat_id"]
        self.chat_name = f"chat_{self.chat_id}"

        chat = await get_chat_by_id(self.chat_id)
        if chat is None:
            await self.close()  # TODO ENSURE CHAT EXISTS
            return

        user = self.scope["user"]
        print(user)

        if user is None:  # No logged user
            await self.close()
            return

        # Check if user is part of chat
        user1_id = await get_chat_user1_id(chat)
        user2_id = await get_chat_user2_id(chat)

        if user.id != user1_id and user.id != user2_id:
            await self.close()
            return

        # Check if user is already in chat
        if user.id in self.users:
            return

        self.users.append(user.id)

        # Join room group
        await self.channel_layer.group_add(self.chat_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        user = self.scope["user"]
        if user.id in self.users:
            self.users.remove(user.id)
        await self.channel_layer.group_discard(self.chat_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        user = self.scope["user"]

        chat = await get_chat_by_id(self.chat_id)

        user1_id = await get_chat_user1_id(chat)
        user2_id = await get_chat_user2_id(chat)
        receiver = user1_id if user.id == user2_id else user2_id

        reading = receiver.id in self.users

        await create_chat_message(chat, message, user, receiver, reading)

        # Send message to room group
        await self.channel_layer.group_send(
            self.chat_name, {"type": "chat.message", "message": message, "from_user": user.username, "read": reading}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        from_user = event["from_user"]
        read = event["read"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message, "from_user": from_user, "read": read}))


@database_sync_to_async  # We need to run database queries asynchronously
def get_chat_by_id(chat_id):
    return Chat.objects.get(id=chat_id)


@database_sync_to_async  # We need to run database queries asynchronously
def get_chat_user1_id(chat):
    return chat.user1.id


@database_sync_to_async  # We need to run database queries asynchronously
def get_chat_user2_id(chat):
    return chat.user2.id


@database_sync_to_async  # We need to run database queries asynchronously
def create_chat_message(chat, message, from_user, to_user, read):
    return ChatMessage.objects.create(chat=chat, message=message, from_user=from_user, to_user=to_user, read=read)
