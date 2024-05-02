from rest_framework import serializers
from ..models import ChatMessage


class MessageSerializer(serializers.ModelSerializer):
    model = ChatMessage
    fields = ['chat', 'message', 'date', 'from_user', 'to_user', 'read']
