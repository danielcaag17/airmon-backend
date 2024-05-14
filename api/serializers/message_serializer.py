from rest_framework import serializers
from ..models import ChatMessage


class MessageSerializer(serializers.ModelSerializer):
    chat_id = serializers.SerializerMethodField(source='chat')
    content = serializers.CharField(source='message')
    date = serializers.DateTimeField()
    sender = serializers.SerializerMethodField(source='from_user')
    receiver = serializers.SerializerMethodField(source='to_user')
    read = serializers.BooleanField()

    class Meta:
        model = ChatMessage
        fields = ['chat_id', 'content', 'date', 'sender', 'receiver', 'read']

    def get_chat_id(self, obj):
        return obj.chat.id

    def get_sender(self, obj):
        return obj.from_user.username

    def get_receiver(self, obj):
        return obj.to_user.username
