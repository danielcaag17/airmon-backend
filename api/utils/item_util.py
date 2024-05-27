from django.utils import timezone

from ..models import PlayerActiveItem, Capture, Airmon
from ..serializers import AirmonSerializer


def get_active_items(user):
    items = PlayerActiveItem.objects.filter(user=user)

    for item in items:
        if item.expiration < timezone.now():
            item.delete()

    return PlayerActiveItem.objects.filter(user=user)


def handle_specific_action(user, item_name):
    if item_name == 'coin_booster':
        return
    elif item_name == 'exp_booster':
        return
    elif item_name == 'extra_roulette_spin':
        return
    elif item_name == 'airbox':
        return _handle_airbox(user)

    return


def _handle_airbox(user):
    airmon = Airmon.objects.order_by('?').first()
    Capture.objects.create(user=user, airmon=airmon, date=timezone.now(), attempts=0)
    return AirmonSerializer(airmon).data
