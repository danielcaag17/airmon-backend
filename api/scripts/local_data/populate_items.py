from api.scripts.django_setup import setup_django

setup_django()

from api.models import Item

Item.objects.create(
    name='coin_booster',
    price=100,
    description='30% more coins earned for 30 minutes',
    image='items/coin_booster.png',
    duration='00:30:00'
)

Item.objects.create(
    name='exp_booster',
    price=100,
    description='30% more experience earned for 2 hours',
    image='items/exp_booster.png',
    duration='02:00:00'
)

Item.objects.create(
    name='extra_roulette_spin',
    price=100,
    description='1 extra roulette spin',
    image='items/extra_roulette_spin.png',
    duration='00:00:00'
)

Item.objects.create(
    name='airbox',
    price=1000,
    description='Open this box to get a random airmon',
    image='items/airbox.png',
    duration='00:00:00'
)

