from django.db.models.signals import post_save
from django.dispatch import receiver

from .utils import *
from ..models import Capture, Player


@receiver(post_save, sender=Capture)
def capture_created(sender, instance, created, **kwargs):
    if created:
        player = Player.objects.get(user__username=instance.username)
        player.n_airmons_capturats += 1
        raresa = get_raresa(instance.airmon_id)
        if raresa in raresa_mapping:
            setattr(player, raresa_mapping[raresa], getattr(player, raresa_mapping[raresa]) + 1)
        player.save()
    else:
        print(f'User {instance.username} has been updated.')


raresa_mapping = {
    "Legendary": "total_airmons_legendary",
    "Mythical": "total_airmons_mythical",
    "Epic": "total_airmons_epic",
    "Special": "total_airmons_special",
    "Common": "total_airmons_common"
}
