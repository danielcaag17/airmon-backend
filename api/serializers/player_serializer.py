from rest_framework import serializers

from api.models import Player, Language


class PlayerSerializer(serializers.ModelSerializer):
    language = serializers.ChoiceField(choices=[(tag.value, tag.value) for tag in Language])
    username = serializers.SerializerMethodField()

    class Meta:
        model = Player
        fields = ['username', 'language', 'xp_points', 'coins', 'avatar']

    def get_username(self, obj):
        return obj.user.username
