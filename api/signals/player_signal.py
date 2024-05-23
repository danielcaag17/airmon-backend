from django.db.models.signals import post_save, pre_save, post_delete
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


old_values_cache = {}


@receiver(pre_save, sender=Player)
def cache_old_values(sender, instance, **kwargs):
    if instance.pk:
        old_instance = Player.objects.get(pk=instance.pk)
        old_values_cache[instance.pk] = old_instance.coins


@receiver(post_save, sender=Player)
def player_updated(sender, instance, created, **kwargs):
    if created:
        pass
    else:
        old_coins = old_values_cache.get(instance.pk)
        new_coins = instance.coins

        # Player ha obtingut monedas
        if old_coins is not None and old_coins < new_coins:
            # Sumar la diferencia de monedes que ha guanyat
            instance.total_coins += new_coins - old_coins
            # Evitar bucle infinit
            instance.save(update_fields=['total_coins'])


@receiver(post_save, sender=Capture)
def capture_created(sender, instance, created, **kwargs):
    if created:
        player = Player.objects.get(user__username=instance.username)
        player.n_airmons_capturats += 1
        raresa = get_raresa(instance.airmon_id)
        if raresa in raresa_mapping:
            player_field = raresa_mapping[raresa]
            setattr(player, player_field, getattr(player, player_field) + 1)
            # Actualiza solo los campos modificados utilizando 'update_fields'
        update_fields = ['n_airmons_capturats'] + [raresa_mapping[raresa]] if raresa in raresa_mapping else []
        player.save(update_fields=update_fields)
    else:
        pass


raresa_mapping = {
    "Legendary": "total_airmons_legendary",
    "Mythical": "total_airmons_mythical",
    "Epic": "total_airmons_epic",
    "Special": "total_airmons_special",
    "Common": "total_airmons_common"
}


@receiver(post_delete, sender=Capture)
def mymodel_post_delete(sender, instance, **kwargs):
    player = Player.objects.get(user__username=instance.username)
    player.airmons_alliberats += 1
    player.save(update_fields=['airmons_alliberats'])
