from django.contrib.auth.models import User
from rest_framework import serializers

from ..models import Friendship
from ..models import Chat
from ..models import Player, PlayerImages


class FriendshipSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    chat_id = serializers.SerializerMethodField()

    class Meta:
        model = Friendship
        fields = ['username', 'chat_id', 'date']

    def get_username(self, obj):
        if obj.user1.username == self.context['username']:
            return obj.user2.username
        else:
            return obj.user1.username

    def get_chat_id(self, obj):
        return Chat.objects.get(user1__username=obj.user1,
                                user2__username=obj.user2).id
