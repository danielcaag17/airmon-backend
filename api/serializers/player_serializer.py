from rest_framework import serializers

from api.models import Player, Language, PlayerImages


class PlayerSerializer(serializers.ModelSerializer):
    language = serializers.ChoiceField(choices=[(tag.value, tag.value) for tag in Language])
    username = serializers.SerializerMethodField()
    password = serializers.SerializerMethodField()

    class Meta:
        model = Player
        fields = ['username', 'language', 'xp_points', 'coins', 'avatar', 'password']
        # TODO: correcte password si es atribut de user??

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
        read_only_fields = ['user']


class PlayerStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['n_airmons_capturats', 'airmons_alliberats', 'n_consumibles_usats',
                  'n_tirades_ruleta', 'total_coins', 'total_airmons_common', 'total_airmons_special',
                  'total_airmons_epic', 'total_airmons_mythical', 'total_airmons_legendary',
                  'total_compres',]
