from django.utils import timezone

from ..models import PlayerActiveItem


def get_active_items(player_id):
    items = PlayerActiveItem.objects.filter(user=player_id)

    result = []
    for item in items:
        if item.expiration < timezone.now():
            item.delete()
        else:
            result.append(item)

    return result


def add_active_item(player_id, item_id, expiration):
    item = PlayerActiveItem(user=player_id, item_name=item_id, expiration=expiration)
    item.save()
    return item
