from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Chat, ChatMessage
from ..serializers import MessageSerializer


class ChatView(APIView):
    def get(self, request, *args, **kwargs):
        chat_id = kwargs.get("chat_id")
        if chat_id is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        chat = Chat.objects.get(id=chat_id)
        if chat is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # Check if the user is in the chat
        if chat.user1 != request.user and chat.user2 != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        messages = ChatMessage.objects.filter(chat=chat)

        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)
