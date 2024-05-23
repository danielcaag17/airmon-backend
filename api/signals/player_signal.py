from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from .utils import get_raresa
from ..models import Capture, Player


@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created:
        user = User.objects.get(username=instance.username)
        Player.objects.create(user=user, avatar=None)
    else:
        pass


@receiver(post_save, sender=Player)
def player_updated(sender, instance, created, **kwargs):
    if created:
        pass
    else:
        # Instancia no modificada
        old_instance = Player.objects.get(pk=instance.pk)

        # Player ha obtingut monedes
        if old_instance.coins < instance.coins:
            # Sumar la diferencia de monedes que ha guanyat
            instance.total_coins = instance.coins - old_instance.coins
            # Evitar bucle infinit
            instance.save(update_fields=['total_coins'])


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
        pass


raresa_mapping = {
    "Legendary": "total_airmons_legendary",
    "Mythical": "total_airmons_mythical",
    "Epic": "total_airmons_epic",
    "Special": "total_airmons_special",
    "Common": "total_airmons_common"
}
