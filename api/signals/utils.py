from ..models import Airmon


def get_raresa(airmon_name):
    airmon = Airmon.objects.get(name=airmon_name)
    return airmon.rarity
