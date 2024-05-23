from rest_framework import serializers

from api.models import PlayerTrophy


class PlayerTrophySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerTrophy
        fields = '__all__'
