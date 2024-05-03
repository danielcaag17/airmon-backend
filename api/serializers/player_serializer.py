from rest_framework import serializers

from api.models import Player, Language, PlayerImages


class PlayerSerializer(serializers.ModelSerializer):
    language = serializers.ChoiceField(choices=[(tag.value, tag.value) for tag in Language])

    class Meta:
        model = Player
        fields = ['user', 'language', 'xp_points', 'coins', 'avatar']


class PlayerImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerImages
        fields = ['image', 'date']

