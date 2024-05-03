from rest_framework import serializers

from api.models import Player, Language, PlayerImages


class PlayerSerializer(serializers.ModelSerializer):
    language = serializers.ChoiceField(choices=[(tag.value, tag.value) for tag in Language])
    username = serializers.SerializerMethodField()
    password = serializers.SerializerMethodField()

    class Meta:
        model = Player
        fields = ['username', 'language', 'xp_points', 'coins', 'avatar', 'password']

    def get_username(self, obj):
        return obj.user.username

    def get_password(self, obj):
        return obj.user.password


class PlayerPublicSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = Player
        fields = ['username', 'avatar']

    def get_username(self, obj):
        return obj.user.username


class PlayerImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerImages
        fields = ['user', 'image', 'date']
