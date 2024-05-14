from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Chat, ChatMessage
from ..serializers import MessageSerializer


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class ChatView(APIView):
    def get(self, request, *args, **kwargs):
        chat_id = kwargs.get("chat_id")
        last = request.query_params.get("last")
        if chat_id is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            chat = Chat.objects.get(id=chat_id)
        except Chat.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # Check if the user is in the chat
        if chat.user1 != request.user and chat.user2 != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        if last is not None and last == "true":

            try:
                message = ChatMessage.objects.filter(chat=chat).last()
            except ChatMessage.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            serializer = MessageSerializer(message)
            return Response(serializer.data)

        messages = ChatMessage.objects.filter(chat=chat)

        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)
