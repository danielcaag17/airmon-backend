from django.utils import timezone

from ..models import PlayerActiveItem


def get_active_items(player_id):
    items = PlayerActiveItem.objects.filter(user=player_id)

    for item in items:
        if item.expiration < timezone.now():
            item.delete()

    return PlayerActiveItem.objects.filter(user=player_id)
