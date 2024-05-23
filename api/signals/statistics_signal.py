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
        action = raresa_actions.get(raresa, lambda player: handle_default(player))
        action(player)
        player.save()
    else:
        print(f'User {instance.username} has been updated.')



