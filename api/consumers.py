import json

from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from .models import Chat, ChatMessage


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        self.send(text_data=json.dumps({"message": message}))


class AsyncChatConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.chat_name = None
        self.chat_id = None
        self.users = []

    async def connect(self):
        self.chat_id = self.scope["url_route"]["kwargs"]["chat_id"]
        self.chat_name = f"chat_{self.chat_id}"

        chat = Chat.objects.get(id=self.chat_id)
        if not chat.exists():
            await self.close()  # TODO ENSURE CHAT EXISTS
            return

        user = self.scope["user"]

        # Check if user is part of chat
        if user.id != chat.user1.id and user.id != chat.user2.id:
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
        self.users.remove(user.id)
        await self.channel_layer.group_discard(self.chat_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        user = self.scope["user"]

        chat = Chat.objects.get(id=self.chat_id)
        receiver = chat.user1 if user.id == chat.user2.id else chat.user2

        reading = receiver.id in self.users

        ChatMessage.objects.create(chat=chat, message=message, from_user=user, to_user=receiver, read=reading)

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
