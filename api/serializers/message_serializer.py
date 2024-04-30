from rest_framework import serializers
from ..models import ChatMessage


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = ['chat', 'message', 'date', 'from_user', 'to_user', 'read']
