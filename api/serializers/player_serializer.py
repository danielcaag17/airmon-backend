from rest_framework import serializers

from api.models import Player, Language, PlayerImages


class PlayerSerializer(serializers.ModelSerializer):
    language = serializers.ChoiceField(choices=Language.choices)
    username = serializers.SerializerMethodField()

    class Meta:
        model = Player
        fields = ['username', 'language', 'xp_points', 'coins', 'avatar']

    def get_username(self, obj):
        return obj.user.username


class PlayerPublicSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = Player
        fields = ['username', 'avatar', 'xp_points']

    def get_username(self, obj):
        return obj.user.username


class PlayerImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerImages
        fields = ['user', 'image', 'date']
        read_only_fields = ['user']


class PlayerStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['n_airmons_capturats', 'airmons_alliberats', 'n_consumibles_usats',
                  'n_tirades_ruleta', 'total_coins', 'total_airmons_common', 'total_airmons_special',
                  'total_airmons_epic', 'total_airmons_mythical', 'total_airmons_legendary',
                  'total_compres',]
