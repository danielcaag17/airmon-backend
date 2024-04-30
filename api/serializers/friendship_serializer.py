from rest_framework import serializers

from ..models import Friendship


class FriendshipSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = Friendship
        fields = ['username', 'date']

    def get_username(self, obj):
        if obj.user1.username == self.context['username']:
            return obj.user2.username
        else:
            return obj.user1.username

